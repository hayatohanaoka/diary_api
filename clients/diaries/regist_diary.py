import requests

from diary_api.clients.token_login_user import get_login_token

login_token_json = get_login_token('aa@bbb.ccc', '123456789')
token = login_token_json['token']

res = requests.post(
    'http://127.0.0.1:8000/api/v1/diaries/',
    data={
        'title': 'test_diary',
        'content': 'This is a test diary',
        'diary_date': '2024-08-11',
    },
    headers={'Authorization': f'Token {token}'}
)
print(res.status_code)
print(res.content)
