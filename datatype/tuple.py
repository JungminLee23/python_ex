# tuple.py
# 값을 수정 할 수 없음. 읽기만 가능 => 속도가 빠름

#%%

t1 = ()
t2 = (1, 2, 3)
t3 = (1,)
t4 = 1, 2, 3
t5 = (1, 2, "Life", "is")
t6 = (1, 2, ("Life", "is"))


#%%
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)

#%% 튜플은 삽입, 삭제, 수정 불가
# del t2[0]
# t1[0] = 1

#%% 인덱싱, 슬라이싱, +, *
print(t5[3])
print(t5[0:3])
print(t2[0] + t2[1])
print(t2 + t3)
# print(t2 * t3) # 안됨ㄴ
print(t2 * 2)  # 반복의 의미로 튜플 * 일반 숫자는 가능

#%% 튜플을 리스트로 변경 / 리스트를 튜플로 변경
print(list(t2))

list1 = [5, 2, 3, 4]
print(tuple(list1))

#%% 튜플 자체 삭제
del t2

