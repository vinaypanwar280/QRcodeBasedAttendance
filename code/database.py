import mysql.connector as ms

mydb  = ms.connect(
    host="localhost",
    user = "root",
    passwd = "Realme_5",
    database = "minor_project_II"
    )

cur = mydb.cursor()
"""
try :
    relation =  cur.execute("select roll_no, Name from studentrecord")

except :
    mydb.rollback()

for i in cur :
    print(i)


#print(mydb)
"""
def entry(Enscan, rollno) :
    if Enscan  == True :
        qur = "update studentrecord set NoOfEnterance= 1 where roll_no = "+str(rollno)
        
    else:
        qur = "update studentrecord set NoOfEnterance= 0 where roll_no = "+str(rollno)
    
    cur.execute(qur)
    mydb.commit() 
    
def exits(Exscan,rollno) :
    if Exscan == True :
        qur =  "update studentrecord set NoOfExits= 1 where roll_no = "+str(rollno)
    else :
        qur =  "update studentrecord set NoOfExits= 0 where roll_no = "+str(rollno)
    cur.execute(qur)
    mydb.commit() 


entry(True,1)
entry(True,3)
entry(True,10)
entry(True,4)
entry(True,6)

print("Name of the student who entried in the lectures")
cur.execute("select roll_no, Name from studentrecord where NoOfEnterance = 1")
for i in cur :
    print(i)

exits(True,1)
exits(True,3)
exits(True,10)
exits(False,4)
exits(True,6)

print("Name of the student who exited from the lectures")
cur.execute("select roll_no, Name from studentrecord where NoOfExits = 1")
for i in cur :
    print(i)

cur.execute("update studentrecord set presents = 1 where NoOfEnterance= 1 and NoOfExits = 1")
mydb.commit()   

print("Name of the student who was present in all of the lectures")
cur.execute("select roll_no,Name,presents from studentrecord where presents = 1")
for i in cur :
    print(i)

mydb.commit() 

cur.execute("describe studentrecord")
for i in cur :
    print(i)
mydb.close()