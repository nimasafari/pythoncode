
# Boolean  = True / False

# f = True # false 
# b = True # true
# print(f and b)
# print(f or b)

# age = 20
# status = False
# if age == 20:
#     status = True
# # not status == False
# # status == True
# if status: 
#     print("your age is 20")
# else:
#     print("your age not 20")

################################################### If/Else

# a = 20
# b = 20
# print(a > b)
# if (a > b):
#     print("a > b")
# elif a <= b:
#     print("a <= b")
# elif a == b:
#     print(" a == b")
# else:
#     print("ELSE")
# if a > b:
#     print("a > b")
# else:
#     print(" a < b or a == b")
# print(bool("Hello"))
# print(bool(15))

################################################### Oprator
# 
# a = 10 
# b = 30 
# c = a + b
# print(c)
# d = a * b
# print(d)
# f = a / b
# print(f)
# f = a - b
# print(f)
# f = a ** b
# print(f)
# x = 5
# print(x)
# x += 5
# print(x)
# x -= 5
# print(x)
# x *= 5
# print(x)
# x /= 5
# print(x)
# x **= 5
# print(x)

################################################### List
# 
mylist = ["one", 1 , "two", "three", "five", "one"]

# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[3])
# print(list(set(mylist)))

# for item in mylist:
#     print(item)

# for i in range(len(mylist)):
#     print(mylist[i])

# mylist.append("123")
# print(mylist)

# mylist.pop()
# print(mylist)

# new_lst = mylist #.copy()
# new_lst.append(123123)
# print(mylist)
# print(new_lst)

# print(new_lst is mylist)
# for item in mylist:
#     print("one" in str(item))
# print("one" in str(mylist[1]))


# mylst2 = []
# mylst = list()
# mylst.append((1, 2, 3, 4)) ## add tuple
# # print(mylst)
# mylst.append({"one": 1}) ## dict
# print(mylst)
# mylst2.append("hello")
# mylst.append(mylst2)
# print(mylst)
# for item in mylst:
#     print(item)
#     if isinstance(item, dict):
#             print(item["one"])
#     for item2 in item:
#         print(item2)

# print(mylist)
# print(mylist[:-3])

# mylist = [2, 1, 4, 3]
# mylist.sort()
# print(mylist)

# mylist.sort(reverse=True)
# print(mylist)
# mylist.reverse()
# print(mylist)


# new_cpy_lst = mylist.copy() # new_cpy_lst = mylist
# print(new_cpy_lst)
# join_new_lst = new_cpy_lst + mylist # append
# print(join_new_lst)

# new_cpy_lst.extend(mylist)
# print(new_cpy_lst)

# mylist.clear()
# for i in range(len(mylist)):
#     mylist[i] = "six"
# print(mylist)

# print(mylist.count("five"))


################################################### Tuple
# [] == list 
# {key : value} == dict
# () == tuple

mytuple = ("one", "two", "three")
# print(mytuple)
# print(mytuple[0])
# print(mytuple[1])
# print(mytuple[2])

# for item in mytuple:
#     print(item)

# for i in range(len(mytuple)):
#     print(mytuple[i])

mytuple2 = ("one", "two", "three", "asas")

# print(mytuple is mytuple2)
# # for loop 
# print(mytuple[0] in "one")

# Casting Tuple to List ====> List to tuple
# lst_tuple = list(mytuple)
# lst_tuple.append("pppppp")
# print(tuple(lst_tuple))

# for i in range(len(mytuple)):
#     mytuple = list(mytuple)
#     mytuple[i] = "test"

# print(tuple(mytuple))
# lst_tuple = list(mytuple)
# lst_tuple.remove("one")
# print(tuple(lst_tuple))

# join_tuple = mytuple + mytuple2
# print(join_tuple)

# print(mytuple * 2)

# print(mytuple.index("two"))

################################################### Dict
# 
mydict_2 = dict()
mydict = {
    "firstname": "ramin",
    "lastname": "farajpour",
    "age": 27,
    "address" : "tehran",
    "country" : "iran"
}

# import json
# print(json.dumps(mydict))
# print(mydict)

# print(mydict["firstname"] + " " + mydict["lastname"])
# print(mydict["lastname"])
# print(mydict["age"])
# print(mydict["address"])
# print(mydict["country"])

# mylst = [1, 2,3,4]
# ddd = dict()
# ddd = {"mylst" : mylst}
# ddd.update(ddd)
# print(ddd)
# mytple = (1,2,3,4)
# mydict = {"mytuple" : mytuple}
# print(mydict)
# print(mydict["mytuple"])


# # print(dict_lst)

# mydict["firstname"] = "nima"
# print(mydict)
# a ,b = 10, 30

# for key, value in mydict.items():
#     print("%s : %s" % (key, value))  
#     print("{} : {}".format(key, value)) 

# print(len(mydict))

# mydict.update({"degree": "MS"})
# print(mydict)

# mydict.update({"degree": [1,2,3,4,5]})
# print(mydict)

# print(mydict.get("firstname")) # print(mydict["firstname"])

# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())

# print(mydict is mydict)
# print("ramin1" in mydict.get("firstname"))

# if "firstname" in mydict:
#     print("Yes. there is.")

# mydict.pop("firstname")
# print(mydict)
############################## Delete Dict
# del mydict["age"]
# print(mydict)
############################## Copy Dict
# new_dict = mydict.copy()
# print(new_dict)

# dict_to_dict = {

#     "one" : { 
#         "two" : {
#             "three": {
#                 "name" : "nima",
#                 "age" : 25
#             }
#         }
#     }

# }
# print(dict_to_dict)
# print(dict_to_dict.clear())

################################################### While loop

# while True:
    
    
#     print("OKOK")
#     # continue
#     break
#     # return

# i = 0
# while  i < 10:
    
#      print(i)
#      i += 1

################################################### for loop

# for i in range(40):
#     print(i)


################################################### Function

# def funcname(fname, lname):
#     print(fname)
#     print(lname)

# def funcname(*name):
#     print(name[2])

# def funcname(**name):
#     print(name["fname"])
#     print(name["lname"])
#     print(name["age"])

# def funcname(name = None):
#     print(name)


# if __name__ == "__main__":
#     # funcname("nima", "safari", "okokokokok")
#     # funcname(fname="nima", lname="safari", age=22)
#     funcname("okokok")


################################################### Lambda


# x = lambda a : a + 20
# print(x(10))

# x = lambda a : a * 20
# print(x(10))


# x = lambda a, b, c : a + b + c
# print(x(10, 10, 10))

# def myfunc():  
#     return lambda a : a * 20

# mm = myfunc()
# print(mm)