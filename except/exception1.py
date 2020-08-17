# 예외상황
# 컴파일 예외 => 문법적인 에러
# 런타임 예외 => 실행 후에 나타나는 에러


#%% 컴파일 에러
# print("Test)
# 이런 오류의 경우 잘 잡아줌

#%%
a, b = 10, 15
# print(c)  # NameError : 참조변수 없음

# ---------------------------------------여기까지 컴파일 에러

#%% 런타임 에러

print(10 / 0)  # ZeroDivisionError : 0으로 나누면 안된다.
# 빨간줄 안뜸

#%%
list1 = [10, 20, 30]
print(list1[0])
print(list1[3])  # IndexError : 인덱스가 범위 밖임

#%%
dict = {"name": "Kim", "age": 25, "city": "seoul"}
# print(dict["hobby"])  # KeyError : key 값 없는데 쓰면 이런 에러 남

# 그렇기에 get으로 쓰는게 권장사항?
print(dict.get("hobby"))  # None 뜸

#%%
x = [1, 5, 9]
# x.remove(10)  # ValueError : list.remove(x)
x.index(10)  # ValueError : 10 is not in list

#%%
number_input = int(input("정수 입력 >> "))
print("원 반지름 : ", number_input)
print("원 둘레 : ", 2 * 3.14 * number_input)
print("원 넓이 : ", 3.14 * number_input * number_input)

# 숫자를 넣으면 잘 실행 됨
# 근데 글자를 넣으면 ValueError가 나옴.
# ==> int 타입으로 변환할 수 없어서

#%%
x = [1, 2]  # 리스트
y = (3, 4)  # 튜플
# print(x + y)  # TypeError : list와 튜플을 더해서 에러 남.(타입이 달라서)
print(x + list(y))  # 이렇게 써주면 된다.
