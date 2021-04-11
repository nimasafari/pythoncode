

# r === read
# w === write
# a === append
# x === create file specified

######################################## Write to File
# f = open("google.txt", "w")
# f.write("this is a test")
# f.close()


######################################## Read to file

# f = open("google.html", "r")
# data = f.readlines() # or f.readline()

# print(data)
# f.close()

# while True:
#     data = f.readline()
#     if not data:
#         break
#     print(data)
    

######################################## Append File

# append_file = open("google.txt", "a")
# append_file.write("\nappended")
# append_file.close()

######################################## Delete File

# import os

# try:
#     os.renames("hello", "dadi")
# except:
#     pass

# try:
#     os.remove("google.txt")
# except:
#     pass

# print(os.curdir)

