import os
import sys

from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser, WebhookHandler

load_dotenv();

channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

def getLineBotAPI():
    line_bot_api = LineBotApi(channel_access_token);
    return line_bot_api

def getWebhookHandler():
    handler = WebhookHandler(channel_secret);
    return handler

def getWebhookParser():
    parser = WebhookParser(channel_secret);
    return parser;