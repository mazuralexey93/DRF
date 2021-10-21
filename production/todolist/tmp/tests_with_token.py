import requests

user_data = {'username': 'django',
             'password': 'geekbrains'}

response = requests.post(
    'http://localhost:8000/api/token/',
    data=user_data)
print(response.status_code)
print(response.json())

# {'token': '6da4f6ea5d8f917930cab8b55020ce93b37104de'}
# {'refresh':
# 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMjIzNjU5NCwianRpIjoiMDRiOWY5ZmE1MGI0NDdhYWE4Y2RhMmEyNjg1ZDIyYmMiLCJ1c2VyX2lkIjoxfQ.EznhceCNDeKntiPuVTolhYvzUBF3iUs0whrcUMJCxAU',
# 'access':
# 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMTUwNDk0LCJqdGkiOiJhODNlZGE5ZGEwY2Q0ZjA1OTk2YmRhZDZmMGJjNDFmMiIsInVzZXJfaWQiOjF9.18V1-LDHoZRbks7REdbFVDYykiII6IOGUJqiQFwV8pM'
# }
