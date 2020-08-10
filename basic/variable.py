# 변수 : 정수형, 문자형, 실수형, 불린형
#         타입을 지정하지 않는다.(값을 할당 받으면 타입이 결정)
str1 = "Life is too short, You need Python"
str2 = "123"

num1 = 10
num2 = 10.5

num3 = num4 = 20
print("num3 = ", num3)
print("num4 = ", num4)


num5, num6 = 10, 20
print("num5 = %d, num6 = %d" % (num5, num6))

# num5와 num6의 값을 서로 바꿔서 출력
num5, num6 = num6, num5
print("num5 = %d, num6 = %d" % (num5, num6))

str3 = 500
print(type(str3))
str3 = "Hello"
print(type(str3))

# 정수형 값
a = 123
b = -178
c = 0

# 실수형 값
a = 1.2
b = -3.45
c = 4.24e10
d = 4.24e-10
print("c : ", c, " d : ", d)

# 8진수, 16진수
print()
print(0o177)  # 0o : 8진수
print(0x1511)  # 0x : 16진수


# type() : 변수의 타입을 확인
# 변수의 타입을 변경 : str() - 문자열로 변경
#                     int() - 정수형
print("\n~~~변수 타입 확인 및 변경~~~")
a = 3
print("a 타입 : ", type(a))  # <class 'int'>
print("a 타입 : ", type(str(a)))  # <class 'str'>
print("1.2 타입 : ", type(str(1.2)))
print("True 타입 : ", type(str(True)), str(True))
print()
print("True 타입 : ", type(int(True)), int(True))

print("1.2 타입 : ", type(int(1.2)), int(1.2))
print("3.5 타입 : ", type(int(3.5)), int(3.5))

# 소수점, 지수를 포함하는 문자열은 정수형으로 변경하지 않는다.
# print("'99 타입 : ", type(int("99.5")), int("99.5"))

print()
print("True 타입 : ", type(float(True)), float(True))
print("False 타입 : ", type(float(False)), float(False))
print("'99' 타입 : ", type(float(99)), float(99))

print()
print("99 타입 : ", type(bool(99)), bool(99))
print("0 타입 : ", type(bool("0")), bool("0"))
print("0.1 타입 : ", type(bool(0.1)), bool(0.1))
print("0 타입 : ", type(bool(0)), bool(0))
print("1 타입 : ", type(bool(1)), bool(1))
