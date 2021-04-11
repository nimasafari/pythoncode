import pymysql



con = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='forclass',
)

try:

    ############ Select version database
    '''with con.cursor() as cur:
        cur.execute("select version();")
        version = cur.fetchone()
        print(version)
    '''
    ############ Insert to table user

    # with con.cursor() as cur:
    #     cur.execute("insert into users(username, email, firstname) values('nima', 'nima@gmail.com', 'nima safari')")
    #     con.commit()
    #     print("Insert was succefully")

    ############ Select One from table user
    # with con.cursor() as cur:
    #         cur.execute("select * from users where email='nima@gmail.com'")
    #         data = cur.fetchone()
    #         print(data)

    ############ Select All from table user
    # with con.cursor() as cur:
    #         cur.execute("select * from users")
    #         alldata = cur.fetchall()
    #         for item in alldata:
    #             if isinstance(item, tuple):
    #                 for mytuple in item:
    #                     print(mytuple)
    #                 print("#" * 100)
    #         # print(list(alldata))

    ############ Delete from users

    # with con.cursor() as cur:
    #         #  cur.execute("delete from users where username='nima'")
    #         cur.execute("UPDATE users SET firstname='nima' WHERE username='ramin'")
    #         con.commit()
    #         print("Updated")


    ############# Drop tables

    # with con.cursor() as cur:
    #         #  cur.execute("delete from users where username='nima'")
    #         cur.execute("drop from users;")
    #         con.commit()
    #         print("Updated")


except Exception as e:
    print(e)
