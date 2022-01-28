import mysql.connector as ms

mydb  = ms.connect(
    host="localhost",
    user = "root",
    passwd = "Realme_5",
    database = "minor_project_II"
    )

cur = mydb.cursor()

result = cur.execute("select * from studentrecord")

list = []
for i in cur :
    #print(i)
    list.append(i)
    
    
for i in list :
    for j in i :
        print(j)