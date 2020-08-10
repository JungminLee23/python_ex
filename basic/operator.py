#%%
# 산술 연산자 : +, -, *, /, %, //, **
a = 3
b = 4


print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)  # 그냥 곱하기
print("a / b = ", a / b)  # 소수점까지 출력
print("a // b = ", a // b)  # 정수 나누기 연산자
print("a ** b = ", a ** b)  # 제곱 연산자
#%%

#%%
print()
a, b, c = 2, 3, 4
print(a + b - c, a + b * c, a + b / c)

print()
s1, s2, s3 = "100", "100.123", "9999999999999"
print(s1 + s2 + s3)

print()
print(float(s1) + float(s2) + float(s3))

print()
# print(s1 + 1)

print(int(s1) + 1)
print()
print()
# 동전 교환하기
money = 7777

# 500원 : 00개, 100원 : 0개, 50원 : 0개, 10원 : 0개, 나머지돈
one = money // 500
money = money % 500

two = money // 100
money = money % 100

three = money // 50
money = money % 50

four = money // 10
money = money % 10

print(
    "500원 : ", one, " 100원 : ", two, " 50원 : ", three, " 10원 : ", four, " 나머지 : ", money
)
#%%
#%%
print("Jupyter")
#%%
#%%
# 대입 연산자
a = 10
a += 5  # a = a+5
print(a)
a -= 5  # a = a-5
print(a)
a *= 5  # a = a*5
print(a)
a /= 5  # a = a/5 --> 소수점까지 결과 나옴
print(a)
a //= 5  # a = a//5 --> 정수까지 결과 나옴(자바에서 쓰는 나누기 개념)
print(a)
a %= 5  # a= a%5
print(a)
a **= 5  # a = a**5 --> 제곱
print(a)
#%%


#%%
# 관계 연산자 : ==, !=, >, >=, <, <=
a, b = 10, 0
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
#%%

#%%
# 논리 연산자
a, b, c = 100, 60, 15
print("and : ", a > b and b > c)
print("or : ", a > b or b < c)
print("not : ", not b < c)
#%%

#%%
# 비트 연산자 : &, |
a, b, c = 100, 60, 15
print("& : ", 10 & 7)  # 1010 & 0111 -> 0010이 된다
print("| : ", 10 | 7)  # 1010 | 0111 -> 1111이 된다.
print("& : ", (a > b) & (b < c))  # 0001 & 0000
print("| : ", (a > b) | (b < c))  # 0001 | 0000

