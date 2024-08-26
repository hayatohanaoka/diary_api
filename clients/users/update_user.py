import requests

from diary_api.clients.token_login_user import get_login_token

token = get_login_token('aa@bbb.ccc', '123456789')

res = requests.patch(
    'http://127.0.0.1:8000/api/v1/users/2/',
    data={
        'username': 'test_user',
        'nickname': 'test_nickname_',
        'email': 'aa@bbb.ccc',
    },
    headers={
        'Authorization': f'Token {token}'
    }
)

print(res.status_code)
print(res.content)
