import requests

res = requests.post('http://127.0.0.1:8000/api/v1/users/', {
    'username': 'test_user',
    'nickname': 'test_nickname',
    'email': 'aabb@bbb.ccc',
    'password': '123456789'
})
print(res.status_code)
print(res.content)
