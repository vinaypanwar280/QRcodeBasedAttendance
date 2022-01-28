import qrcode as qr

StudentName = { 1 : 'Aayushi jariwala' , 2 : 'Bipasha Rao' , 3 : 'Chetali joshi' , 4 : 'Deepa thakur' , 5 :'Esha Rathore' , 
               6 : 'fana khan' , 7 : 'Geeta panwar' , 8 : 'himani ahirwal' , 9 : 'Vanshika jain' , 10 : 'vaishanavi Kausal',
               11 : 'Vikas Dhakad'} 

#print(StudentName[1])
student_qr = []
 

student = qr.make(input("enter name : "))
student.save("test.png")
