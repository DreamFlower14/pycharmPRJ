from tkinter import *
from tkinter import messagebox

window = Tk()


def tclass():
    if chk.get() == 0:
        messagebox.showinfo("", "체크버튼 off")
    else:
        messagebox.showinfo("", "체크버튼 on")


# 메인 코드

chk = IntVar()
cb = Checkbutton(window, text="클릭하세요~",variable=chk, command=tclass)

cb.pack()
window.mainloop()
