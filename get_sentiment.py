# coding: utf-8
import sys
import os
import time
import random
import datetime
import telepot
import string
import re
import nltk
from emo_unicode import *
from langdetect import detect
from googletrans import Translator
from google.cloud import language_v1
from google.cloud.language_v1 import enums

def translate_message(text):
  translator = Translator()
  try:
    translation = translator.translate(text, src=detect(text))
  except:
    translation = translator.translate('')
  tranlated_msg = translation.text  
  return tranlated_msg

def convert_emoticons(text):
    for emot in EMOTICONS:
        text = re.sub(u'('+emot+')', "_".join(EMOTICONS[emot].replace(",","").split()), text)
    return text

def convert_emojis(text):
  for emot in UNICODE_EMO:
    try:
      text = re.sub(r'('+emot+')', "_".join(UNICODE_EMO[emot].replace(",","").replace(":","").split()), text)
    except Exception:
      pass
  return text

def clean_message(text):
  user_removed = re.sub(r'@[A-Za-z0-9]+','',text)
  link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
  number_removed = re.sub('\d+', '', link_removed)
  trans = translate_message(number_removed)
  emot_conv = convert_emoticons(trans)
  emoj_conv = convert_emojis(emot_conv)
  final = emoj_conv
  return emoj_conv

def analyze_sentiment(text_content):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'I am so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_sentiment(document, encoding_type=encoding_type)
    # Get overall sentiment of the input document
    score = u"SentiGinger score: {}".format(round(response.document_sentiment.score, 1))
    magnitude = u"SentiGinger magnitude: {}".format(round(response.document_sentiment.magnitude, 1))
    return score, magnitude

def handle(msg):
  chat_id = msg['chat']['id']
  text = msg['text']

  print('Got command: {}'.format(text))
  score, magnitude = analyze_sentiment(clean_message(text)) 
  bot.sendMessage(chat_id, str(score + ' ,' + magnitude))

bot = telepot.Bot('869154407:AAFcpQaMoNGHMWsDga4dK8eRAPKsm7CtTHM')
bot.message_loop(handle)
print('I am listening...')

while 1:
  time.sleep(10)
