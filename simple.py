from pdfminer.high_level import extract_text
import sys
import re
import regex

def execute(filepath):
    FILE_PATH = filepath

    text = extract_text(FILE_PATH)
    # print(text)

    lines = text.split('\n')

    arr = []

    for line in lines:
        line = re.sub(r"\s+", "", line)
        code_regex = re.compile('[━┨┏┬┓┠─┗┷┛┼┃]+')
        line = code_regex.sub('', line)
        line = line.replace('所有者一覧表（建物）', '')

        search = regex.match('(\p{Script=Hiragana}|\p{Script=Katakana}|\p{Script=Han})', line)
        index = regex.match('(所有者|(住所│氏名))', line)

        if (search is not None) and (index is None):
            arr.append(line)

    name_address = arr[-1].split('│')

    response = {'号室': arr[0].split('－')[-1], '氏名': name_address[1], '住所': name_address[0]}

    return response