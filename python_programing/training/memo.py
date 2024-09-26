# 日本語対応のメモ帳アプリ

# メモを保存するファイル名
memo_file = "memo.txt"

# メモを表示する関数
def show_memos():
    try:
        with open(memo_file, 'r', encoding='utf-8') as file:
            content = file.read().strip()  # 内容を読み込み、空白を削除
            if content:
                print("\n--- 保存されているメモ ---")
                print(content)
            else:
                print("メモがありません。")
    except FileNotFoundError:
        print("メモファイルが見つかりません。")

# メモを追加する関数
def add_memo():
    memo = input("追加したいメモを入力してください: ").strip()  # 入力値の前後の空白を削除
    if memo:  # 空の入力を防止
        with open(memo_file, 'a', encoding='utf-8') as file:  # 'a'モードは追記モード
            file.write(memo + "\n")
        print(f"メモ '{memo}' を保存しました。")
    else:
        print("メモが空です。再度入力してください。")

# メモを削除する関数（ファイル内容を空にする）
def delete_memos():
    with open(memo_file, 'w', encoding='utf-8') as file:  # 'w'モードでファイルを空にする
        pass
    print("メモを全て削除しました。")

# メインループ
while True:
    print("\n--- メモ帳メニュー ---")
    print("1. メモを見る")
    print("2. メモを追加する")
    print("3. メモを削除する")
    print("4. 終了")

    choice = input("選択肢を入力してください (1-4): ")

    if choice == '1':
        show_memos()
    elif choice == '2':
        add_memo()
    elif choice == '3':
        delete_memos()
    elif choice == '4':
        print("終了します。")
        break
    else:
        print("無効な選択です。")
