# 위젯 배치
from tkinter import *

window = Tk()

# 버튼 자동 생성?
for i in range(3):
    btn1 = Button(window, text="버튼" + str(i + 1))
    btn1.pack(side=BOTTOM, fill=X, padx=10, pady=10)

# btn1 = Button(window, text="버튼1")
# btn2 = Button(window, text="버튼2")
# btn3 = Button(window, text="버튼3")


# 수평배치
# btn1.pack(side=RIGHT)
# btn2.pack(side=RIGHT)
# btn3.pack(side=RIGHT)

# 수직 배치
# fill : 채우기
# padx, pady : 바깥쪽 여백
# ipadx, ipady : 안쪽 여백
# btn1.pack(side=BOTTOM, fill=X, padx=10, pady=10)
# btn2.pack(side=BOTTOM, ipadx=10, ipady=10)
# btn3.pack(side=BOTTOM)


window.mainloop()

