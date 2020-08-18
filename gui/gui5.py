from tkinter import *

window = Tk()


def test():
    pass


# 버튼이 눌려지면 무슨 일을 하게 하고 싶으면 command 다음에
# 해야 하는 일이 들어있는 함수 명을 넣어준다.
btn = Button(window, text="종료", fg="red", command=test)
btn.pack()
window.mainloop()

