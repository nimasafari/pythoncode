import re


# text = "this is a test."
# x = re.search("^this.*test*", text)
# # x = re.search("^this.*test$", text)
# print(x)

################################

# text = "this is a message"
# x = re.findall("message", text)
# if x:
#     print("founded")
# else:
#     print("not founded")

#################################

# text = "this is a message"
# x = re.search("\s", text)
# print(x.start())

#################################

# text = "this is a message123"
# x = re.split("\D", text)
# for i in x:
#     if i :
#         print(i)

# for item in text:
#     if item.isdigit():
#         print(item)

# x = text.split(" ")
# print(list(set(x))[1])

##################################

# text = "this is a message"
# x = re.sub("\s", "9", text)
# # x = text.replace(" ", "9")
# print(x)


###################################

# password = input("Enter string to test: ")
# if re.fullmatch(r'[A-Za-z0-9@#$%^&+=-]{3,}', password):
#     print(password)
# else:
#     print("password is invalid")

