from cgitb import text
from itertools import count
from time import sleep
from tkinter import *
from tkinter import font
from tkinter.constants import LEFT
from tkinter import ttk
import mysql.connector as ms
from numpy import pad

#connecting to databases
mydb  = ms.connect(
    host="localhost",
    user = "root",
    passwd = "Realme_5",
    database = "minor_project_II"
    )

cur = mydb.cursor()

#root 
window = Tk()
window.title("QRcode")
window.title("QRCode Based Attendance System")
window.iconbitmap(r'img\Sage_University_logo.ico')
window.geometry("600x600")

#background 
#background = PhotoImage(file= 'img/background.jpg')
background = 'light cyan'

#size of back button
bsize = 6

#font selection 
fnt = 'rockwell'
f_effect = 'italic'

#main frame 
main_frame = Frame(window, bg= background)
main_frame.pack(fill=BOTH , expand= 1)


#created a lable 
label = Label(main_frame,bg = background)
label.place(x= 100,y=100)
#label = Label(window,bg = 'light blue')
#label.place()

#destroying each object

#m.wm_attributes('-transparentcolor','grey')
txt = Label(main_frame,text="QRcode Based Attendance System",font=(fnt,25, 'bold'),bg=background, fg='dark blue')
txt.pack(padx=10, pady= 20, anchor='center')
    
