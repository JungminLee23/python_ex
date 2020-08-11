# function(함수)

#%%
# 함수정의
def hello():
    print("Hello!!!!!!!!!")


# 함수 사용
hello()

#%%
def hello2():
    return "Helloooo!!!"


# 함수 사용
print(hello2())
msg = hello2()
print(msg, "Hong!!")

#%% 함수 안에 인수 사용
def add(a, b):
    print(a + b)


add(5, 6)

#%%
def add2(a, b):
    return a + b


print(add2(4, 5))

#%% 가변 인자
def add_many(*args):
    print(args)


add_many(15, 63, 869, 45, 67, 5)
add_many(16)
add_many(27, 35, 36)
add_many()
add_many("abc", "def", "hjl")

#%% 2
def add_many2(*args):
    result = 0
    for i in args:
        result += i
    print(result)


add_many2(15, 63, 869, 45, 67, 5)
add_many2(16)
add_many2(27, 35, 36)
add_many2()


#%% 가변인자를 사용 시 주의점
# 가변 매개변수 뒤에는 일반 매개변수가 올 수 없음
# 가변 매개변수는 하나만 사용 가능
def sum_mul(choice, *args):
    if choice == "mul":
        result = 1
        for i in args:
            result *= i
    elif choice == "add":
        result = 0
        for i in args:
            result += i
    return result


print("덧셈 : ", sum_mul("add", 1, 2, 3, 4, 5))
print("곱셈 : ", sum_mul("mul", 1, 2, 3, 4, 5))

#%%
def args_func(*args):
    for arg in args:
        print(arg)
    for k, v in enumerate(args):
        print(k, v)


args_func(1, 23, 546)
args_func("a", "b", "c")
args_func([2, 3, 45, 67])
args_func((2, 3, 45, 67))
args_func({"name": "hong", "age": 25, "addr": "서울"})

#%%
# **kwargs : 가변 인자들을(파라미터) 딕셔너리 형태로 처리
def args_func2(**kwargs):
    print(kwargs)


args_func2(name="Kim")
args_func2(name="Park", age=10, title="title")
args_func2(name="Cho", name2="min", active="test")

#%%
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, *args, **kwargs)


example_mul(10, 20)
example_mul(20, 30, "park", "kim")
# example_mul(20, 30, "park", "kim", age=25, name="cho")

#%% 기본 매개변수
def print_n_times(value, n=2):
    for i in range(n):
        print(value)


print_n_times("안녕하세요", n=4)


#%% 다중 리턴
def sum_and_mul(a, b):
    return a + b, a * b


print(sum_and_mul(3, 4))  # 기본 결과는 튜플로

#%%
a, b = sum_and_mul(4, 5)  # 이 경우 결과는 개별 변수에 담김
print(a, " ", b)

#%%
def func_mul(x):
    y1 = x * 100
    y2 = x * 1000
    y3 = x * 10000
    # return [y1, y2, y3]
    return (y1, y2, y3)


# list1 = func_mul(10)
# print(list1)
tuple = func_mul(10)
print(tuple)

#%%
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." % nick)


say_nick("바보")
say_nick("야호")

#%% 두 개의 인자와 연산자를 받아서 사칙연산을 수행하는 fourRules 함수를 작성하시오.
def fourRules(x, y):
    sum = x + y
    minus = x - y
    mul = x * y
    div = x // y
    return sum, minus, mul, div


print(fourRules(6, 3))

#%%
def fourRules2(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "//":
        return num1 // num2


a, b = 6, 3
print("{} {} {} = {}".format(a, "+", b, fourRules2(a, b, "+")))
print("{} {} {} = {}".format(a, "-", b, fourRules2(a, b, "-")))
print("{} {} {} = {}".format(a, "*", b, fourRules2(a, b, "*")))
print("{} {} {} = {}".format(a, "//", b, fourRules2(a, b, "//")))

#%% 1~100까지 소수 구하기

list1 = []
list1.append(2)


def sosu():
    for i in range(2, 101):
        for j in range(2, i):
            if i % j == 0:
                break
            if i == j + 1:
                list1.append(i)


sosu()
print(list1)

#%%
prime_list = []


def isPrime(x):
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt += 1

    if cnt == 2:
        prime_list.append(x)
    return prime_list


for j in range(1, 100):
    isPrime(j)

print(prime_list)

#%% 중첩 된 리스트를 하나의 리스트로 반환하는 함수
# def flatten(data):
#     list1 = []
#     for i in range(len(data)):
#         while True:
#             if type(data[i]) == int:
#                 list1.append(data[i])
#                 break
#             else:
#                 for j in len(data[i]):
#                     if len(data[i][j]) == 1:
#                         list1.append(data[i][j])
#                         break


def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output


example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본 : ", example)
print("변환 : ", flatten(example))  # [1,2,3,4,5,6,7,8,9] 형태로 출력되도록

#%%
output = [[], [], []]


def reshape(numbers):
    for i in numbers:
        output[(i + 2) % 3].append(i)
    return output


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("원본 : ", numbers)
print("변환 : ", reshape(numbers))  # [[1,4,7], [2,5,8], [3,6,9]]

#%%
import random


def get_number():
    return random.randrange(1, 46)


lotto = []
num = 0
print("로또 추첨 시작")
while True:
    num = get_number()

    if lotto.count(num) == 0:
        lotto.append(num)
    if len(lotto) >= 6:
        break

lotto.sort()
print("추첨된 로또 번호 ==> ", lotto)

#%% 변수의 유효범위
a = 1


def func1(a):
    print("함수 내부 ", a)
    a += 1
    print("함수 내부 ", a)


def func2():
    # 함수 내부에서 함수 외부에 있는 변수를 참조하지 못함
    # 그래서 참조하기 위한 구문 필요
    global a
    a += 3
    return a


func1(1)
print(a)
print(func2())
