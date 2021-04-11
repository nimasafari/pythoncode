# x = 10
# y = 10
# z = "salam"

# print(x)
# print("\n")
# print(y)
# print("\n")
# print(z)

################################################

# f = ''' Hello My friends'''
# print(f)

# print(type(x))
# print(type(y))
# print(type(str(x)))
# new_str = str(x)
# print(type(new_str))

################################################

# x = "test"
# y = 'test'
# z = "Test"

# if x == z:
#     print("Match")
# else:
#     print("not match")

################################################

# x , y , z = "test1", "test2", "test3"
# x = y

# print(x)
# print(y)
# print(z)

################################################

# x = y = z = "test"

# print(x)
# print(y)
# print(z)

################################################

# x = "test"
# y = "test"

# z = x + y # str + str = True
# g = str(1) + y # int + str = False, str(int) + str = True

# a = 10
# b = 20
# print(a + b)
# print(a * b)
# h = a - b
# print(h)
# print(str(h))
# print(abs(h))

# print(g)
# print(z)

################################################

# Data Types : 
    # Text Type : str, 
    # Numric Type : int, float, complex
    # Sequence Type : list, tuple, range
    # mapping type : dict
    # Set type : set, frozenset
    # Boolean Type : False, True
    # Binary Type : bytes, bytearray, memoryview

# x = 10 
# print(type(x))

# x = 1j
# print(type(x))

# x = 20.01
# print(type(x))

# x = "abc"
# print(type(x))

# x = ["a", "b", "c"]
# print(type(x))

# x = {"key": "value"}
# print(type(x))

# x = (1 , "one", "two")
# print(type(x))

# x = range(6)
# print(type(x))

# x = True
# print(type(x))

# x = b"abc"
# print(type(x))

# x = bytearray(5)
# print(type(x))

# x = memoryview((bytes(5)))
# print(type(x))
# print(x)

# x = frozenset({"key": "value"})
# print(type(x))

################################################
# Integer

# import random

# myrand = random.randrange(1, 1000)
# print(myrand)


################################################
# Casting 
# x = int(1)
# y = int(2.5)
# z = int("23123123123")
# print(x)
# print(y)
# print(z)


# x = float(1)
# y = float(2.8)
# z = float("3")
# d = float("4.3")
# print(x)
# print(y)
# print(z)
# print(d)

# x = str("s1")
# y = str(2)
# z = str(3.0)
# print(x)
# print(y)
# print(z)

################################################
# Array String 

# "r[0] a[1] m[2] i[3] n[4]" 
# name = "ali"
# print(name)
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])

# for varianlename in string/list/tuple:
# for item in name:
#     print(item)
#     # break
#     continue

# print(len(name))

## Check String
# message = "this is my name is ramin"
# if name in message:
#     print("match ...")

## Check is not in
# txt = "my name is ali"
# if name not in txt:
#     print("is not match")

################################################
# Slicing
       #"01234"
# name = "ramin"
# print(name[0:2])
# print(name[2:4])
# print(name[4:])

# start slicing
# print(name[:3])

# end slicing
# print(name[2:])

# negtive slicing
# print(name[:-4])

################################################
# Upper Case

# a = "Hello, World "
# print(a.upper())
# print(a.lower())
# print(a.strip())
# print(a.split(","))
# print(a.rsplit(" "))
# print(a.replace("Hello", "Goodbye"))

################################################
# Concatination

# a = "hello"
# b = "world"
# c = a  + " " + b
# print(c)

################################################
# Format String
# age = 20
# message = "Hi, my name is ali, i'm old is " + str(age)
# print(message)
 

# message = "Hi, my name is ali, i'm old is {}"
# final_message = message.format(age)
# print(final_message)

# message = "Hi, my {} is ali, i'm old is {}"
# print(message.format("hello", age))


# message = "Hi, my {0} is ali, i'm old is {1}"
# print(message.format(age, "hello"))

################################################
