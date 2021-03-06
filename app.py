# -*- coding: utf-8 -*-
import os
from flask import Flask, request
import json
import requests
#import psycopg2

import re
import random
from bs4 import BeautifulSoup
from collections import defaultdict
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from linebot import LineBotApi
from linebot.exceptions import LineBotApiError

from tinydb import TinyDB, Query
# end import module



####google sheet####
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


global cell

scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("dcs-report").sheet1  # Open the spreadhseet
cell = sheet.cell(2,2).value  # Get the value of a specific cell
####google sheet####


########################## TinyDb #################
db = TinyDB('db.json')
item = Query()
########################## TinyDb #################


'''
try:
    conn = psycopg2.connect("dbname='d6nfkhldr8m73b' user='dxebvbtkaavoqw' host='ec2-54-235-114-242.compute-1.amazonaws.com' password='850c57e80ca8ddc9bd59b42511534ca024b3b02e98b85646746e937551fefeb8'")
    cur = conn.cursor()

except:
    print 'cannot connect'
'''



app = Flask(__name__)
#line_bot_api = LineBotApi('wbeBaLPb7xIuGymdaHU9yHy300QZ383XYgewhXLSoRe3TnlWo1xQuypNFpis1ExGrSTV1WpmtmQEiaR9tRPQHFUspwI9rVk2Ajfrg1WUwFpV9ewvq/vDx9LItfeNW+9y6Ih/OcwNpJPB/UfE9afIFwdB04t89/1O/w1cDnyilFU=') # Channel Access Token DCS-BOT
#handler = WebhookHandler('49a9d31e3b8135ee7f85e6bc78848baa') # Channel Secret DCS-BOT

#line_bot_api = LineBotApi('CFaQZEnotjzhRjT4JMbcMyA0cksM4HE9Zu7HA8xQdWVbOMh6HLdeiCp2NKv6gmjNmJHs+NhWvnk8DYUZ3r8mCX6goDgYby/EV9s+/2mR9piHnPUVUGzWhRlmWw5K8RQG8iwgtSPnw89zEaUILnhtMwdB04t89/1O/w1cDnyilFU=') # Channel Access Token Report
#handler = WebhookHandler('f1e03e9bb185204d4494a1cce993970a') # Channel Secret Report

line_bot_api = LineBotApi('3vo+d/hHTrjlVBrJoCbiAiMWk9J3a40OyCQ0hbRyefioHo8CqR/Uyn4LVCJay7X6Y+NzdR1bzI+W5IH5wiiQUWQMf0Ezqo08YChiLExXTSTs7fpdcs/pa9HPfOw3XwSd7i9yPaR6ujvhBbQezdsytgdB04t89/1O/w1cDnyilFU=') # Channel Access Token Report
handler = WebhookHandler('9cfd6ef939de3489cadbccdda4e2c653') # Channel Secret Report
#end Token

# for test route
@app.route('/')
def hello():
    return 'Hello World! thongpoon Sarsaiy'

@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good</h2>'


@app.route('/query/<name>')
def profile(name):
    a = str(db.search(item.type == name))
    return '<h2>Tuna is good %s</h2>' % a
    #return '<h2>Tuna is good %s</h2>' % name

