from tkinter import *

window = Tk()

flist = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif",
         "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]

photoList = [None] * 9
num = 0


def Next():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file="../August/GIF/" + flist[num])
    pLabel.configure(image=photo)
    pLabel.image = photo


def pre():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file="../August/GIF/" + flist[num])
    pLabel.configure(image=photo)
    pLabel.image = photo


# 메인코드

window.geometry("700x500")
window.title("사진 앨범 보기")

btNext = Button(window, text="다음", command=Next)
btPre = Button(window, text="이전", command=pre)

photo = PhotoImage(file="../August/GIF/" + flist[0])
pLabel = Label(window, image=photo)

btNext.place(x=250, y=10)
btPre.place(x=400, y=10)
pLabel.place(x=15, y=50)

window.mainloop()
