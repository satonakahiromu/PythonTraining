# カウントダウンタイマー

import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = f'{mins:02d}:{secs:02d}'
        print(time_format, end='\r')  # '\r' で行を上書き
        time.sleep(1)
        seconds -= 1
    print("時間です！")

# メイン処理
try:
    seconds = int(input("カウントダウンの秒数を入力してください: "))
    countdown_timer(seconds)
except ValueError:
    print("正しい数値を入力してください。")
