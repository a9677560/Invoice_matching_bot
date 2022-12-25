import os

from dotenv import load_dotenv
from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, ImageSendMessage, CarouselTemplate, CarouselColumn

load_dotenv();
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(channel_access_token)

def send_text_message(reply_token, text):
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def push_message(userid, msg):
    line_bot_api.push_message(userid, TextSendMessage(text=msg))
    return "OK"

def send_image_url(id, img_url):
    message = ImageSendMessage(
        original_content_url=img_url,
        preview_image_url=img_url
    )
    line_bot_api.reply_message(id, message)

    return "OK"

def send_button_message(id, img, title, uptext, labels, texts):
    acts = []
    for i, lab in enumerate(labels):
        acts.append(
            MessageTemplateAction(
                label=lab,
                text=texts[i]
            )
        )

    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url=img,
            title=title,
            text=uptext,
            actions=acts
        )
    )
    line_bot_api.push_message(id, message)
    return "OK"

def send_button_carousel(id):
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/W6DA2KG.jpg',
                    title='功能列表',
                    text='你想要做什麼呢？',
                    actions=[
                        MessageTemplateAction(
                            label='查看當期號碼',
                            text='當期號碼'
                        ),
                        MessageTemplateAction(
                            label='查看前期號碼',
                            text='前期號碼'
                        ),
                        MessageTemplateAction(
                            label='兌獎',
                            text='兌獎'
                        )
                    ]
                ),
            ]
        )
    )
    line_bot_api.push_message(id, message)

    return "OK"

def send_button_message(id, uptext, labels, texts):

    acts = []
    for i, lab in enumerate(labels):
        acts.append(
            MessageTemplateAction(
                label=lab,
                text=texts[i]
            )
        )

    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            #thumbnail_image_url=img,
            #title=title,
            text=uptext,
            actions=acts
        )
    )
    line_bot_api.push_message(id, message)
    return "OK"