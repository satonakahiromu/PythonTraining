#パスワードランダム生成アプリ

import secrets
import string

def get_random_password_string(length):
    pass_chars = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(pass_chars)for x in range(length))
    return password

print(get_random_password_string(100))
print(get_random_password_string(15))
print(get_random_password_string(8))

