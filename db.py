import pymysql
con = pymysql.connect(host= 'localhost', user='andrey', password='1234', database='work')
def get_version():
    with con:
       cur = con.cursor()
       cur.execute("SELECT VERSION()")

    version = cur.fetchone()
    print("Версия БД:{}".format(version[0]))

with con:
   cur=con.cursor()
   cur.execute("SELECT * FROM users")

   rows= cur.fetchall()
   print("id name classname login password")
   for row in rows:
       print(" {0} {1} {2} {3} {4}".format(row[0],row[1],row[2],row[3],row[4]))
