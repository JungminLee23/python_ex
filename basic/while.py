#%%
i = 1
while i < 11:
    print(i)
    i = i + 1

print()
i = 1
while i <= 10:
    print(i, end=" ")

#%%
# 1~100까지 짝수만 출력
i = 1
while i <= 100:
    i += 1
    if i % 2 == 0:
        print(i, end=" ")

#%%
# 1~100까지 합계를 구한 뒤 출력
sum1, i = 0, 0
while i < 100:
    i += 1
    sum1 += i
print("1~100까지의 합 : {}".format(sum1))

#%%
# 3단 구구단 출력
i = 0
while i < 9:
    i += 1
    print("%d * %d = %d" % (3, i, (3 * i)))

#%%
# 사용자로부터 입력을 받아서 화면에 출력하기
# 종료는 q를 입력하면 종료

ans = ""
while ans != "q":
    ans = input("입력하세요(q누르면 종료) : ")
    print("사용자의 입력 값 : ", ans)
