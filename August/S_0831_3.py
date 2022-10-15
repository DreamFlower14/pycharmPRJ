from tkinter import *

window = Tk()

label1 = Label(window, text = "Top" ,font = ("궁서체",30),fg = "white")
label2 = Label(window, text = "Gun", font = ("궁서체",30),fg = "white")
label3 = Label(window, text = "매버릭",font = ("궁서체",20),fg = "blue", width=50, height=5, anchor=CENTER)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()