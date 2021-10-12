from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.geometry('800x600')
root.title("Sign Up ")

label_0 = Label(root, text="Sign Up Form with git_hub",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Name",width=20,font=("bold", 10))
label_1.place(x=80,y=100)

entry_1 = Entry(root)
entry_1.place(x=240,y=100)

label_2 = Label(root, text="Username",width=20,font=("bold", 10))
label_2.place(x=80,y=160)

entry_2 = Entry(root)
entry_2.place(x=240,y=160)

label_3 = Label(root, text="Email ID",width=20,font=("bold", 10))
label_3.place(x=80,y=130)

entry_3 = Entry(root)
entry_3.place(x=240,y=130)

label_3_1 = Label(root, text="Password",width=20,font=("bold", 10))
label_3_1.place(x=80,y=190)

entry_3_1 = Entry(root)
entry_3_1.place(x=240,y=190)


label_3_2 = Label(root, text="Confirm Password",width=20,font=("bold", 10))
label_3_2.place(x=80,y=220)

entry_3_2 = Entry(root)
entry_3_2.place(x=240,y=220)


label_3_3 = Label(root, text="Profile Picture",width=20,font=("bold", 10))
label_3_3.place(x=500,y=100)

entry_3_3 = Entry(root)
entry_3_3.place(x=240,y=220)

    
# from PIL import Image, ImageTk

# img=PhotoImage(file='img_2.png',master = canvas, width = 20, height = 10)
# Label(root,image=img).pack()
                                                                          


label_4 = Label(root, text="Gender",width=20,font=("bold", 10))
label_4.place(x=70,y=250)

var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=250)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=250)

label_5 = Label(root, text="Education",width=20,font=("bold", 10))
label_5.place(x=70,y=280)

list1 = ['Masters','Graduation', 'Diploma'];

c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('Masters')
droplist.place(x=240,y=280)

label_6 = Label(root, text="Hobbies",width=20,font=("bold", 10))
label_6.place(x=85,y=330)



var1 = IntVar()
Checkbutton(root, text="running", variable=var1).place(x=235,y=330)
var2 = IntVar()
Checkbutton(root, text="Dancing", variable=var2).place(x=320,y=330)
var3 = IntVar()
Checkbutton(root, text="Eating", variable=var3).place(x=410,y=330)
var4 = IntVar()
Checkbutton(root, text="Sleeping", variable=var4).place(x=500,y=330)
var5 = IntVar()
Checkbutton(root, text="Singing", variable=var5).place(x=590,y=330)
var6 = IntVar()
Checkbutton(root, text="Playing", variable=var6).place(x=235,y=360)
var7 = IntVar()
Checkbutton(root, text="Surfing", variable=var7).place(x=320,y=360)
var8 = IntVar()
Checkbutton(root, text="Cricket", variable=var8).place(x=410,y=360)
var9 = IntVar()
Checkbutton(root, text="TV", variable=var9).place(x=500,y=360)
var10 = IntVar()
Checkbutton(root, text="Carroms", variable=var10).place(x=590,y=360)

Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=280,y=420)

root.mainloop()
