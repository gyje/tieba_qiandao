# tieba_qiandao
#### 百度贴吧极速签到,200个吧用时1.6秒,简单直接 <br />
**需要的第三方库:requests,gevent**.<br />

**配置:**
1. 先正常登录[百度贴吧](tieba.baidu.com),然后访问[WAP贴吧](http://wapp.baidu.com/)<br />
2. F12打开控制台,Network选项卡,点击左上角我爱逛的贴吧,![点击左上角我爱逛的贴吧](http://opgtctagy.bkt.clouddn.com/1.png)<br />
3. 把图中的Request Headers内容复制替换qiandao.py中的Headers,复制图中的RequestURL,到`fid=...&kw=`截至,替换qiandao.py中的url,把cookie复制到qiandao.py中ba_cookie处![tu2](http://opgtctagy.bkt.clouddn.com/2.png)<br />
4. 点击图中的更多,显示所有你关注的贴吧![图3](http://opgtctagy.bkt.clouddn.com/3.png)<br />
复制吧名到notepad++中,用正则表达式或其它方式转为("steam","图拉丁","Erlang"······)的形式,然后复制替换qiandao.py中的ba_name_tuple<br /><br />

**运行:**<br />
运行后会提示运行方式,输入go回车,是签到,直接回车是检查签到状态,未签到或者贴吧无法签到(贴吧被封/贴吧没有任何帖子/贴吧名被重定向)会在控制台输出"吧名-->Error"<br />

**不足**:代码写的比较烂,只是为了实现功能,没考虑优雅.如果有不正确的地方请issues或Pull requests
