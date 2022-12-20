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

