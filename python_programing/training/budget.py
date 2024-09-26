import json

# データファイル名
file_name = 'budget_data.json'

# データの初期化
budget_data = {'収入': [], '支出': []}


# ファイルからデータを読み込む関数
def load_data():
    global budget_data
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            budget_data = json.load(file)
    except FileNotFoundError:
        print("データファイルが見つかりません。新しいファイルを作成します。")
    except json.JSONDecodeError:
        print("ファイルが破損しています。")


# ファイルにデータを書き込む関数
def save_data():
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(budget_data, file, ensure_ascii=False, indent=4)


# 収入の追加
def add_income(amount):
    budget_data['収入'].append(amount)
    save_data()
    print(f"収入 {amount} 円を追加しました。")


# 支出の追加
def add_expense(amount):
    budget_data['支出'].append(amount)
    save_data()
    print(f"支出 {amount} 円を追加しました。")


# 収支のバランスを計算
def calculate_balance():
    total_income = sum(budget_data['収入'])
    total_expense = sum(budget_data['支出'])
    balance = total_income - total_expense
    print(f"合計収入: {total_income} 円")
    print(f"合計支出: {total_expense} 円")
    print(f"現在の残高: {balance} 円")


# メインメニュー
def main():
    load_data()
    while True:
        print("\n--- 簡易予算管理メニュー ---")
        print("1. 収入を追加")
        print("2. 支出を追加")
        print("3. 収支を表示")
        print("4. 終了")

        choice = input("選択肢を入力してください (1-4): ")

        if choice == '1':
            amount = int(input("追加する収入額を入力してください: "))
            add_income(amount)
        elif choice == '2':
            amount = int(input("追加する支出額を入力してください: "))
            add_expense(amount)
        elif choice == '3':
            calculate_balance()
        elif choice == '4':
            print("終了します。")
            break
        else:
            print("無効な選択です。")


if __name__ == '__main__':
    main()
