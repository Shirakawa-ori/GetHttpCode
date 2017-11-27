# GetHttpCode

很菜的代码。。<br>
需要用到redis<br>
pip install redis<br>
<br>
编辑add.sh批量添加关注的网站 必须有http:// 或者https:// 不然会报错<br>
<br>
status.py 是网页展示<br>
getHttpCode.py 获取Http状态码<br>
callsendmail.py 用作邮件通知（需要换成自己的stmp和邮箱）<br>
getHttpCode.py 循环获取脚本<br>
msgqmail.py 读取队列发送邮件<br>
<br>后台运行请使用nohup<br>
