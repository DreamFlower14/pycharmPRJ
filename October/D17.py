from tkinter import *
from tkinter import messagebox


def cute():
    messagebox.showinfo("강쥐버튼", "강쥐 참 귀엽죠..?")


window = Tk()

window.geometry("400x100")
window.resizable(width=True, height=True)
photo = PhotoImage(file="../August/GIF/dog.gif")
버튼 = Button(window, image=photo, command=cute)

버튼.pack()
window.mainloop()
