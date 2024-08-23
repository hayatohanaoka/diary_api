import requests

def get_login_token(email, password):
    res = requests.post('http://127.0.0.1:8000/api/v1/users/login/', data={
        'email': email,
        'password': password
    })
    return res.json()
