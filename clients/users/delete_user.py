import requests

from diary_api.clients.token_login_user import get_login_token

token = get_login_token('aabb@bbb.ccc', '123456789')

res_1 = requests.delete(
    'http://127.0.0.1:8000/api/v1/users/1/',
    headers={'Authorization': f'Token {token}'}
)
print(res_1.status_code)
print(res_1.content)

res_2 = requests.delete(
    'http://127.0.0.1:8000/api/v1/users/3/',
    headers={'Authorization': f'Token {token}'}
)
print(res_2.status_code)
print(res_2.content)

