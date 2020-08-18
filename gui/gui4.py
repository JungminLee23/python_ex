from tkinter import *

window = Tk()

# PhotoImage는 jpg 파일을 끌고 들어오지 못한다.
photo1 = PhotoImage(file="./resource/cat2.gif")
photo2 = PhotoImage(file="./resource/dog2.gif")


label1 = Label(window, image=photo1)
label2 = Label(window, image=photo2)


label1.pack(side=LEFT)
label2.pack()
window.mainloop()
