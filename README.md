# tieba_qiandao
#### 百度贴吧极速签到,200个吧用时1.6秒,简单直接 <br />
**需要的第三方库:requests,gevent,pyquery**.<br />

**配置:**
1. 先正常登录[百度贴吧](tieba.baidu.com),然后访问[WAP贴吧](http://wapp.baidu.com/)<br />
2. F12打开控制台,Network选项卡,点击左上角我爱逛的贴吧,![点击左上角我爱逛的贴吧](http://opgtctagy.bkt.clouddn.com/1.png)<br />
3. <s>把图中的Request Headers内容复制替换qiandao.py中的Headers,复制图中的RequestURL,到`fid=...&kw=`截至,替换qiandao.py中的url,</s>把cookie复制到qiandao.py中ba_cookie处![tu2](http://opgtctagy.bkt.clouddn.com/2.png)<br />

**运行:**<br />
首次运行会在文件同目录下生成qd_config.ini配置文件<br />
运行后会提示运行方式,输入go回车,是签到,直接回车是检查签到状态,未签到或者贴吧无法签到(贴吧被封/贴吧没有任何帖子/贴吧名被重定向)会在控制台输出"吧名-->Error".<br />
解决方案:贴吧被封无解;极少数情况下的贴吧没有任何帖子,实际会已签到但显示Error;贴吧被重定向可以把重定向前的名称删掉,然后替换为重定向后的名称.<br />
**不足**:代码写的比较烂,只是为了实现功能,没考虑优雅.如果有不正确的地方请issues或Pull requests
