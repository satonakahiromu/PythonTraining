# To Doリストアプリ（CLI版）

# タスクリストを格納するリスト
tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("現在、タスクはありません。")
    else:
        print("\nTo Doリスト:")
        for index, task in enumerate(tasks, 1):
            status = "完了" if task['completed'] else "未完了"
            print(f"{index}. {task['title']} [{status}]")

def add_task(title):
    tasks.append({"title": title, "completed": False})
    print(f"タスク '{title}' を追加しました。")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"タスク '{removed_task['title']}' を削除しました。")
    else:
        print("無効なインデックスです。")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        print(f"タスク '{tasks[index]['title']}' を完了しました。")
    else:
        print("無効なインデックスです。")

# メインループ
while True:
    print("\n--- To Do リストメニュー ---")
    print("1. タスクを表示")
    print("2. タスクを追加")
    print("3. タスクを削除")
    print("4. タスクを完了")
    print("5. 終了")

    choice = input("選択肢を入力してください (1-5): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        title = input("追加したいタスクを入力してください: ")
        add_task(title)
    elif choice == '3':
        show_tasks()
        index = int(input("削除したいタスクの番号を入力してください: ")) - 1
        delete_task(index)
    elif choice == '4':
        show_tasks()
        index = int(input("完了にしたいタスクの番号を入力してください: ")) - 1
        complete_task(index)
    elif choice == '5':
        print("終了します。")
        break
    else:
        print("無効な選択です。")
