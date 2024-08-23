import requests

from token_login_user import get_login_token

login_token_json = get_login_token('aav@bbb.ccc', '123456789')
token = login_token_json['token']

res = requests.patch(
    'http://127.0.0.1:8000/api/v1/users/1/',
    data={
        'username': 'test_user',
        'nickname': 'test_nickname',
        'email': 'a@bbb.ccc',
    },
    headers={
        'Authorization': f'Token {token}'
    }
)

print(res.status_code)
print(res.content)
