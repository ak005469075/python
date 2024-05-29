import requests;
import os;
from login import get_cookie

cookie=get_cookie()
print(cookie)
header={

'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',

'Cookie': cookie,

'Referer': 'xxx',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'

}
a,b=input("输入导出月份和天数，如5 31：").split()
a=int(a)
b=int(b)
filepath=f"C:\\Users\\Administrator\\Desktop\\{a}"
if not os.path.exists(filepath):
	os.mkdir(filepath)
print(f"正在导出到{filepath}")
a=str(a) if a>9 else "0"+str(a)
for i in range(1,b+1):
	i=str(i) if i>9 else "0"+str(i)
	url=f"http://xxx/{a}-{i}/xxx/{a}-{i}/xxx"	
	r=requests.get(url=url,headers=header)
	if r.status_code == 200:
		fp=open(f"{filepath}\\{a}-{i}.xls","wb")
		fp.write(r.content)
		fp.close()
	else:
		print(f"[-]错误")

print("即使没有数据也会写进去，所以需要请打开文件确认一下")