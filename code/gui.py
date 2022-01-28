from cgitb import text
from time import sleep
from tkinter import *
from tkinter import font
from tkinter.constants import LEFT
from tkinter import ttk
import mysql.connector as ms
#root 
window = Tk()
window.title("QRcode")
window.title("QRCode Based Attendance System")
window.iconbitmap(r'img\Sage_University_logo.ico')
window.geometry("600x600")

#background 
#background = PhotoImage(file= 'img/background.jpg')
background = 'light blue'


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
    #destroyed function
    def destroyed() :
        txt1.destroy()
        update.destroy()
        add.destroy()
        delete.destroy()
        show.destroy()
    
    #delete button 
    def delstudent() :
        destroyed()
        head = Label(main_frame, text= "DELETE RECORD",fg='RED',bg=background,font=('Comic sans ms', 22,'bold')).pack(padx=20, pady= 20)
        Label(main_frame,text='\t\t\t\t\tName                   : ',bg=background,font=(fnt,16)).pack(padx=5, pady= 15, anchor='w')
        name = Entry(main_frame,font=(fnt,16))
        name.place(x=700,y=190)
        Label(main_frame,text='\t\t\t\t\tStandard             : ',bg=background,font=(fnt,16)).pack(padx=5, pady= 15, anchor='w')
        std = Entry(main_frame,font=(fnt,16))
        std.place(x=700,y=250)
        Label(main_frame,text='\t\t\t\t\tRoll No                :  ',bg=background,font=(fnt,16)).pack(padx=5, pady= 15, anchor='w')
        rollno = Entry(main_frame,font=(fnt,16))
        rollno.place(x=700,y=310)
        Label(main_frame,text='\t\t\t\t\tFather Name     : ',bg=background,font=(fnt,16)).pack(padx=5, pady= 15, anchor='w')
        fname = Entry(main_frame,font=(fnt,16))
        fname.place(x=700,y=370)
        Label(main_frame,text='\t\t\t\t\tMother Name    : ',bg=background,font=(fnt,16)).pack(padx=5, pady= 15, anchor='w')
        mname = Entry(main_frame,font=(fnt,16))
        mname.place(x=700,y=430)
    
        #get Entries
        def close_window() :
            print(name.get())
            print(fname.get())
            print(mname.get())
            print(std.get())
            print(rollno.get())
            window.destroy()
        #submit button
        sub_button = Button(main_frame,text="SUBMIT",font=(fnt,12, 'bold'),height=1,width=10,bg='dark green', command= close_window)
        sub_button.pack(padx=10, pady= 40)

    
    #add details functions 
    def addstudent() :
        destroyed()
        head = Label(main_frame, text= "Fill The Details",fg='Black',bg=background,font=('Comic sans ms', 26,'bold'))
        head.pack(padx=20,pady=20)
        Label(main_frame,text='\t\t\t\t\tName                   : ',bg=background,font=(fnt,16)).pack( pady= 15, anchor='w')
        name = Entry(main_frame,font=(fnt,16))
        name.place(x=700,y=198)
        Label(main_frame,text='\t\t\t\t\tFather Name         : ',bg=background,font=(fnt,16)).pack( pady= 15,anchor='w')
        fname = Entry(main_frame,font=(fnt,16))
        fname.place(x=700,y=258)
        Label(main_frame,text='\t\t\t\t\tMother Name        : ',bg=background,font=(fnt,16)).pack( pady= 15, anchor= 'w')
        mname = Entry(main_frame,font=(fnt,16))
        mname.place(x=700,y=318)
        Label(main_frame,text='\t\t\t\t\tStandard                : ',bg=background,font=(fnt,16)).pack( pady= 15, anchor='w')
        std = Entry(main_frame,font=(fnt,16))
        std.place(x=700,y=378)
        Label(main_frame,text='\t\t\t\t\tAddress                 : ',bg=background,font=(fnt,16)).pack( pady= 15, anchor='w')
        addr = Entry(main_frame,font=(fnt,16))
        addr.place(x=700,y=438)
    
        #get entries
        def close_window() :
            print(name.get())
            print(fname.get())
            print(mname.get())
            print(std.get())
            print(addr.get())
            window.destroy()

        #submit button
        sub_button = Button(main_frame,text="SUBMIT",font=(fnt,12, 'bold'),height=1,width=10,bg='dark green', command= close_window)
        sub_button.pack(padx=20, pady= 20)
    
    #update details function
    def updatestudent() :
        destroyed()
        head = Label(main_frame, text="Update The Student Details", bg= background , font= ('Comic sans ms',22, 'bold')).pack(padx=20,pady=20)
        Label(main_frame, text="\t\t\t\t\tExisted Name  : ",font=(fnt, 16), bg= background).pack(padx=5,pady=15, anchor="w")
        Exist_name = Entry(main_frame,font=(fnt,16))
        Exist_name.place(x=700,y=190)
        Label(main_frame,text='\t\t\t\t\tStandard     : ',bg=background,font=(fnt,16)).pack(padx=5, pady= 15,anchor='w')
        std = Entry(main_frame, font=(fnt,16))
        std.place(x=700,y= 248)
        Label(main_frame, text="\t\t\t\t\tRoll Number    :", font=(fnt,16) , bg= background).pack(padx=5,pady=15, anchor='w')
        roll_no = Entry(main_frame,font=(fnt,16))
        roll_no.place(x=700,y=310)
    
        #getting values
        def close_window() :
            if Exist_name.get() != None or std.get() != None :
                print(Exist_name.get())
                Label(main_frame, text= "Record has been Updated", font=(fnt,16),bg= background).pack(padx=20,pady=20,anchor=CENTER)
                #window.destroy()
            else :
                window.destroy()
    
        #submit button 
        sub_button = Button(main_frame,text="SUBMIT",font=(fnt,12, 'bold'),height=1,width=10,bg='dark green', command= close_window)
        sub_button.pack(padx=10, pady= 40)
    
    #show details function
    def showdetails() :
        destroyed()
        head = Label(main_frame, text= "Details of student",fg='Green',bg=background,font=('Comic sans ms', 22,'bold')).pack(padx=20,pady=20)
        Label(main_frame,text='\t\t\t\t\tName                  : ',bg=background,font=(fnt,16)).pack(padx=5, pady= 15,anchor='w')
        name = Entry(main_frame ,font=(fnt,16))
        name.place(x=700,y=190)
        Label(main_frame,text='\t\t\t\t\tStandard     : ',bg=background,font=(fnt,16)).pack(padx=5, pady= 15,anchor='w')
        std = Entry(main_frame, font=(fnt,16))
        std.place(x=700,y= 250)
        Label(main_frame,text='\t\t\t\t\tEnrollment Number     : ',bg=background,font=(fnt,16)).pack(padx=5, pady= 15,anchor='w')
        rollno = Entry(main_frame,font=(fnt,16))
        rollno.place(x=700,y=310)
        #getting details
        def close_window() :
            print('Name : ',name.get())
            print('Standard :',std.get())
            print('Roll no : ',rollno.get())
            
            window.destroy()  
    
        #submit button 
        sub_button = Button(main_frame,text="SUBMIT",font=(fnt,12, 'bold'),fg='white',height=1,width=10,bg='dark green', command= close_window)
        sub_button.pack(padx=10, pady= 40)
    
    txt1 = Label(main_frame,text="Choose any Option.",font=(fnt,18, 'bold'),bg=background)
    txt1.pack(padx=20, pady= 20)
    #add student
    add = Button(main_frame,text = "add student",font=(fnt,15, 'bold',f_effect), width=20, height= 2,fg='black',bg='light gray',command=addstudent)
    #add.place(x = 680,y=100)
    add.pack(padx=20, pady=10)
    #show student details
    show = Button(main_frame,text = "show student details",font=(fnt,15, 'bold', f_effect), width=20 , height= 2,fg='black',bg='light gray',command=showdetails)
    show.pack(padx=20, pady= 20)
    #update student details
    update = Button(main_frame,text = "update student details",font=(fnt,15, 'bold', f_effect), width=20 , height=2,bg='light gray',fg='black',command=updatestudent)
    update.pack(padx=20, pady= 20)
    #delete student
    delete = Button(main_frame,text = "delete student", width= 20,font=(fnt,15, 'bold', f_effect) , height=2,bg='light gray',fg='black',command=delstudent)
    delete.pack(padx=20, pady= 20)

#User label destroy 
def user_pass_destroy() :
    userlabel.destroy()
    passlable.destroy()
    user_name.destroy()
    password.destroy()    
    submit.destroy()

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