import requests

# OpenWeather API
API_KEY = '7c43f7741a782c808a2666d5d1d27b4b'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# 地域名ユーザー入力
city = input("天気を確認したい都市名を入力してください: ")

# 完全なURLを作成
url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric&lang=ja"

# APIリクエストを送信
response = requests.get(url)

# レスポンスを確認
if response.status_code == 200:
    data = response.json()
    main = data['main']
    weather = data['weather'][0]

    # 取得したデータを表示
    print(f"都市: {data['name']}")
    print(f"天気: {weather['description']}")
    print(f"温度: {main['temp']}°C")
    print(f"湿度: {main['humidity']}%")
else:
    print("天気情報を取得できませんでした。都市名が正しいか確認してください。")
