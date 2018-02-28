#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys   
from dingtalkchatbot.chatbot import DingtalkChatbot
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=#yourtoken'

def ddbot_text(webhook,text):
    xiaoding = DingtalkChatbot(webhook)
    # Text消息
    xiaoding.send_text(msg=text)

if __name__ == "__main__":
    ddbot_text(webhook,'text')
