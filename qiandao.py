import requests,time,gevent,gevent.monkey,re
from threading import Thread
gevent.monkey.patch_socket()

url="http://tieba.baidu.com/mo/....../&kw="
ba_cookie=""
ba_name_tuple=('steam','单机游戏','使命召唤6','杀戮间','汉服','图拉丁','为知笔记')#windows下gevent有1024个Port限制,所以超过1024个可能出错

headers={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cookie':ba_cookie,
'Host':'tieba.baidu.com',
'Proxy-Connection':'keep-alive',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
s=requests.Session()
def run(ba_url,ba_name):
	qian_url=ba_url+ba_name
	s.get(qian_url,headers=headers)
def go():
	taske=[gevent.spawn(run,url,i) for i in ba_name_tuple]
	gevent.joinall(taske)
rebuild=re.compile(r"已签到")
def check(ba_name):
	content=s.get(url+ba_name,headers=headers).text
	return_list=rebuild.findall(content)
	if str(return_list)=="['已签到']":
		pass
	else:
		print (ba_name+"-->Error")
def checkth():
	for g in ba_name_tuple:
		m=Thread(target=check,args=(g,))
		m.start()
if __name__=="__main__":
	index=input("how work?\n")
	if index=="go":
		star=time.time()
		go()
		print (time.time()-star)
	else:
		checkth()
	
