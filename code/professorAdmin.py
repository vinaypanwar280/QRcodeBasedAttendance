import mysql.connector as ms
from tkinter import *
from tkinter.constants import LEFT

mydb  = ms.connect(
    host="localhost",
    user = "root",
    passwd = "Realme_5",
    database = "minor_project_II"
    )

cur = mydb.cursor()

def showallstudents() :
    qur = "Select * from studentrecord"
    cur.execute(qur)
    
    for i in cur :
        print(i)
        
def showdetails() :
    name = input("Name of the student : ")
    rollno = input("Roll number of the student : ")
    standard = input("Standard  : ")
    #qur = "select * from studentrecord where roll_no ="+rollno+" and Name = "+name+" or standard = "+standard
    qur = "select * from studentrecord where Name = '"+name+"' and roll_no = "+rollno+" and standard = "+standard+";"
    
    try :
        cur.execute(qur)
    except :
        print("student Not exist.")
        mydb.rollback()
    for i in cur :
        print(i)
        
    mydb.commit()

def destudent() :
    name = input("Name of the student : ")
    roll = input(" Roll number : ")
    qur = "delete from studentrecord where roll_no = "+roll+" and Name = "+name+";"
    
    try :
        cur.execute(qur)
        print("details deleted.")
    
    except :
        print("invalid details")
        mydb.rollback()
    
    mydb.commit()

def addstudent() :
    name = input("Name of the student : ")
    fname = input("Father's name : ")
    Mname = input("Mother's name : ")
    std = int(input("class : "))
    addss = input("Adress :")
    
    qur = "INSERT into studentrecord(Name,Fathers_Name,Mothers_Name,standard,address,NoOfEnterance,NoOfExits,presents,totalNumberOfAttendance,totaldayson)\
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data =(name,fname,Mname,std,addss,0,0,0,0,0)
    
    try :
        cur.execute(qur,data)
        print("New student added.")
    
    except :
        print("Re-enter the details.")
        mydb.rollback()
    
    mydb.commit()
    



def gui() :
    #created a window tool 
    window = Tk()
    
    #adding Title
    window.title("QRCode Based Attendance System")
    window.iconbitmap(r'img\favicon.ico')


    txt = Label(window,text="QRcode Based Attendance System",font=('times new roman',25, 'bold'))
    txt.place(x = 560,y=0)

    txt1 = Label(window,text="Choose any Option.",font=('times new roman',18, 'bold'))
    txt1.place(x =710,y=40)
    #txt1.pack()
    #txt.insert("QRCode Based Attendance System")
    #add student
    add = Button(window,text = "add student",font=('times new roman',15, 'bold'), width=20, height= 2,fg='white',bg='navy blue',command='')
    add.place(x = 680,y=100)
    #show student details
    show = Button(window,text = "show student details",font=('times new roman',15, 'bold'), width=20 , height= 2,fg='white',bg='navy blue',command='')
    show.place(x = 680,y=200)
    #update student details
    update = Button(window,text = "update student details",font=('times new roman',15, 'bold'), width=20 , height=2,bg='navy blue',fg='white',command='')
    update.place(x = 680,y=300)
    #delete student
    delete = Button(window,text = "delete student", width= 20,font=('times new roman',15, 'bold') , height=2,bg='navy blue',fg='white',command='')
    delete.place(x = 680,y=400)

    #start window widget 
    window.mainloop()
    
def main() : 
   # gui()
    print("Choose option : \n1. Show all students detail\n2. Show Student details\n3. Add student\n4. delete student\n") 
    option = int(input())
    if option == 1 :
        showallstudents()
    if option == 2 :
        showdetails()
    
    if option == 3 :
        addstudent()
    
    if option == 4 :
         destudent() 

main()
