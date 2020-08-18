from tkinter import *

window = Tk()

# PhotoImage는 jpg 파일을 끌고 들어오지 못한다.
photo = PhotoImage(file="./resource/cat2.gif")

label = Label(window, image=photo)

label.pack()
window.mainloop()
