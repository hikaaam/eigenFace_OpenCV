from tkinter import *
import os

main = Tk()
#1440,810
main.geometry('{}x{}'.format(800, 600))
main.wm_title("TA2020")

svalue = StringVar() # defines the widget state as string


comments = """Tugas Akhir Face recognition using Eigenface algorithm.







"""

widgets = Label(main, 
           justify=LEFT,
           padx = 10, 
           text=comments).pack(side="bottom")

w = Entry(main,textvariable=svalue) # adds a textarea widget
w.pack()
w.place(x=350,y=100)
def fisher_train_button_fn():
    name = svalue.get()
    os.system('python train_eigen.py %s'%name)

def fisher_recog_button_fn():
    os.system('python recog_eigen.py')

train_fisher_button = Button(main,text="train", command=fisher_train_button_fn)
train_fisher_button.pack()
train_fisher_button.place(x=350,y=150)
recog_fisher_button = Button(main,text="recognize", command=fisher_recog_button_fn)
recog_fisher_button.pack()
recog_fisher_button.place(x=350,y=200)

main.mainloop()
