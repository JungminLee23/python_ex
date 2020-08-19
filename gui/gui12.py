from tkinter import *


# window = Tk()
# window.title("이미지 버튼 배치")

# img_source = "./resource/"
# btn_image = ["instagram.png", "facebook.png", "twitter.png"]

# for i in range(3):
#     img = img_source + btn_image[i]
#     photo = PhotoImage(file=img)
#     btn = Button(window, image=photo)
#     btn.pack(side=LEFT)

# window.mainloop()

# 쌤 방법
window = Tk()
window.title("이미지 버튼 배치")

photoList = [
    PhotoImage(file="./resource/instagram.png"),
    PhotoImage(file="./resource/facebook.png"),
    PhotoImage(file="./resource/twitter.png"),
]

btnList = []

for i in range(3):
    button = Button(window, image=None)
    btnList.append(button)

for i, btn in enumerate(btnList):
    button.configure(image=photoList[i])
    button.pack(side=LEFT, fill=X, ipadx=10, ipady=10)

window.mainloop()
