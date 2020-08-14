import os

print("현재 운영체제 : ", os.name)
print("현재 폴더 : ", os.getcwd())
print("현재 폴더 내부의 요소 : ", os.listdir())

# os.mkdir("hello")  # hello 폴더 만들어짐.
os.rmdir("hello")  # hello 폴더 삭제