########################### Line API ###############
@handler.default()
def default(event):
    print(event)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)

    ########################################## Dcs report User ask ################################################
    #paper
    if event.message.text == "Serv":
        msg = 'No Data'
        msg = sheet.cell(2,1).value  # Get the value of a specific cell
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0

        '''
        msg = 'No Data'
        try:
            cur.execute("""SELECT * from t_report""")
        except:
            print 'cannot select'

        rows = cur.fetchall()
        for row in rows:
            msg = row[1]

        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
    #paper   
    if event.message.text == "Temp":
        msg = 'No Data'
        msg = sheet.cell(2,2).value  # Get the value of a specific cell
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
        msg = 'No Data'
        try:
            cur.execute("""SELECT * from t_report""")
        except:
            print 'cannot select'

        rows = cur.fetchall()
        for row in rows:
            msg = row[2]

        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
    #paper
    if event.message.text == "Rect":
        msg = 'No Data'
        msg = sheet.cell(2,3).value  # Get the value of a specific cell
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
        msg = 'No Data'
        try:
            cur.execute("""SELECT * from t_report""")
        except:
            print 'cannot select'

        rows = cur.fetchall()
        for row in rows:
            msg = row[3]

        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
    #paper
    if event.message.text == "Netw":
        msg = 'No Data'
        msg = sheet.cell(2,4).value  # Get the value of a specific cell
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
        msg = 'No Data'
        try:
            cur.execute("""SELECT * from t_report""")
        except:
            print 'cannot select'

        rows = cur.fetchall()
        for row in rows:
            msg = row[4]

        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
    #paper
    if event.message.text == "Cont":
        msg = 'No Data'
        msg = sheet.cell(2,5).value  # Get the value of a specific cell
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
        msg = 'No Data'
        try:
            cur.execute("""SELECT * from t_report""")
        except:
            print 'cannot select'

        rows = cur.fetchall()
        for row in rows:
            msg = row[5]

        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
    #paper
    if event.message.text == "Report":
        msg = 'No Data'
        msg = sheet.cell(2,6).value  # Get the value of a specific cell
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
        msg = 'No Data'
        try:
            cur.execute("""SELECT * from t_report""")
        except:
            print 'cannot select'

        rows = cur.fetchall()
        for row in rows:
            msg = row[8]

        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
################################################## pulp ###################################
    #pulp
    if event.message.text == "Tmp":
        msg = 'No Data'
        msg = sheet.cell(2,7).value  # Get the value of a specific cell
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
        msg = 'No Data'
        try:
            cur.execute("""SELECT * from t_report""")
        except:
            print 'cannot select'

        rows = cur.fetchall()
        for row in rows:
            msg = row[10]

        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
    #pulp
    if event.message.text == "Rct":
        msg = 'No Data'
        msg = sheet.cell(2,8).value  # Get the value of a specific cell
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
        msg = 'No Data'
        try:
            cur.execute("""SELECT * from t_report""")
        except:
            print 'cannot select'

        rows = cur.fetchall()
        for row in rows:
            msg = row[11]

        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''        
    #pulp
    if event.message.text == "Net":
        msg = 'No Data'
        msg = sheet.cell(2,9).value  # Get the value of a specific cell
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
        msg = 'No Data'
        try:
            cur.execute("""SELECT * from t_report""")
        except:
            print 'cannot select'

        rows = cur.fetchall()
        for row in rows:
            msg = row[6]

        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
    #pulp
    if event.message.text == "Con":
        msg = 'No Data'
        msg = sheet.cell(2,10).value  # Get the value of a specific cell
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
        msg = 'No Data'
        try:
            cur.execute("""SELECT * from t_report""")
        except:
            print 'cannot select'

        rows = cur.fetchall()
        for row in rows:
            msg = row[7]

        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
    #pulp     
    if event.message.text == "Rpt":
        msg = 'No Data'
        msg = sheet.cell(2,11).value  # Get the value of a specific cell
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
        msg = 'No Data'
        try:
            cur.execute("""SELECT * from t_report""")
        except:
            print 'cannot select'

        rows = cur.fetchall()
        for row in rows:
            msg = row[9]

        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))
        return 0
        '''
    ########################################## Dcs report User ask ################################################
    
    
    if event.message.text == "aa":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='your text is aa'))
        return 0

    if event.message.text == "bb":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
        return 0

    if event.message.text == "cc":
        #profile = line_bot_api.get_profile('C91f0e330efd3aebe03c34bfd2bd40cce')
        #profile = line_bot_api.get_profile('U5e90b6b6d543d8d96be449d8fcd3ddbe')
        #a = (profile.display_name)
        #b = (profile.group_id) #for group_id
        #c = (profile.picture_url)
        #d = (profile.status_message)
        line_bot_api.push_message('C22aaa682ea40676ee0f1d6fd120265b4', TextSendMessage(text='Hello MyJob'))
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=a))
        return 0
    
    if event.message.text == "dd":
        #profile = line_bot_api.get_profile('U5e90b6b6d543d8d96be449d8fcd3ddbe') #profile of sender => Thongpoon Auto 0684 (User)
        #a = (profile.display_name)
        #b = (profile.user_id) #for user_id
        #c = (profile.picture_url)
        #d = (profile.status_message)
        #line_bot_api.push_message(b, TextSendMessage(text='Hello Thongpoon!'))
        line_bot_api.push_message('Ub4c61cd90d77325b3cf97e4f9d881f26', TextSendMessage(text='Hello Thongpoon!'))
        return 0


    if event.message.text == "json":
        
        #Thongpoon
        json_line = request.get_json()
        json_line = json.dumps(json_line)
        decoded = json.loads(json_line)

        #user = user who send message to me
        #messageGet = message that user send to me
        #typeGet = type of data that user send to me
        user = decoded["events"][0]['replyToken']
        messageGet = decoded["events"][0]['message']['text']
        typeGet = decoded["events"][0]['message']['type']
        #Thongpoon
    
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=json_line))
        return 0








if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