def main_window() :
    #destroyed show details
        
    #destroyed function
    def destroyed() :
        txt1.pack_forget()
        update.pack_forget()
        add.pack_forget()
        delete.pack_forget()
        show.pack_forget()
    
    #delete button 
    def delstudent() :
        destroyed()
        head = Label(main_frame, text= "DELETE RECORD",fg='RED',bg=background,font=('Comic sans ms', 22,'bold'))
        head.pack(padx=20, pady= 20)
        namel=Label(main_frame,text='\t\t\t\t\tName                   : ',bg=background,font=(fnt,16))
        namel.pack(padx=5, pady= 15, anchor='w')
        name = Entry(main_frame,font=(fnt,16))
        name.place(x=700,y=190)
        stdl=Label(main_frame,text='\t\t\t\t\tStandard             : ',bg=background,font=(fnt,16))
        stdl.pack(padx=5, pady= 15, anchor='w')
        std = Entry(main_frame,font=(fnt,16))
        std.place(x=700,y=250)
        rnml=Label(main_frame,text='\t\t\t\t\tRoll No                :  ',bg=background,font=(fnt,16))
        rnml.pack(padx=5, pady= 15, anchor='w')
        rollno = Entry(main_frame,font=(fnt,16))
        rollno.place(x=700,y=310)
        father_label=Label(main_frame,text='\t\t\t\t\tFather Name     : ',bg=background,font=(fnt,16))
        father_label.pack(padx=5, pady= 15, anchor='w')
        fname = Entry(main_frame,font=(fnt,16))
        fname.place(x=700,y=370)
        mother_label=Label(main_frame,text='\t\t\t\t\tMother Name    : ',bg=background,font=(fnt,16))
        mother_label.pack(padx=5, pady= 15, anchor='w')
        mname = Entry(main_frame,font=(fnt,16))
        mname.place(x=700,y=430)
    
        #get Entries
        def close_window() :
            #databaes connectivity
            qur = "delete from studentrecord where roll_no = "+rollno.get()+" and Name= "+name.get()+";"
            
            
            try :
                cur.execute(qur)
                Label(main_frame, text='Record deleted',font=(fnt, 16), fg='black', bg= background).pack(padx=5,pady=5)
            
            except :
                Label(main_frame, text='Fill again, couldn\'t be deleted',font=(fnt, 16), fg='black', bg= background).pack(padx=5,pady=5)
                mydb.rollback()
        #window.destroy()
        def destroys() :
            head.pack_forget()
            namel.pack_forget()
            name.place_forget()
            father_label.pack_forget()
            fname.place_forget()
            mother_label.pack_forget()
            mname.place_forget()
            stdl.pack_forget()
            std.place_forget()
            rnml.pack_forget()
            rollno.place_forget()
            sub_button.pack_forget()
            back.pack_forget()
            main_window()
        #back button
        back = Button(main_frame, text="Back", font=(fnt,10,f_effect),bg='light gray', width=bsize, command= destroys)
        back.pack(padx=150, pady=5,anchor='w')                
          
        #submit button
        sub_button = Button(main_frame,text="SUBMIT",font=(fnt,12, 'bold'),height=1,width=10,bg='dark green', command= close_window)
        sub_button.pack(padx=10, pady= 40)

    
    #add details functions 
    def addstudent() :
        destroyed()
        head = Label(main_frame, text= "Fill The Details",fg='Black',bg=background,font=('Comic sans ms', 26,'bold'))
        head.pack(padx=20,pady=20)
        namel =Label(main_frame,text='\t\t\t\t\tName                   : ',bg=background,font=(fnt,16))
        namel.pack( pady= 15, anchor='w')
        name = Entry(main_frame,font=(fnt,16))
        name.place(x=700,y=198)
        father_label=Label(main_frame,text='\t\t\t\t\tFather Name         : ',bg=background,font=(fnt,16))
        father_label.pack( pady= 15,anchor='w')
        fname = Entry(main_frame,font=(fnt,16))
        fname.place(x=700,y=258)
        mother_label=Label(main_frame,text='\t\t\t\t\tMother Name        : ',bg=background,font=(fnt,16))
        mother_label.pack( pady= 15, anchor= 'w')
        mname = Entry(main_frame,font=(fnt,16))
        mname.place(x=700,y=318)
        stdl =Label(main_frame,text='\t\t\t\t\tStandard                : ',bg=background,font=(fnt,16))
        stdl.pack( pady= 15, anchor='w')
        std = Entry(main_frame,font=(fnt,16))
        std.place(x=700,y=378)
        addr_label=Label(main_frame,text='\t\t\t\t\tAddress                 : ',bg=background,font=(fnt,16))
        addr_label.pack( pady= 15, anchor='w')
        addr = Entry(main_frame,font=(fnt,16))
        addr.place(x=700,y=438)
    
        #get entries
        def close_window() :

            #data that is to feed the data base
            qur = "INSERT into studentrecord(Name,Fathers_Name,Mothers_Name,standard,address,NoOfEnterance,NoOfExits,presents,totalNumberOfAttendance,totaldayson)\
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            data = (name.get(),fname.get(),mname.get(),std.get(),addr.get(),0,0,0,0,0)
            
            #executing the query
            try :
                cur.execute(qur,data)
                mydb.commit()
                Label(main_frame, text='Student added to the record',font=(fnt, 16), fg='black', bg= background).pack(padx=5,pady=5)
            
            except :
                Label(main_frame,text='Enter accurate details',font=(fnt,14), fg='black', bg=background).pack(padx=5,pady=5)
            
        #window.destroy()
        def destroys() :
            head.pack_forget()
            namel.pack_forget()
            name.place_forget()
            father_label.pack_forget()
            fname.place_forget()
            mother_label.pack_forget()
            mname.place_forget()
            stdl.pack_forget()
            std.place_forget()
            addr_label.pack_forget()
            addr.place_forget()
            sub_button.pack_forget()
            back.pack_forget()
            main_window()
        #back button
        back = Button(main_frame, text="Back", font=(fnt,10,f_effect),bg='light gray', width=bsize, command= destroys)
        back.pack(padx=150, pady=5,anchor='w')
        #submit button
        sub_button = Button(main_frame,text="SUBMIT",font=(fnt,12, 'bold'),height=1,width=10,bg='dark green', command= close_window)
        sub_button.pack(padx=20, pady= 20)
        #end of the function
        
    #update details function
    def updatestudent() :
        destroyed()
        head = Label(main_frame, text="Update The Student Details", bg= background , font= ('Comic sans ms',22, 'bold'))
        head.pack(padx=20,pady=20)
        namel =Label(main_frame, text="\t\t\t\t\tExisted Name  : ",font=(fnt, 16), bg= background)
        namel.pack(padx=5,pady=15, anchor="w")
        Exist_name = Entry(main_frame,font=(fnt,16))
        Exist_name.place(x=700,y=190)
        stdl =Label(main_frame,text='\t\t\t\t\tStandard     : ',bg=background,font=(fnt,16))
        stdl.pack(padx=5, pady= 15,anchor='w')
        std = Entry(main_frame, font=(fnt,16))
        std.place(x=700,y= 248)
        rnml = Label(main_frame, text="\t\t\t\t\tRoll Number    :", font=(fnt,16) , bg= background)
        rnml.pack(padx=5,pady=15, anchor='w')
        rollno = Entry(main_frame,font=(fnt,16))
        rollno.place(x=700,y=310)
    
        #getting values
        def close_window() :
            if Exist_name.get() != None or std.get() != None :
                print(Exist_name.get())
                Label(main_frame, text= "Record has been Updated", font=(fnt,17),bg= background).pack(padx=20,pady=20,anchor=CENTER)
                #window.destroy()
            else :
                window.destroy()
        #forgate function for forgating elements
        def destroys() :
            head.pack_forget()
            namel.pack_forget()
            Exist_name.place_forget()
            stdl.pack_forget()
            std.place_forget()
            rnml.pack_forget()
            rollno.place_forget()
            sub_button.pack_forget()
            back.pack_forget()
            main_window()
        
        #back button
        back = Button(main_frame, text="Back", font=(fnt,10,f_effect),bg='light gray', width=bsize, command= destroys)
        back.pack(padx=150, pady=5,anchor='w')
        #submit button 
        sub_button = Button(main_frame,text="SUBMIT",font=(fnt,12, 'bold'),height=1,width=10,bg='dark green', command= close_window)
        sub_button.pack(padx=10, pady= 40)
        #end of the function       
    
    #show details function
    def showdetails() :
        destroyed()
        
        head = Label(main_frame, text= "Details of student",fg='Green',bg=background,font=('Comic sans ms', 22,'bold'))
        head.pack(padx=20,pady=20)
        namel =Label(main_frame,text='\t\t\t\t\tName                  : ',bg=background,font=(fnt,16))
        namel.pack(padx=5, pady= 15,anchor='w')
        name = Entry(main_frame ,font=(fnt,16))
        name.place(x=700,y=190)
        stdl=Label(main_frame,text='\t\t\t\t\tStandard     : ',bg=background,font=(fnt,16))
        stdl.pack(padx=5, pady= 15,anchor='w')
        std = Entry(main_frame, font=(fnt,16))
        std.place(x=700,y= 250)
        rnml = Label(main_frame,text='\t\t\t\t\tEnrollment Number     : ',bg=background,font=(fnt,16))
        rnml.pack(padx=5, pady= 15,anchor='w')
        rollno = Entry(main_frame,font=(fnt,16))
        rollno.place(x=700,y=310)
        #getting details
        def close_window() :
            #query to execute
            qur = "select * from studentrecord where Name = '"+name.get()+"' and roll_no = "+rollno.get()+" and standard = "+std.get()+";"
            
            try :
                global cont
                cont = 0
                cur.execute(qur)
                for i in cur :
                   cont+=1
                   global lable1
                   lable1= Label(main_frame,text = i, font=(fnt , 16), fg= 'black' , bg= background)
                   lable1.pack(padx=5,pady=5)
            
            except :
                global lable2
                lable2=Label(main_frame,text = 'Student not exist', font=(fnt , 16), fg= 'black' ,bg= background)
                lable2.pack(padx=5,pady=5, anchor='center')
            #end of the function    
        #window destroy function 
        def destroys() :
            head.pack_forget()
            namel.pack_forget()
            name.place_forget()
            stdl.pack_forget()
            std.place_forget()
            rnml.pack_forget()
            rollno.place_forget()
            sub_button.pack_forget()
            #lable1.pack_forget()
            #lable2.pack_forget()
            back.pack_forget()
            main_window()
        
        #back button
        back = Button(main_frame, text="Back", font=(fnt,10,f_effect),bg='light gray', width=bsize, command= destroys)
        back.pack(padx=150, pady=5,anchor='w')
        #submit button 
        sub_button = Button(main_frame,text="SUBMIT",font=(fnt,12, 'bold'),fg='white',height=1,width=10,bg='dark green', command= close_window)
        sub_button.pack(padx=10, pady= 40)
        #end of the fucntion
    
    #main text      
    txt1 = Label(main_frame,text="Choose any Option.",font=(fnt,18, 'bold'),bg=background)
    txt1.pack(padx=20, pady= 20)
    #add student
    add = Button(main_frame,text = "add student",font=(fnt,15, 'bold',f_effect), width=20, height= 2,fg='black',bg='light green',command=addstudent)
    #add.place(x = 680,y=100)
    add.pack(padx=20, pady=10)
    #show student details
    show = Button(main_frame,text = "show student details",font=(fnt,15, 'bold', f_effect), width=20 , height= 2,fg='black',bg='light green',command=showdetails)
    show.pack(padx=20, pady= 20)
    #update student details
    update = Button(main_frame,text = "update student details",font=(fnt,15, 'bold', f_effect), width=20 , height=2,bg='light green',fg='black',command=updatestudent)
    update.pack(padx=20, pady= 20)
    #delete student
    delete = Button(main_frame,text = "delete student", width= 20,font=(fnt,15, 'bold', f_effect) , height=2,bg='light green',fg='black',command=delstudent)
    delete.pack(padx=20, pady= 20)

#User label destroy 
def user_pass_destroy() :
    userlabel.pack_forget()
    passlable.pack_forget()
    user_name.pack_forget()
    password.pack_forget()
    submit.pack_forget()

#get details
def get_details() :
    print(user_name.get())
    print(password.get())
    user_pass_destroy()
    main_window()



#username details
userlabel=Label(main_frame,text='Username  ',bg=background,font=(fnt,16))
userlabel.pack(padx=5, pady= 15,anchor='center')
user_name = Entry(main_frame, font=(fnt, 12), width= 30)
user_name.pack(padx=5, pady= 10,anchor='center')
passlable=Label(main_frame,text='Password  ',bg=background,font=(fnt,16))
passlable.pack(padx=5, pady= 15,anchor='center')
password = Entry(main_frame, font=(fnt, 12), width= 30)
password.pack(padx=5, pady= 10,anchor='center')

    
submit = Button(main_frame,text= 'Submit', font=(fnt, 12,'bold', f_effect),height=1,width=10, fg= 'white', bg= 'dark green',command= get_details)
submit.pack(padx=20,pady=20)
#start window widget 
window.mainloop()
