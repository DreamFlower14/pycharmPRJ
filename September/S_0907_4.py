from tkinter import *

window = Tk()

btnList = [None] * 3

for i in range(0,3) :
    btnList[i] = Button(window, text = "버튼" + str(i + 1))

for btn in btnList :
    btn.pack(side = TOP,fill = X, ipadx = 10, ipady = 10)

# button1 = Button(window, text = "버튼1")
# button2 = Button(window, text = "버튼2")
# button3 = Button(window, text = "버튼3")
#
# button1.pack(side = LEFT)
# button2.pack(side = LEFT)
# button3.pack(side = LEFT)

window.mainloop()