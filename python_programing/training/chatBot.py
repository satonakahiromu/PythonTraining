# 簡易チャットボット

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "こんにちは" in user_input:
        return "こんにちは！どうしましたか？"
    elif "天気" in user_input:
        return "天気は晴れです。"
    elif "さようなら" in user_input:
        return "さようなら！またお話ししましょう。"
    else:
        return "すみません、よくわかりません。"


# メインループ
def main():
    print("チャットボットへようこそ！何か話しかけてください。")

    while True:
        user_input = input("あなた: ")

        if "さようなら" in user_input:
            print("ボット: " + chatbot_response(user_input))
            break
        else:
            print("ボット: " + chatbot_response(user_input))


if __name__ == '__main__':
    main()
