from tkinter import *
from path_relative import *
from tkinter import messagebox as m
import csv
from tkinter import ttk
import re


def search():
    global house
    house=[]
    class unonode:
        def __init__(self,fno=None,price=None,bhk=None,status=None,contact=None,type=None,next=None):
            self._fno=fno
            self._price=price
            self._bhk=bhk
            self._status=status
            self._contact=contact
            self._type=type
            self._next=next
    class unoccupied:
        def __init__(self):
            self._head=unonode()
            pos=self._head
            with open(r'D:\vs code prog\finaldraft\unoccupied_final.csv',"r") as csvfile:
                data=csv.reader(csvfile,delimiter=",")
                for i in data:
                 pos._next=unonode(i[0],i[1],i[2],i[3],i[4],i[5],pos._next)
                 pos=pos._next
        def display(self):
            pos=self._head
            s=''
            l=[]
            
            
            while pos._next is not None:
                s='Flat no.: '+ pos._next._fno+"   "+'Price: '+pos._next._price+"\n"+pos._next._bhk+"    "+pos._next._status+"   "+" Contact number: "+pos._next._contact+"   "+pos._next._type.capitalize()+'\n' 
                l.append(s)  
                global house
                house.append(pos._next._fno)
                pos=pos._next
            return l
        def link_delete(self,flat):
            pos=self._head
            while pos._next is not None:
                if pos._next._fno==flat:
                    pos._next=pos._next._next
                    break
                pos=pos._next
        def delete(self,flat):
            import csv
            input = open('unoccupied_final.csv', 'r+')
            writer = csv.writer(input)
            for row in csv.reader(input):
             if row[0]!=flat:
                writer.writerow(row)
            input.close()
        


    def sign():
        win = Toplevel(root)
        win.geometry("1200x900")
        win.title("SIGN UP")

        global regex
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        def check(email):
         if(re.fullmatch(regex, email)):
            return True
         else:
            return False
        def sign_up():
                if entry_1.get()=='' or entry_2.get()=='' or entry_3.get()=='' or entry_4.get()=='':
                    m.showerror("Error","All fields are mandatory")
                else:
                    if entry_1.get() not in house:
                        m.showerror("Error","Enter valid Flat number")
                        sign()
                    elif  not (entry_4.get().isdigit()) or len(entry_4.get())<10 :
                        m.showerror("Error","Enter valid Mobile number")
                        sign()
                    elif not (check(entry_3.get())):
                        m.showerror("Error","Enter valid Email id")
                        sign()
                    elif not(entry_2.get().isalpha()):
                        m.showerror("Error","Name must be alphabets")
                        sign()
                    else:
                        new= Toplevel(win)
                        new.geometry("1200x900")
                        new.title("BOOKING")
                        image_back = PhotoImage(file=relative_to_assets("thank.png"))
                        l = Label(new,image=image_back)
                        l.place(x=0,y=0)
                        user=Label(new,text=entry_1.get(),font=('Helvetica',19))
                        user.place(x=822,y=565)
                        import random
                        import string
                        # get random string of letters and digits
                        source = string.ascii_letters + string.digits
                        result_str = ''.join((random.choice(source) for i in range(6)))
                        pass_w=result_str
                        passw=Label(new,text=pass_w,font=('Helvetica',19))
                        passw.place(x=822,y=619.5)
                        flat_no=entry_1.get()
                        unc=unoccupied()
                        unc.link_delete(str(flat_no))
                        #unc.delete(str(flat_no)) 
                        new.mainloop() 
                        #entry_1 is flat no.
                        #entry_2 is name
                        #entry_3 is email
                        #entry_4 is contact no.
                        #must add all these records to occupied
                    

        image_background = PhotoImage(
        file=relative_to_assets("BG.png"))

        label = Label(
        win,
        image=image_background
    )
        label.place(x=0, y=0)

        entry_1 = Entry(win,
                bd=0,
                bg="#D9D9D9",
                highlightthickness=0,
                fg="black",
                font=("Courier","18")
            )
        entry_1.place(
                x=735.0,
                y=258.0,
                width=387.0,
                height=52.0
            )
            
        entry_2 = Entry(win,
                bd=0,
                bg="#D9D9D9",
                highlightthickness=0,
                fg="black",
                font=("Courier","18")
            )
        entry_2.place(
                x=735.0,
                y=362.0,
                width=387.0,
                height=52.0
            )

        entry_3 = Entry(win,
                bd=0,
                bg="#D9D9D9",
                highlightthickness=0,
                fg="black",
                font=("Courier","16")
    )
        entry_3.place(
                x=735.0,
                y=470.0,
                width=387.0,
                height=52.0
            )

        entry_4 = Entry(win,
                bd=0,
                bg="#D9D9D9",
                highlightthickness=0,
                fg="black",
                font=("Courier","18")
    )
        entry_4.place(
                x=735.0,
                y=575.0,
                width=387.0,
                height=52.0
            )

        button_image_1 = PhotoImage(
                file=relative_to_assets("button_1.png"))
                
        button_1 = Button(win,
                image=button_image_1,
                borderwidth=0,
                highlightthickness=0,
                command=sign_up ,
                relief="flat")

        button_1.place(
                x=810.0,
                y=710.0,
                width=215,
                height=60)
        win.resizable(False,False)
        win.mainloop()

    root =Tk()
    root.geometry('1800x1800')
    root.title('Kaushalya Alacrity Apartments')
    main_frame=Frame(root)
    main_frame.pack(fill=BOTH,expand=1)
    #create canvas
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
    #create scrollbar
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e : my_canvas.configure(scrollregion=my_canvas.bbox('all')) )
    second_frame= Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame,anchor='nw')
    p=0
    for i in unoccupied().display():
        
        frame_body=Frame(second_frame,width=380, height=150,background='lightblue', highlightbackground='black',highlightthicknes=3)
        frame_body.grid(row=p+1,column=0,padx=20,pady=20,ipadx=5,ipady=5,columnspan=2)
        l3=Label(frame_body,text= i,font=('Helvetica',24),fg='#1A1A1A',width=80,height=5)
        l3.grid(row=p,column=0,padx=10,pady=10)
        b1=Button(frame_body,text='REGISTER NOW',font=('Helvetica',15),bg='#98F5FF',fg='#1A1A1A',command=sign)
        b1.grid(row=p+1,column=1,padx=20,pady=10)
        p+=1
    root.mainloop()


