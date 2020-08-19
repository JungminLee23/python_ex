# 좋아하는 동물 투표하는 프로그램
from tkinter import *

# 이미지 안뜸
# def myFunc():
#     image_1 = "./resource/"
#     if rdo.get() == 1:
#         image_1 += "dog2.gif"
#     elif rdo.get() == 2:
#         image_1 += "cat2.gif"
#     elif rdo.get() == 3:
#         image_1 += "rabbit.gif"
#     photo = PhotoImage(file=image_1)
#     label_image.configure(image=photo)


# def btn():
#     label_image.pack()


# window = Tk()

# # 생성
# label = Label(window, text="좋아하는 동물 투표", font=("궁서체", 20), fg="Red")
# label_image = Label(window, image=None)
# rdo = IntVar()
# rb1 = Radiobutton(window, text="강아지", variable=rdo, value=1, command=myFunc)
# rb2 = Radiobutton(window, text="고양이", variable=rdo, value=2, command=myFunc)
# rb3 = Radiobutton(window, text="토끼", variable=rdo, value=3, command=myFunc)
# btn = Button(window, text="사진보기", command=btn)


# # 배치
# label.pack()
# rb1.pack()
# rb2.pack()
# rb3.pack()
# btn.pack()

# window.mainloop()

# ===================================================쌤 ver


def view():
    click_rdo = rdo_value.get()
    if click_rdo == 1:
        img_label.configure(image=photo1)
    elif click_rdo == 2:
        img_label.configure(image=photo2)
    else:
        img_label.configure(image=photo3)


window = Tk()
window.geometry("500x400")
title = Label(window, text="좋아하는 동물 투표", font=("궁서체", 30), fg="red")

rdo_value = IntVar()

rdo_dog = Radiobutton(window, text="강아지", variable=rdo_value, value=1)
rdo_cat = Radiobutton(window, text="고양이", variable=rdo_value, value=2)
rdo_rabbit = Radiobutton(window, text="토끼", variable=rdo_value, value=3)

photo1 = PhotoImage(file="./resource/dog2.gif")
photo2 = PhotoImage(file="./resource/cat2.gif")
photo3 = PhotoImage(file="./resource/rabbit.gif")

button = Button(window, text="사진보기", command=view)
img_label = Label(window, image=None)


title.pack()
rdo_dog.pack()
rdo_cat.pack()
rdo_rabbit.pack()
button.pack()
img_label.pack()
window.mainloop()
