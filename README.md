# tieba_qiandao
#### 百度贴吧极速签到,200个吧用时1.6秒,简单直接 <br />
**需要的第三方库:requests,gevent,pyquery**.<br />
**安装第三方库```pip install requests gevent pyquery```**

**配置:**<br />
**Update:**
在网页端登陆百度贴吧，F12打开控制台，复制你的cookie到ba_cookie处,OK.
![说明图片](http://opgtctagy.bkt.clouddn.com/Snipaste_2017-08-24_10-45-10.png)

**运行:**<br />
首次运行会在文件同目录下生成qd_config.ini配置文件<br />
运行后会提示运行方式,输入go回车,是签到,直接回车是检查签到状态,未签到或者贴吧无法签到(贴吧被封/贴吧没有任何帖子/贴吧名被重定向)会在控制台输出"吧名-->Error".<br />
解决方案:贴吧被封无解;极少数情况下的贴吧没有任何帖子,实际会已签到但显示Error;贴吧被重定向可以把重定向前的名称删掉,然后替换为重定向后的名称.<br />
**不足**:请提issues或Pull requests
