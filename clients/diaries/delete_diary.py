import requests

from diary_api.clients.token_login_user import get_login_token

token = get_login_token('aa@bbb.ccc', '123456789')

res = requests.delete(
    'http://127.0.0.1:8000/api/v1/diaries/74366808d30242798dc1436c518aad06/details/',
    headers={
        'Authorization': f'Token {token}'
    }
)

print(res.headers)
print(res.status_code)
print(res.content)
