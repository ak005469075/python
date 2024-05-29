import requests;

def get_cookie():
	he={ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}

	url="http://登录页面"

	params={
	'username':'xxx',
	'password':'xxx',
	'type':'xxx'
	}


	res=requests.post(url=url,headers=he,data=params,verify=False)
	#这里是只有一个值才这样，如果有多个请拼接
	for i in res.cookies:
		cookie=f"{i.name}={i.value};"
	print(cookie)
	final_cookie=f"{cookie} sdsad=asdasd;"
	return final_cookie

