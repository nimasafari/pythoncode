import urllib3


# http = urllib3.PoolManager()
# r = http.request('GET', 'https://reqres.in/api/users?page=2')
# print(type(r.data))
# mystr = r.data.decode()
# print(type(mystr))
# print(mystr)

########################################### Register 
import json


data = {
    'email': 'eve.holt@reqres.in',
    'password': 'pistol'
}

data = json.dumps(data).encode('utf-8')

http = urllib3.PoolManager()
r = http.request('POST', 'https://reqres.in/api/register', body=data, headers={'Content-Type': 'application/json' })
print(r.data)
