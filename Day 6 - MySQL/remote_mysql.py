import pymysql



con = pymysql.connect(
    host='sql6.freemysqlhosting.net',
    user='sql6403303',
    password='8CtrkcG3ml',
    database='sql6403303',
)

with con.cursor() as cur:
        cur.execute("select version();")
        version = cur.fetchone()
        print(version)