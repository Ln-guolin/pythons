#!/usr/bin/env python
#!coding=utf-8
#author=guolin
import sys
reload(sys)
import emoji
import re

emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)

# 移除表情
def remove_emoji(text):
    return emoji_pattern.sub(r'', text)

# 转换表情为文字
def parse_to_text(text):
    return emoji.demojize(text)

# 文字转表情
def parse_to_emoji(emoji_text):
    return emoji.emojize(emoji_text)

if __name__=="__main__":

    str_emoji = u"哈哈😊哈😊"

    print u"移除表情："+remove_emoji(str_emoji)

    print u"转换表情："+parse_to_text(str_emoji)

    print u"还原表情："+emoji.emojize(parse_to_text(str_emoji))







