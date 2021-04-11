import requests


# def write_2_file(google_msg):
#     f = open("google.html", "wb")
#     f.write(google_msg)
#     f.close()

# r = requests.get("https://google.com")
# if r.status_code == 200:
#     print("it's ok")
#     print("#" * 100)
#     write_2_file(r.content)
# else:
#     print("it's not ok")


############################################## Get List User


# import json


# myreq = requests.get("https://reqres.in/api/users?page=2")
# if myreq.status_code == 200:
#     print(myreq)
#     print(type(myreq))
#     myreq_decode = json.loads(myreq.text)
#     # print(myreq_decode)
#     print("*" * 100)
#     mylst = myreq_decode["data"]
#     for item in mylst:
#         print("#" * 100)
#         print(item["first_name"])


######################################### Check session with request userid

# login (user/pass) ====> web app Django ====> database check (user/pass) ====> session
#  request.session == infouser(3 ,username, email) ====> request (api/users/3) ====> 
#   if request.session["userid"] ==  request_id:
#       TODO
#   else:
#       retuen message(access forbedent)

######################################### Create user (Registeration)

# import time

# data = {
#     "name": "morpheus",
#     "job": "leader"
# }

# while True:
#     myreq = requests.post("https://reqres.in/api/users", data=data)
#     if myreq.status_code == 201:
#         print(myreq.content)
#     time.sleep(3)

#########################################

# https://www.digikala.com/recommendation/v1/ ====> EndPoint API === Action list product

## Rest API
'''
# Author name , Title

GET /rest/book/1

search table book
authorid ===> firstname


'''
## GraphQL
'''
// GET /graphql?query={ book(id: "1") { title, author { firstName } } }

{
  "title": "Black Hole Blues",
  "author": {
    "firstName": "Janna",
  }
}

'''


######################################### Update user (Registeration)
# import time
# import json

# data = {
#     'name': 'morpheus',
#     'job': 'zion resident'
# }

# # new_data = json.dumps(data)
# myreq = requests.put("https://reqres.in/api/users/3", data=data) # or patch
# if myreq.status_code == 200:
#     print(myreq.content)

######################################### Delete user

# myreq = requests.delete("https://reqres.in/api/users/2")
# if myreq.status_code == 204:
#     print(myreq.content)

######################################### Login user


# login = {
#     "email": "eve.holt@reqres.in",
#     "password": "cityslicka"
# }

# myreq = requests.post("https://reqres.in/api/login", data=login)
# if myreq.status_code == 200:
#     print(myreq.content)

