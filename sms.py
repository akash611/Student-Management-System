from tkinter import *
from tkinter import ttk
import pymysql
from pymysql import cursors
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        
        title=Label(self.root, text="Student Management System", bd=10,relief= GROOVE, font=("Trebuchet MS",40,"bold"),bg="red",fg="yellow")
        title.pack(side=TOP, fill=X)
        #====All variables===
        self.name_var=StringVar()
        self.roll_var=StringVar()
        self.class_var=StringVar()
        self.gender_var=StringVar()
        self.dob_var=StringVar()
        self.ph_var=StringVar()
        self.mail_var=StringVar()
        self.searchby=StringVar()
        self.searchvalue=StringVar()

       
        #===Manage Frame===================

        Manage_Frame=Frame(self.root, bd=4, relief=RIDGE, bg="blue")
        Manage_Frame.place(x=0,y=90, width=450, height= 600)
        m_title=Label(Manage_Frame, text="Manage Students", bg="blue", fg="white", font=("Trebuchet MS",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
        lbl_name=Label(Manage_Frame, text="Name", bg="blue", fg="white", font=("Trebuchet MS",16,"bold"))
        lbl_name.grid(row=1, column=0,pady=5,padx=20, sticky="w")
        txt_name=Entry(Manage_Frame, textvariable=self.name_var, font=("Trebuchet MS",15,"bold"),bd=5, relief=GROOVE)
        txt_name.grid(row=1, column=1,pady=5,padx=20, sticky="w")
        lbl_roll=Label(Manage_Frame, text="Roll No.", bg="blue", fg="white", font=("Trebuchet MS",16,"bold"))
        lbl_roll.grid(row=2, column=0,pady=5,padx=20, sticky="w")
        txt_roll=Entry(Manage_Frame,textvariable=self.roll_var, font=("Trebuchet MS",15,"bold"),bd=5, relief=GROOVE)
        txt_roll.grid(row=2, column=1,pady=5,padx=20, sticky="w")
        lbl_class=Label(Manage_Frame, text="Class", bg="blue", fg="white", font=("Trebuchet MS",16,"bold"))
        lbl_class.grid(row=3, column=0,pady=5,padx=20, sticky="w")
        comb_class=ttk.Combobox(Manage_Frame,textvariable=self.class_var,font=("Trebuchet MS",13,"bold"))
        comb_class['values']=("6","7","8","9","10","11","12")
        comb_class.grid(row=3, column=1,pady=5,padx=20, sticky="w")
        lbl_gender=Label(Manage_Frame, text="Gender", bg="blue", fg="white", font=("Trebuchet MS",16,"bold"))
        lbl_gender.grid(row=4, column=0,pady=5,padx=20, sticky="w")
        comb_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("Trebuchet MS",13,"bold"))
        comb_gender['values']=("Male", "Female", "Others")
        comb_gender.grid(row=4, column=1,pady=5,padx=20, sticky="w")
        lbl_dob=Label(Manage_Frame, text="D.O.B", bg="blue", fg="white", font=("Trebuchet MS",16,"bold"))
        lbl_dob.grid(row=5, column=0,pady=5,padx=20, sticky="w")
        txt_dob=Entry(Manage_Frame,textvariable=self.dob_var, font=("Trebuchet MS",15,"bold"),bd=5, relief=GROOVE)
        txt_dob.grid(row=5, column=1,pady=5,padx=20, sticky="w")
        lbl_phn=Label(Manage_Frame, text="Ph No.", bg="blue", fg="white", font=("Trebuchet MS",16,"bold"))
        lbl_phn.grid(row=6, column=0,pady=5,padx=20, sticky="w")
        txt_phn=Entry(Manage_Frame,textvariable=self.ph_var, font=("Trebuchet MS",15,"bold"),bd=5, relief=GROOVE)
        txt_phn.grid(row=6, column=1,pady=5,padx=20, sticky="w")
        lbl_mail=Label(Manage_Frame, text="Email Id", bg="blue", fg="white", font=("Trebuchet MS",16,"bold"))
        lbl_mail.grid(row=7, column=0,pady=5,padx=20, sticky="w")
        txt_mail=Entry(Manage_Frame,textvariable=self.mail_var, font=("Trebuchet MS",15,"bold"),bd=5, relief=GROOVE)
        txt_mail.grid(row=7, column=1,pady=5,padx=20, sticky="w")
        lbl_add=Label(Manage_Frame, text="Address", bg="blue", fg="white", font=("Trebuchet MS",16,"bold"))
        lbl_add.grid(row=8, column=0,pady=5,padx=20, sticky="w")
        self.txt_add=Text(Manage_Frame,width=32, height=4, font=("Trebuchet MS",10,"bold"))
        self.txt_add.grid(row=8, column=1,pady=5,padx=20, sticky="w")

        ###=====buttonframe===
        btn_frame=Frame(Manage_Frame,bd=4,relief=RIDGE, bg="yellow")
        btn_frame.place(x=5, y=515, width=432.5)
        add_btn=Button(btn_frame, command=self.add_student, text="Add", width=10, font=("Trebuchet MS",10,"bold"),bg="red",fg="white").grid(row=0,column=0,padx=8,pady=8)
        del_btn=Button(btn_frame, command=self.delete_data, text="Delete", width=10,font=("Trebuchet MS",10,"bold"),bg="red",fg="white").grid(row=0,column=1,padx=8,pady=8)
        update_btn=Button(btn_frame, command=self.update_data ,text="Update", width=10,font=("Trebuchet MS",10,"bold"),bg="red",fg="white").grid(row=0,column=2,padx=8,pady=8)
        clr_btn=Button(btn_frame, command=self.clear, text="Clear", width=10,font=("Trebuchet MS",10,"bold"),bg="red",fg="white").grid(row=0,column=3,padx=8,pady=8)



        #===Details Frame=================

        Detail_Frame=Frame(self.root, bd=4, relief=RIDGE, bg="pink")
        Detail_Frame.place(x=451,y=90, width=900, height= 600)

        ##====Search=====

        lbl_search=Label(Detail_Frame,text="Search by", bg="pink", fg="white", font=("Trebuchet MS",16,"bold"))
        lbl_search.grid(row=0, column=0,pady=5,padx=20, sticky="w")
        comb_search=ttk.Combobox(Detail_Frame,textvariable=self.searchby,font=("Trebuchet MS",15,"bold"))
        comb_search['values']=("roll_no", "name", "ph_no","class")
        comb_search.grid(row=0, column=1,pady=5,padx=10, sticky="w")
        txt_search=Entry(Detail_Frame,textvariable=self.searchvalue, font=("Trebuchet MS",12,"bold"),bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2,pady=5,padx=10, sticky="w")
        search_btn=Button(Detail_Frame, command=self.search_data, text="Search", width=10,font=("Trebuchet MS",10,"bold"),bg="red",fg="white").grid(row=0,column=3,padx=10,pady=5)
        showall_btn=Button(Detail_Frame, command=self.fetch_data, text="Show all", width=10,font=("Trebuchet MS",10,"bold"),bg="red",fg="white").grid(row=0,column=4,padx=10,pady=5)

        #====Table Frame===
        tab_frame=Frame(Detail_Frame,bd=4, relief=RIDGE ,bg= "green")
        tab_frame.place(x=10,y=45,height=540, width=875)
        scroll_x=Scrollbar(tab_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(tab_frame,orient=VERTICAL)
        self.student_tab= ttk.Treeview(tab_frame,columns=("Name","Roll No.","Class","Gender","D.O.B","Ph No.","Email Id", "Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_tab.xview)
        scroll_y.config(command=self.student_tab.yview)
        self.student_tab.heading("Name",text="Name")
        self.student_tab.heading("Roll No.",text="Roll No.")
        self.student_tab.heading("Class",text="Class")
        self.student_tab.heading("Gender",text="Gender")
        self.student_tab.heading("D.O.B",text="D.O.B")
        self.student_tab.heading("Ph No.",text="Ph No.")
        self.student_tab.heading("Email Id",text="Eamil Id")
        self.student_tab.heading("Address",text="Adress")
        self.student_tab['show']='headings'
        self.student_tab.column("Name",width=150)
        self.student_tab.column("Roll No.",width=100)
        self.student_tab.column("Class",width=75)
        self.student_tab.column("Gender",width=100)
        self.student_tab.column("D.O.B",width=100)
        self.student_tab.column("Ph No.",width=100)
        self.student_tab.column("Email Id",width=100)
        self.student_tab.column("Address",width=200)
        self.student_tab.pack(fill=BOTH,expand=1)
        self.student_tab.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_student(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="sms")
        cur=con.cursor()
        cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)",
        (
        self.name_var.get(),
        self.roll_var.get(),
        self.class_var.get(),
        self.gender_var.get(),
        self.dob_var.get(),
        self.ph_var.get(),
        self.mail_var.get(),
        self.txt_add.get('1.0',END)))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="sms")
        cur=con.cursor()
        cur.execute("select * from student")
        rows=cur.fetchall()
        self.student_tab.delete(*self.student_tab.get_children())
        for row in rows:
                self.student_tab.insert('',END,values=row)
                con.commit()
        con.close 

    def clear(self):
        self.name_var.set(""),
        self.roll_var.set(""),
        self.class_var.set(""),
        self.gender_var.set(""),
        self.dob_var.set(""),
        self.ph_var.set(""),
        self.mail_var.set(""),
        self.txt_add.delete('1.0',END)
    
    def get_cursor(self,ev):
        cursor_row= self.student_tab.focus()
        contents= self.student_tab.item(cursor_row)
        row=contents['values']
        self.name_var.set(row[0]),
        self.roll_var.set(row[1]),
        self.class_var.set(row[2]),
        self.gender_var.set(row[3]),
        self.dob_var.set(row[4]),
        self.ph_var.set(row[5]),
        self.mail_var.set(row[6]),
        self.txt_add.delete('1.0',END)
        self.txt_add.insert(END,row[7])

    def update_data(self):
         pass
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="sms")
        cur=con.cursor()
        cur.execute("delete from student where roll_no=%s",self.roll_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="sms")
        cur=con.cursor()
        cur.execute("select * from student where " +str(self.searchby.get())+" LIKE '%"+str(self.searchvalue.get())+"%'")
        rows=cur.fetchall()
        self.student_tab.delete(*self.student_tab.get_children())
        for row in rows:
                self.student_tab.insert('',END,values=row)
                con.commit()
        con.close()
    

            





root=Tk()
ob=Student(root)
root.mainloop()