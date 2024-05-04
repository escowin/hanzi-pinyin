from pypinyin import pinyin, Style

def hanzi_to_pinyin(text):
    string = pinyin(text, style=Style.TONE)
    return ' '.join([item[0] for item in string])

hanzi = "你好，世界！"
pinyin = hanzi_to_pinyin(hanzi)
print(pinyin)