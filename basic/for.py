# for


#%%
# range() : 범위를 줄 수 있는 함수(범위 지정)
print(range(5))  # 0~5
print(list(range(5)))  # [0,1,2,3,4]
print(list(range(1, 5)))  # [1,2,3,4] -> 1 <= x < 5 이런 느낌
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8] -> 세 번째는 증감에 대한 것

#%%
# 0~9까지 출력
for i in range(1, 10):
    print(i, end=" ")

print()
# 1~10까지 출력
for i in range(1, 11):
    print(i, end=" ")

# 1~100까지 출력
for i in range(1, 101):
    print(i, end=" ")

#%%
# 1~10 사이에 짝수만 출력
for i in range(1, 11):
    if i % 2 == 0:
        print(i, end=" ")

#%%
total = 0
# 1 ~ 100까지 합계를 구한 후 출력
for i in range(1, 101):
    total += i

print(total)

#%% 사용자로부터 숫자를 입력받아
# 1~ 사용자가 입력한 숫자까지 합계를 구하시오

# num = int(input("숫자 입력 : "))
# total = 0
# for i in range(1, num + 1):
#     total += i
# print(total)

#%%
for i in range(4, -1, -1):
    print(i, end=" ")

#%%
print(sum(range(1, 11)))
print(sum(range(1, 101)))

#%%
word = "dreams"
for s in word:
    print(s)

#%%
# 3단 출력
for i in range(1, 10):
    print(3, " * ", i, " = ", 3 * i)

#%%
# 이중 for문
for i in range(3):
    for j in range(3):
        print(j, end="")
    print()

#%%
for i in range(3):
    for j in range(3):
        print("*", end="")
    print()

#%%
# 0 1 2 3 4
# 1 2 3 4 5
# 2 3 4 5 6
# 3 4 5 6 7
# 4 5 6 7 8

for i in range(5):
    for j in range(5):
        print(i + j, end=" ")
    print()

#%% 2~9단 출력
# 2 * 1 = 2 2 * 2 = 4..
# 3 * 1 = 3 3 * 2 = 6...
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i * j, end=" ")
    print()

#%% 2~9단 출력
# 2*1=2 3*1=3 4*1=4
# 2*2=4 3*2=6...
for i in range(1, 10):
    for j in range(2, 10):
        print("%d*%d=%d" % (j, i, (j * i)), end="\t")
    print()
#%%
i = 1
while i <= 10:
    if i == 5:
        break
    print(i, end=" ")
    i += 1

#%%
i = 1
while i <= 10:
    i += 1
    if i % 2 == 1:
        continue
    print(i, end=" ")

#%%
# 1~10까지 출력하는데(단, 5를 제외)
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" ")

#%%
# 직각 삼각형 형태의 별
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
