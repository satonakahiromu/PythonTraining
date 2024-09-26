# 進化版電卓アプリ（メモリ機能付き）

memory = 0  # メモリの初期値


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."


def save_to_memory(result):
    global memory
    memory = result
    print(f"メモリに保存しました: {memory}")


def recall_memory():
    return memory


print("進化版電卓アプリ（メモリ機能付き）")
print("操作を選んでください:")
print("1. 足し算")
print("2. 引き算")
print("3. 掛け算")
print("4. 割り算")
print("5. メモリを呼び出す")
print("6. メモリに保存する")

choice = input("選択 (1/2/3/4/5/6): ")

if choice in ['1', '2', '3', '4']:
    num1 = float(input("1つ目の数値を入力してください: "))
    num2 = float(input("2つ目の数値を入力してください: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")

    # 結果をメモリに保存するか尋ねる
    save = input("結果をメモリに保存しますか？ (y/n): ")
    if save.lower() == 'y':
        save_to_memory(result)

elif choice == '5':
    print(f"メモリの内容: {recall_memory()}")

elif choice == '6':
    result = float(input("メモリに保存したい数値を入力してください: "))
    save_to_memory(result)

else:
    print("無効な選択です")