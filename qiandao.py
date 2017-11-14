import requests,time,gevent,gevent.monkey,re,os
from threading import Thread
from pyquery import PyQuery as pq
gevent.monkey.patch_socket()

url="http://tieba.baidu.com/mo/q---F55A5B1F58548A7A5403ABA7602FEBAE%3AFG%3D1--1-1-0--2--wapp_1510665393192_464/sign?tbs=af62312bf49309c61510669752&fid=152744&kw="
ba_cookie='把cookies复制到这儿'

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
def writeconfig():
	temp=pq(requests.get("http://wapp.baidu.com/",headers={'Cookie':ba_cookie}).content)
	ba_all_url="http://"+str([i.attr("href") for i in temp(".my_love_bar").children().items()][-1])[2:]
	retemp=re.compile(r">\w*</a>")
	ba_name_list=[]
	for i in retemp.findall(requests.get(ba_all_url,headers={'Cookie':ba_cookie}).text)[1:-2]:
		ba_name_list.append(i[1:-4])
	with open("qd_config.ini","w+",encoding="utf-8") as fob:
		fob.write(str(tuple(ba_name_list)))
def checkconfig():
	if "qd_config.ini" in os.listdir(os.getcwd()):
		pass
	else:
		writeconfig()
def readconfig():
	global ba_name_tuple
	with open("qd_config.ini","r",encoding="utf-8") as fob:
		ba_name_tuple=eval(fob.read())
if __name__=="__main__":
	checkconfig()
	readconfig()
	index=input("how work?\n")
	if index=="go":
		star=time.time()
		go()
		print (time.time()-star)
	else:
		checkth()
