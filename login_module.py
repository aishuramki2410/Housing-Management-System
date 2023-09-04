from tkinter import *
from path_relative import *
import ast
from functools import partial
from tkinter import messagebox as mbox
import tkinter.font as font
import csv
def login():
    
    class Node:
      def __init__(self,flatno=None,name=None,phn=None,pwd=None,owship=None,mail=None,next=None):
        self.flatno=flatno
        self.name=name
        self.phn=phn
        self.pwd=pwd
        self.owship=owship
        self.mail=mail
        self.next=next
    class occupied_details():
        def __init__(self):
         self.head=Node()
         self.dummyend=Node()
         self.head.next=self.dummyend
        def create(self):
         with open("user_details.txt","r") as file:
            reader=file.readlines()
            
            for x in reader:
                row=list(x.split(','))
                self.head.next=Node(row[0],row[1],row[2],row[3],row[4],row[5],self.head.next)
         return ""
        def check(self):#,user_name,pass_word):
         temp=self.head
         global flatno
         global pwd
         global name
         flatno=[]
         pwd=[]
         while temp.next is not None:
            flatno.insert(0,(temp.flatno))
            pwd.insert(0,(temp.pwd))
            temp=temp.next
         return " "
        def display(self):
         temp=self.head
         global rows
         rows = []
         while temp.next !=None:
            rows.insert(0,[temp.flatno,temp.name,temp.owship,temp.mail])
            temp=temp.next
    def maintanance():
     class maintnode:
        def __init__(self,item=None,next=None):
            self._item=item 
            self._next=next
     class maintenance:
        def __init__(self):
            self._head=maintnode()
            pos=self._head
            with open(r'D:\vs code prog\finaldraft\maintaenance.csv',"r") as csvfile:
                data=csv.reader(csvfile,delimiter=",")
                for i in data:
                  pos._next=maintnode(i,pos._next)
                  pos=pos._next
        def display(self,flat):
            pos=self._head
            user.after(100, user.destroy())
            btn.after(100, btn.destroy())
            btn1.after(100, btn1.destroy())
            months=['FLAT NO','JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
            while pos._next is not None:
                myFont = font.Font(family='Times',size=17)
                if pos._next._item [0] == flat :
                    y=100
                    for i in range(13):
                        month=Label(new,text=months[i],font=myFont,fg='white',bg='black')        
                        month.place(x=400,y=y)
                        month=Label(new,text=':',font=myFont,fg='white',bg='black')        
                        month.place(x=580,y=y) 
                        y+=50
                    y=100
                    for i in range(13):
                        month=Label(new,text=pos._next._item [i],font=myFont,fg='white',bg='black')        
                        month.place(x=650,y=y)
                        y+=50
                pos=pos._next
                
     maintenance().display(usernam) #loginned flat no. should be passed as the parameter
    def display():
     sb = Scrollbar(
     new,
     orient=VERTICAL)
     sb.grid(row=len(rows), column=len(rows[0]), sticky=NS)
     for i in range (len(rows)):
            for j in range (len(rows[0])):
                textarea=Text(new,width=1500,height=900,Wrap=None,yscrollcommand=sb.set)
                e = Entry(new, width=35, fg='red',
                               font=('Arial',10,'bold'))
                e.grid(row=i, column=j)
                e.insert(0, rows[i][j])
     new.mainloop()
    def validate():
    
     if username.get() =="":
        mbox.showerror('ERROR','ALL FIELDS ARE MANDATORY')
     elif password.get() =="":
        mbox.showerror('ERROR','ALL FIELDS ARE MANDATORY')
     elif username.get() not in flatno:
        mbox.showerror('ERROR','INVALID CREDENTIALS')
     elif password.get() not in pwd:
        mbox.showerror('ERROR','INVALID CREDENTIALS')
     else:
        global usernam
        usernam=username.get()
        inde_x=flatno.index(username.get())
        i_n=(list(rows[inde_x]))
        use_r=i_n[1]
        global new
        global user
        global btn
        global btn1
        new= Toplevel()
        new.geometry("1200x850")
        new.configure(bg='black')
        new.title("DETAILS")
        myFont = font.Font(family='Times',size=23)
        user=Label(new,text=("Welcome!!!!",use_r),font=myFont,fg='white',bg='black')        
        user.place(x=400,y=100)
        btn=Button(new,text="Details",command = display)
        btn.place(
            x=450.0,
            y=300.0,
            width=216.5,
            height=61.5)
        btn1=Button(new,text="Maintainence",command = maintanance)
        btn1.place(
            x=450.0,
            y=400.0,
            width=216.5,
            height=61.5)  
    win = Tk()
    win.title('LOGIN')
    win.geometry("1200x900")
    username = StringVar()
    password = StringVar()
    a=occupied_details()
    a.create()
    a.check()
    a.display()
    image_background = PhotoImage(
    file=relative_to_assets("logbg.png"))
    label = Label(
win,
image=image_background
)
    label.place(x=0, y=0)

    entry1_user_name = Entry(win,
            textvariable=username,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0,
            fg="black",
            font=("Courier","15")
)
    entry1_user_name.place(
            x=735.0,
            y=260.0,
            width=387.0,
            height=52.0
        )
    entry2_pwd = Entry(win,
            textvariable=password,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0,
            fg="black",
            font=("Courier","15")
)
    entry2_pwd.place(
            x=735.0,
            y=376.0,
            width=387.0,
            height=52.0
        )
    button_image_1 = PhotoImage(
            file=relative_to_assets("button.png"))
    button_1 = Button(win,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=validate,
            relief="flat"
)
    button_1.place(
            x=810.0,
            y=710.0,
            width=216.5,
            height=61.5
)
    win.resizable(False,False)
    win.mainloop()




