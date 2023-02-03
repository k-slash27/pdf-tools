import PySimpleGUI as sg
import simple

# デザインテーマの設定
sg.theme('DarkAmber')

# ウィンドウの部品とレイアウト
layout = [
    [sg.Text('ファイル', size=(10, 1)), sg.Input(), sg.FileBrowse('ファイルを選択', key='inputFilePath')],
    [sg.Button('キャンセル', key='cancel'), sg.Button('読み出し', key='proceed')],
    [sg.Output(size=(80,20), key='output')]
]

# ウィンドウの生成
window = sg.Window('ツール', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'cancel': #ウィンドウのXボタンを押したときの処理
        break

    if event == 'proceed': #「読み取り」ボタンが押されたときの処理
        filepath = values['inputFilePath']

        data = simple.execute(filepath)

        output = ''
        for k, v in data.items():
            output += ('%s: %s\n' % (k, v))

        window['output'].update(output)

window.close()