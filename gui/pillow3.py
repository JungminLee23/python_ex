from PIL import Image, ImageFilter

image = Image.open("./resource/dog.jpg")

# Thumbnail 이미지 생성
size = (64, 64)
image.thumbnail(size)

image.save("./resource/python-thumb.jpg")

# 크기 조정
image2 = Image.open("./resource/dog.jpg")
image2 = image.resize((600, 600))
image2.save("./resource/dog-resize.jpg")


# 회전
image3 = Image.open("./resource/dog.jpg")
image3.rotate(90).save("./resource/dog-rotate.jpg")

# blur
image4 = Image.open("./resource/dog.jpg")
image4.filter(ImageFilter.BLUR).save("./resource/dog-blur.jpg")
