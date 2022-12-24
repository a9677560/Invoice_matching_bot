try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from linebot.models import MessageEvent, TextMessage, TextSendMessage
from lineapi import getLineBotAPI
import requests

line_bot_api = getLineBotAPI()

def sendUse():
    text1 ='''歡迎使用發票對獎小幫手，請留意下列注意事項：
1. 「兌獎」功能會提示使用者輸入發票最後三碼，若最後三碼有中獎，就提示使用者輸入發票前五碼。
2. 「前期號碼」功能會顯示前兩期發票中獎號碼。
3. 「當期號碼」功能會顯示最近一期發票中獎號碼。
4.  本機器人可能在部分特例情況會產生BUG，若發生以上情形，請通知管理者。'''
    return text1

def showCurrent(event):
    try:
        content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
        tree = ET.fromstring(content.text)  #解析XML
        items = list(tree.iter(tag='item'))  #取得item標籤內容
        title = items[0][0].text  #期別
        pubDate = items[0][2].text  #開獎時間
        ptext = items[0][3].text  #中獎號碼
        ptext = ptext.replace('<p>','').replace('</p>','\n')
        message = title + '\n開獎時間：' + pubDate + '\n' + ptext[:-1]  #ptext[:-1]為移除最後一個\n
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發票號碼發生錯誤！'))

def showOld(event):
    try:
        content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
        tree = ET.fromstring(content.text)  #解析XML
        items = list(tree.iter(tag='item'))  #取得item標籤內容
        message = ''
        for i in range(1,3):
            title = items[i][0].text  #期別
            ptext = items[i][3].text  #中獎號碼
            ptext = ptext.replace('<p>','').replace('</p>','\n')
            message = message + title + '\n' + ptext + '\n'
        message = message[:-2]
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發票號碼發生錯誤！'))

def show3digit(event, mtext):
    try:
        content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
        tree = ET.fromstring(content.text)
        items = list(tree.iter(tag='item'))  #取得item標籤內容
        ptext = items[0][3].text  #中獎號碼
        ptext = ptext.replace('<p>','').replace('</p>','')
        temlist = ptext.split('：')
        prizelist = []  #特別獎或特獎後三碼
        prizelist.append(temlist[1][5:8])
        prizelist.append(temlist[2][5:8])
        prize6list1 = []  #頭獎後三碼六獎中獎號碼
        for i in range(3):
            prize6list1.append(temlist[3][9*i+5:9*i+8])
        if mtext in prizelist:
            message = '符合特別獎或特獎後三碼，請繼續輸入發票前五碼！'
            status = 1
        elif mtext in prize6list1:
            message = '恭喜！至少中六獎，請繼續輸入發票前五碼！'
            status = 2
        else:
            message = '很可惜，未中獎。請輸入下一張發票最後三碼，或輸入「退出」來退出兌獎功能。'
            status = 3
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發票號碼發生錯誤！'))
        status = -1
    return status

def show5digit(event, mtext, mode, digit3):
    try:
        content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
        tree = ET.fromstring(content.text)  #解析DOM
        items = list(tree.iter(tag='item'))  #取得item標籤內容
        ptext = items[0][3].text  #中獎號碼
        ptext = ptext.replace('<p>','').replace('</p>','')
        temlist = ptext.split('：')
        special1 = temlist[1][0:5]  #特別獎前五碼
        special2 = temlist[2][0:5]  #特獎前五碼
        prizehead = []  #頭獎
        for i in range(3):
            prizehead.append(temlist[3][9*i:9*i+8])
        sflag = False  #記錄是否中特別獎或特獎
        if mode=='special' and mtext==special1:
            message = '恭喜！此張發票中了特別獎！'
            sflag = True
        elif mode=='special' and mtext==special2:
            message = '恭喜！此張發票中了特獎！'
            sflag = True
        if mode=='special' and sflag==False:
            message = '很可惜，未中獎。請輸入下一張發票最後三碼。'
        elif mode=='head' and sflag==False:
            for i in range(3):
                if digit3 == prizehead[i][5:8]:
                    pnumber = prizehead[i]  #中獎的頭獎號碼
                    break
            if mtext == pnumber[:5]:
                message = '恭喜！此張發票中了頭獎！'
            elif mtext[1:5] == pnumber[1:5]:
                message = '恭喜！此張發票中了二獎！'
            elif mtext[2:5] == pnumber[2:5]:
                message = '恭喜！此張發票中了三獎！'
            elif mtext[3:5] == pnumber[3:5]:
                message = '恭喜！此張發票中了四獎！'
            elif mtext[4] == pnumber[4]:
                message = '恭喜！此張發票中了五獎！'
            else:
                message = '恭喜！此張發票中了六獎！'
        message = message + '\n請問是否要繼續兌獎？（輸入是或否）'            
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
        return True
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發票號碼發生錯誤！'))
        return False