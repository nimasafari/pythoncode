
from Model.Person import Person
from Database.QueryDB import *
from View.IndexView import showinsertmessage

if __name__ == "__main__":
    
    # Model (Person : name, lnam , age , address , nationalcode, ...)
    obj_person = Person("nima", "safari", "tehran")
    # print(obj_person.retname())
    
    # Add database : insert 
    obj_database = Connection()
    retconn = obj_database.connecting_to_database()
    # Create Table
    # obj_database.createtable_company()

    obj_mysqlauery = MySQLQuerys(retconn)
    obj_mysqlauery.insert()
    # show : selectall:  "select * from Person"
    # show : selectone: "select * from Person where userid=123
    # delete : delete : "delete from Person where userid=123"
    # update : "update Person set value("", "", "")"
    print(showinsertmessage())



    