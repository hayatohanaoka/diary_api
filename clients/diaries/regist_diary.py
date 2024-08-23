import requests

res = requests.post(
    'http://127.0.0.1:8000/api/v1/diaries/write/', {
    'title': 'test_diary',
    'content': 'This is a test diary',
    'diary_date': '2024-08-11',
})
print(res.status_code)
print(res.content)
