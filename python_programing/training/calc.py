# シンプルな電卓アプリ

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

print("シンプルな電卓アプリ")
print("操作を選んでください:")
print("1. 足し算")
print("2. 引き算")
print("3. 掛け算")
print("4. 割り算")

choice = input("選択 (1/2/3/4): ")

num1 = float(input("1つ目の数値を入力してください: "))
num2 = float(input("2つ目の数値を入力してください: "))

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("無効な選択です")
