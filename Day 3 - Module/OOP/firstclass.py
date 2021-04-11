

# class MyClass():
#     x = 5

# obj = MyClass()
# print(obj.x) 

###########################################

# class Person:

#     def __init__(self, name, lname, age):
#         self.Name = name
#         self.LastName = lname
#         self.Age = age

#     def NamePrint(self):
#         print(self.Name)
        
#     def LastNamePrint(self):
#         print(self.LastName)
    
#     def AgePrint(self, myage):
#         self.Age = myage
#         del self.Age
#         # print(myage)
#         # print(self.Age)

# obj = Person("Nima", "Safari", 22)
# obj.AgePrint(30)
# obj.LastNamePrint()
# obj.NamePrint()
# print(obj.Age)


# class Student():
#     pass


# print(obj.name)
# print(obj.lname)

########################################### __init__ #####

# class Person():

#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
    
#     def printnames(self):
#         print(self.firstname, self.lastname)

# class Student(Person):

#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)

# x = Student("Nima", "Safari")
# x.printnames()

# objperson = Person("Nima", "Safari")
# objperson.printnames()

########################################### Supper #####

class Person():

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printnames(self):
        print(self.firstname, self.lastname)

    def ageprint(self):
        print(self.age)

class Student(Person):

    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.firstname = "Ramin"
        self.age = 22
        # Person.__init__(self, fname, lname)

    def welcomemessage(self):
        print(self.firstname, self.lastname)


x = Student("Nima", "Safari")
x.printnames()
x.ageprint()
x.welcomemessage()