import requests

res = requests.post('http://127.0.0.1:8000/api_token/', data={
    'email': 'aav@bbb.ccc',
    'password': '123456789'
})
print(res.status_code)
print(res.content)
