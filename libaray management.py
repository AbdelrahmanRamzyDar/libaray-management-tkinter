from tkinter import *
import tkinter as tk
from tkinter import ttk , messagebox
import mysql.connector
import sqlite3
import datetime
import tkinter



class LibarayManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management")
        self.root.geometry("1550x800+0+0")

#########################################################################

        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.fname_var=StringVar()
        self.lname_var=StringVar()
        self.address1_var=StringVar()
        self.adddress2_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.dayonbook_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.price_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.datedue_var=StringVar()
        self.fine_var=StringVar()

##########################################################################################

        libtitle = Label(self.root, text="Library Management", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        libtitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

########################################################################################
        DataFrameLeft=LabelFrame(frame,text="Library Member Information", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 15, "bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lbmember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman", 15, "bold"), padx=2, pady=6)
        lbmember.grid(row=0,column=0,sticky=W)
        
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman", 15, "bold"),width=27,state="readonly")
        comMember.grid(row=0,column=1)
        comMember["value"]=("admin staff","student","teacher")

        lblpran_no=Label(DataFrameLeft,bg="powder blue",text=" PRN NO",font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblpran_no.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,textvariable=self.prn_var,font=("times new roman", 15, "bold"), width=29)
        txtPRN_NO.grid(row=1,column=1)
      
        lblid_no=Label(DataFrameLeft,bg="powder blue",text=" ID NO",font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblid_no.grid(row=2,column=0,sticky=W)
        txtID_NO=Entry(DataFrameLeft,textvariable=self.id_var,font=("times new roman", 15, "bold"), width=29)
        txtID_NO.grid(row=2,column=1)
      
        lblfirstname=Label(DataFrameLeft,bg="powder blue",text=" F Name",font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblfirstname.grid(row=3,column=0,sticky=W)
        txtfirstname=Entry(DataFrameLeft,textvariable=self.fname_var,font=("times new roman", 15, "bold"), width=29)
        txtfirstname.grid(row=3,column=1)

        lblplastname=Label(DataFrameLeft,bg="powder blue",text=" L Name",font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblplastname.grid(row=4,column=0,sticky=W)
        txtlastname=Entry(DataFrameLeft,font=("times new roman", 15, "bold"), width=29)
        txtlastname.grid(row=4,column=1)

        lblpaddress1=Label(DataFrameLeft,bg="powder blue",text=" Address 1",font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblpaddress1.grid(row=5,column=0,sticky=W)
        txtaddress1=Entry(DataFrameLeft,textvariable=self.address1_var,font=("times new roman", 15, "bold"), width=29)
        txtaddress1.grid(row=5,column=1)
        
        lblpaddress2=Label(DataFrameLeft,bg="powder blue",text=" Address 2",font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblpaddress2.grid(row=6,column=0,sticky=W)
        txtaddress2=Entry(DataFrameLeft,textvariable=self.adddress2_var,font=("times new roman", 15, "bold"), width=29)
        txtaddress2.grid(row=6,column=1)
 
        lblpmobile=Label(DataFrameLeft,bg="powder blue",text=" Mobile",font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblpmobile.grid(row=7,column=0,sticky=W)
        txtmobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("times new roman", 15, "bold"), width=29)
        txtmobile.grid(row=7,column=1)
         
        lblpbookeid=Label(DataFrameLeft,bg="powder blue",text=" Book id",font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblpbookeid.grid(row=0,column=2,sticky=W)
        txtbookeid=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("times new roman", 15, "bold"), width=29)
        txtbookeid.grid(row=0,column=3)


         
        lblpbooktitle=Label(DataFrameLeft,bg="powder blue",text=" Book Title",font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblpbooktitle.grid(row=1,column=2,sticky=W)
        txtbooktitle=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("times new roman", 15, "bold"), width=29)
        txtbooktitle.grid(row=1,column=3)


         
        lblpauthername=Label(DataFrameLeft,bg="powder blue",text=" Author Name",font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblpauthername.grid(row=2,column=2,sticky=W)
        txtauthername=Entry(DataFrameLeft,textvariable=self.author_var,font=("times new roman", 15, "bold"), width=29)
        txtauthername.grid(row=2,column=3)

         
        lblpborraw=Label(DataFrameLeft,bg="powder blue",text=" Date Borrowed",font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblpborraw.grid(row=3,column=2,sticky=W)
        txtborraw=Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("times new roman", 15, "bold"), width=29)
        txtborraw.grid(row=3,column=3)

         
        lblpdatedue=Label(DataFrameLeft,bg="powder blue",text=" Date Due",font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblpdatedue.grid(row=4,column=2,sticky=W)
        txtdatedue=Entry(DataFrameLeft,textvariable=self.datedue_var,font=("times new roman", 15, "bold"), width=29)
        txtdatedue.grid(row=4,column=3)

         
        lblpdaysbook=Label(DataFrameLeft,bg="powder blue",text=" Day on Book",font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblpdaysbook.grid(row=5,column=2,sticky=W)
        txtdaysbook=Entry(DataFrameLeft,textvariable=self.dayonbook_var,font=("times new roman", 15, "bold"), width=29)
        txtdaysbook.grid(row=5,column=3)

         
        lblpfine=Label(DataFrameLeft,bg="powder blue",text=" Late Fine",font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblpfine.grid(row=6,column=2,sticky=W)
        txtfine=Entry(DataFrameLeft,textvariable=self.fine_var,font=("times new roman", 15, "bold"), width=29)
        txtfine.grid(row=6,column=3)

         
        lblpprice=Label(DataFrameLeft,bg="powder blue",text=" Book Price",font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblpprice.grid(row=7,column=2,sticky=W)
        txtprice=Entry(DataFrameLeft,textvariable=self.price_var,font=("times new roman", 15, "bold"), width=29)
        txtprice.grid(row=7,column=3)


        

###############################################right#################################################################

        DataFrameright=LabelFrame(frame,text="Book Information", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 15, "bold"))
        DataFrameright.place(x=910,y=5,width=540,height=350)


        self.textbox=Text(DataFrameright,font=("times new roman", 12, "bold"),width=32,height=15,padx=2, pady=6)
        self.textbox.grid(row=0,column=2)
        listscroll=Scrollbar(DataFrameright)
        listscroll.grid(row=0,column=1,padx=4,sticky="ns")

        listbok=[
                    "To Kill a Mockingbird",
                    "1984",
                    "The Great Gatsby",
                    "The Catcher in the Rye",
                    "The Lord of the Rings",
                    "Harry Potter and the Sorcerer's Stone",
                    "Pride and Prejudice",
                    "The Da Vinci Code",
                    "The Hitchhiker's Guide to the Galaxy",
                    "Brave New World",
                    "The Hunger Games",
                    "One Hundred Years of Solitude",
                    "The Road",
                    "The Girl with the Dragon Tattoo",
                    "The Shining",
                    "The Fault in Our Stars",
                    "Sapiens: A Brief History of Humankind",
                    "Educated",
                    "The Power of Habit",
                    "Atomic Habits"
                    ]
        def selectbook(event=""):
            value=str(listbox1.get(listbox1.curselection()))
            x=value
            if (x=="1984"):
                self.bookid_var.set("BKID5454" )
                self.booktitle_var.set("python")
                self.author_var.set("paul berry")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayonbook_var.set(15)
                self.fine_var.set("150pound")
                self.price_var.set("200 pound")

        listbox1=Listbox(DataFrameright,font=("times new roman", 12, "bold"),width=20,height=16)
        listbox1.bind("<<ListboxSelect>>",selectbook)
        listbox1.grid(row=0,column=0,padx=4)
        listscroll.config(command=listbox1.yview)

        for item in listbok:
            listbox1.insert(END,item)

###############################################
       


        ####################################################   button   ####################################
        framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        framebutton.place(x=0,y=530,width=1530,height=60)

        btnadddate=Button(framebutton,command=self.adddata,text="    Add Date     " ,font=("times new roman", 12, "bold"),width=25,bg="blue",fg="white")
        btnadddate.grid(row=0,column=0)

        btnadddate=Button(framebutton,text="Show Date",command=self.showdata,font=("times new roman", 12, "bold"),width=25,bg="blue",fg="white")
        btnadddate.grid(row=0,column=1)
        btnadddate=Button(framebutton,text="  Update  ",command=self.update,font=("times new roman", 12, "bold"),width=25,bg="blue",fg="white")
        btnadddate.grid(row=0,column=2)
        btnadddate=Button(framebutton,text="    Delete    "   ,command=self.delte,font=("times new roman", 12, "bold"),width=25,bg="blue",fg="white")
        btnadddate.grid(row=0,column=3)
        btnadddate=Button(framebutton,command=self.reset,text="   Reset   ",font=("times new roman", 12, "bold"),width=25,bg="blue",fg="white")
        btnadddate.grid(row=0,column=4)
        btnadddate=Button(framebutton,text="  Exit     ",command=self.exit,font=("times new roman", 12, "bold"),width=25,bg="blue",fg="white")
        btnadddate.grid(row=0,column=5)
        #################################################### information  ####################################
        framedatails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        framedatails.place(x=0,y=600,width=1530,height=195)

        

        Table_frame=Frame(framedatails,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.libaray_table=ttk.Treeview(Table_frame,column=(
                                        'membertype','firstname','last name','Book Id','Book Name','Author','Price','Date borrowd','mobile','address','day on book','fine'),show='headings',height=8,xscrollcommand=xscroll,yscrollcommand=yscroll)




        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.libaray_table.xview)
        yscroll.config(command=self.libaray_table.yview)

        self.libaray_table.heading("membertype",text="Member Type")
        self.libaray_table.heading("firstname",text="firstname")
        self.libaray_table.heading("last name",text="last name")
        self.libaray_table.heading("Book Id",text="Book Id")
        self.libaray_table.heading("Book Name",text="Book Name")
        self.libaray_table.heading("Author",text="Author")
        self.libaray_table.heading("Price",text="Price")
        self.libaray_table.heading("Date borrowd",text="Date borrowd ")
        self.libaray_table.heading("address",text=" address")
        self.libaray_table.heading("day on book",text="day on book ")
        self.libaray_table.heading("mobile",text="mobile ")
        self.libaray_table.heading("fine",text="fine ")
        
        self.libaray_table["show"]="headings"
        self.libaray_table.pack(fill=BOTH,expand=1)


        self.getdata()
        self.libaray_table.bind("<ButtonRelease-1>",self.getcu)
    def adddata(self):
        db=sqlite3.connect(r"C:\Users\abdel\libaray.db")
        cr=db.cursor()
        cr.execute("INSERT INTO libaray VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
    self.member_var.get(),
    self.prn_var.get(),
    self.id_var.get(),
    self.fname_var.get(),
    self.lname_var.get(),
    self.address1_var.get(),
    self.adddress2_var.get(),
    self.mobile_var.get(),
    self.bookid_var.get(),
    self.dayonbook_var.get(),
    self.dateborrowed_var.get(),
    self.price_var.get(),
    self.booktitle_var.get(),
    self.author_var.get(),
    self.datedue_var.get(),
    self.fine_var.get()
))

       
        db.commit()
        self.getdata()
        db.close()

        messagebox.showinfo("Success" , "member has been inserted")


    def getdata(self):
        db=sqlite3.connect(r"C:\Users\abdel\libaray.db")
        cr=db.cursor()
        cr.execute("select * from libaray")
        rows=cr.fetchall()
    

        if len(rows)!=0:
            self.libaray_table.delete(*self.libaray_table.get_children())
            for l in rows:
                self.libaray_table.insert('',END,values=l)
            db.commit()
        db.close()  

    def getcu(self,event=""):
        cr_row=self.libaray_table.focus()
        content=self.libaray_table.item(cr_row)
        row=content["values"]


        
        self.member_var.set(row[1])
        self.prn_var.set(row[2]),
        self.id_var.set(row[3]),
        self.fname_var.set(row[4]),
        self.lname_var.set(row[5]),
        self.address1_varsett(row[6]),
        self.adddress2_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.dayonbook_var.set(row[10]),
        self.dateborrowed_var.set(row[11]),
        self.price_var.set(row[12]),
        self.booktitle_var.set(row[13]),
        self.author_var.set(row[14]),
        self.datedue_var.set(row[15]),
        self.fine_var.set(row[16])
    def showdata(self):
        self.textbox.insert(END,"Member Type\t\t"+self.member_var.get()+"\n")
        self.textbox.insert(END,"id\t\t"+self.id_var.get()+"\n")
        self.textbox.insert(END,"fname\t\t"+self.fname_var.get()+"\n")
        self.textbox.insert(END,"lname\t\t"+self.lname_var.get()+"\n")
        self.textbox.insert(END,"book title\t\t"+self.booktitle_var.get()+"\n")
        self.textbox.insert(END,"dateborrowed\t\t"+self.dateborrowed_var.get()+"\n")
        self.textbox.insert(END,"fine\t\t"+self.fine_var.get()+"\n")
    def reset(self):
        
        self.member_var.set(" "),
        self.prn_var.set(" "),
        self.id_var.set(" "),
        self.fname_var.set(" "),
        self.lname_var.set(" "),
        self.address1_varsett(" "),
        self.adddress2_var.set(" "),
        self.mobile_var.set(" "),
        self.bookid_var.set(" "),
        self.dayonbook_var.set(" "),
        self.dateborrowed_var.set(" "),
        self.price_var.set(" "),
        self.booktitle_var.set(" "),
        self.author_var.set(" "),
        self.datedue_var.set(" "),
        self.fine_var.set(" "),
        self.textbox.delete('1.0', END)

    def exit(self):
        iExit=tkinter.messagebox.askyesno("Libaray management","do u want to exit")
        if iExit>0:
            self.root.destroy()
            return

    def delte(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("error","select memeber")
        else:
            db=sqlite3.connect(r"C:\Users\abdel\libaray.db")
            cr=db.cursor()
            cr.execute("delete * from libaray where PRN_NO=?",self.prn_var.get())
            db.commit()
            messagebox.showinfo("success","deleted sucessfully")
            self.reset()
            self.getdata()
            db.close()
    def update(self):
        db = sqlite3.connect('C:\\Users\\abdel\\libaray.db')
        cursor = db.cursor()
        cursor.execute("UPDATE libaray SET member=? , prn=? , id=? , fname=? , lname=?,mobile?)",( 
    self.member_var.get(),
    self.prn_var.get(),
    self.id_var.get(),
    self.fname_var.get(),
    self.lname_var.get(),
    self.address1_var.get(),
    self.adddress2_var.get(),
    self.mobile_var.get(),
    self.bookid_var.get(),
    self.dayonbook_var.get(),
    self.dateborrowed_var.get(),
    self.price_var.get(),
    self.booktitle_var.get(),
    self.author_var.get(),
    self.datedue_var.get(),
    self.fine_var.get()
))
        db.commit()
        self.getdata()
        self.reset()
        db.close()
        messagebox.showinfo("success","Data Updated Successfully")

            










if __name__ == "__main__":
    root=Tk()
    obj=LibarayManagement(root)
    root.mainloop()
