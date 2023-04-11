#!/usr/bin/env python
# coding: utf-8

# In[32]:


from tkinter import*
r = Tk()

r.title("STUDENT DETAILS")

r.geometry("800x500")

eid = Label(r,text="EMAIL ID").place(x=40,y=30)
pw = Label(r,text="PASSWORD").place(x=40,y=60)
stu_name = Label(r,text="NAME").place(x=40,y=90)
stu_id = Label(r,text="STUDENT ID NO:").place(x=40,y=120)
add = Label(r,text="ADDRESS").place(x=40,y=150)
fname = Label(r,text="FATHER NAME").place(x=40,y=180)
mname = Label(r,text="MOTHER NAME").place(x=40,y=210)
gname = Label(r,text="GUARDIAN NAME").place(x=40,y=240) 
sbttn = Button(r,text="SUBMIT AND EXIT",bd = '5', command = r.destroy).place(x=40,y=270)


eid_input = Entry(r,width =100).place(x=250,y=30)
pw_input = Entry(r,width =100).place(x=250,y=60)
stu_name_input = Entry(r,width =100).place(x=250,y=90)
stu_id_input = Entry(r,width =100).place(x=250,y=120)
add_input = Entry(r,width =100).place(x=250,y=150)
fname_input = Entry(r,width =100).place(x=250,y=180)
mname_input = Entry(r,width =100).place(x=250,y=210)
gname_input = Entry(r,width =100).place(x=250,y=240)


r.mainloop()

