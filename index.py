from pypinyin import pinyin, Style

def hanzi_to_pinyin(text):
    string = pinyin(text, style=Style.TONE)
    return ' '.join([item[0] for item in string])

hanzi = input("Enter Hanzi: " )
pinyin = hanzi_to_pinyin(hanzi)

print(pinyin)