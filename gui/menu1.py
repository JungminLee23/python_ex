from tkinter import *


def fileOpen():
    print("파일 오픈")


window = Tk()

# 메뉴를 담을 전체 메뉴 생성
mainMenu = Menu(window)
# 부모 윈도우에 메뉴 할당
window.config(menu=mainMenu)

# 화면에 보여줄 메뉴 생성
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
# 파일 메뉴의 서브 메뉴 생성
fileMenu.add_command(label="열기", command=fileOpen)
fileMenu.add_separator()
fileMenu.add_command(label="종료")


window.mainloop()
