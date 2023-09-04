from tkinter import *
from path_relative import *
from login_module import *
from main import *
abt =Tk()
abt.geometry('1400x1024')
abt.title('Kaushalya Alacrity Apartments')
image_background = PhotoImage(
    file=relative_to_assets("Desktop.png"))
label = Label(abt,image=image_background)
label.place(x=0, y=0)
button_image_1 = PhotoImage(
            file=relative_to_assets("login.png"))
            
button_1 = Button(abt,image=button_image_1,borderwidth=0,highlightthickness=0 ,relief="flat")
button_1.place(x=78.0,y=227.0,width=217,height=50)
button_image_2 = PhotoImage(
            file=relative_to_assets("search.png"))
            
button_2 = Button(abt,image=button_image_2,borderwidth=0,highlightthickness=0 ,relief="flat")
button_2.place(x=78.0,y=332.0,width=217,height=50)
abt.mainloop()
