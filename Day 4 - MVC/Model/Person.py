

class Person():

    def __init__(self, fname, lname, address):
        self.firstname = fname
        self.lastname = lname
        self.address = address
    
    def retname(self):
        return self.firstname