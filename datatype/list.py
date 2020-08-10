# 리스트
# JAVA에서 ArrayList

# 리스트 생성
#%%
list1 = []
list2 = ["a", "b", "c"]
list3 = ["a", "b", "c", 1, 2]
list4 = [1, 2, 3, 4, 5, 6]
list5 = [1, 2, ["Life", "is", "too", "short"]]  # 2차원 리스트

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)

#%%
# 리스트 인덱싱
print("list3[3] : ", list3[3])
print("list4[-1] : ", list4[-1])
print("list5[2] : ", list5[2])
print("list5[2][1] : ", list5[2][1])
print("list5[-1][-1]", list5[-1][-1])

#%%
list6 = [1, 2, ["a", "b", ["Life", "is"]]]

# is라는 글자를 출력하고 싶다.
print(list6[2][2][1])
# or print(list6[-1][-1][-1])

#%% 리스트 슬라이싱[ : ]
print("list3[0:2]", list3[0:2])
print("list3[:2]", list3[:2])
print("list3[0:-1]", list3[0:-1])  # 끝에 있는 숫자는 포함 안됨

print("list5[2: ] ", list5[2:])
print("list5[2][:2] ", list5[2][:2])

#%% 리스트 연산자
# + : 연결
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = ["a", "b", "c"]
print("list1 + list2 : ", (list1 + list2))
print("list1 + list3 : ", (list1 + list3))
print("list1[0] + list2[0] : ", (list1[0] + list2[0]))
print("list1[0] + list3[0] : ", (list1[0] + list3[0]))  # type에러 나옴(int와 str이기 때문에)

#%%
# * : 반복
print(" * 연산자 : ", (list1 * 3))
print(" * 연산자 : ", (list1[0] * 3))

#%%
# 리스트 요소 수정
list1[1] = 7
print(list1)
list1[1] = "Life"
print(list1)  # 타입이 달라도 상관없음

list2[1:2] = [10, 11]  # 범위를 지정해서 10, 11을 넣겠다.
print(list2)

# 리스트 안에 리스트 형태로 수정
list1[1] = [15, 16, 17]
print(list1)

#%%
# 리스트 삭제 = > del / []
print("list1 삭제 전 : ", list1)
list1[1:3] = []
print("list1 삭제 후 : ", list1)

print("list2 삭제 전 : ", list2)
del list2[1]
print("list2 삭제 후 : ", list2)

#%% 리스트 함수
# 1. append : 존재하는 리스트 뒤에 요소 추가
#             추가하는 요소는 하나의 인자만 허용
list1 = [1, 2, 3]
list1.append(4)
print(list1)

# list.append(5, 6, 7) - 불허
list1.append([5, 6, 7])
print(list1)

#%%
# 1~100까지 숫자 중에서 짝수만 리스트로 생성

list1 = []
for i in range(1, 101):
    if i % 2 == 0:
        list1.append(i)

print(list1)

#%% 리스트 함수
# 2. sort
list1 = [225, 3, 6, 9, 1, 4, 7, 15, 24]
print("정렬 전 : ", list1)
list1.sort()
print("정렬 후 : ", list1)

print()
list2 = ["k", "z", "a", "c", "f", "b"]
print("정렬 전 : ", list2)
list2.sort(reverse=True)
print("정렬 후 : ", list2)

#%%
# 3. 대소문자가 섞인 경우
list3 = ["L", "z", "A", "c", "f", "B"]
print("정렬 전 : ", list3)
list3.sort()
print("정렬 후 : ", list3)

#%%
# 4. 한글 테스트
list4 = ["ㅎ", "ㄱ", "ㄷ", "ㅁ", "ㄴ", "ㄹ"]
print("정렬 전 : ", list4)
list4.sort()
print("정렬 후 : ", list4)

#%% 리스트 함수
# 5. reverse
list1 = [25, 3, 6, 9, 1, 4, 7, 15, 24]
print("reverse 전 : ", list1)
list1.reverse()
print("reverse 후 : ", list1)

# list1 내림차순 정렬
list1.sort()
list1.reverse()
print("list1 : ", list1)

#%%
# 6. index - find는 없다.
print(list1.index(9))
# print(list1.index(2))

#%%
# 7. insert : 특정 위치에 요소 삽입
list1 = [1, 2, 3]
list1.insert(1, 10)
print(list1)

#%%
# 8. remove : 특정 위치의 요소 삭제
list1 = [1, 2, 3]
list1.insert(1, 10)
list1.remove(10)
print(list1)
list1.insert(1, 2)
print(list1)
list1.remove(2)
print(list1)


#%%
# 9. pop : 리스트 요소 중 마지막 요소
list1 = [12, 13, 14, 15, 16]
print(list1.pop())
print(list1)

#%%
# 10. count : 리스트 요소 세기
list1 = [12, 13, 14, 15, 16, 14, 14]
print(list1.count(14))

#%%
# 11. extend : +와 같은 기능
list1.extend([25, 26, 27])
print(list1)

#%%
# 12. clear : 리스트 요소 모두 삭제
list1.clear()
print(list1)


# %%
# list1 = []
if list1:
    print("True")
else:
    print("False")  # 비어있는 리스트인 경우

# str1 = ""
str1 = ""
if str1:
    print("True")
else:
    print("False")  # 값이 없는 경우

#%%
fruits = ["사과", "바나나", "딸기", "포도"]
for f in fruits:
    print(f)

if "딸기" in fruits:
    print("딸기 있음")
else:
    print("딸기 없음")

#%%
arr = [23, 12, 36, 53, 18]

for i in enumerate(arr):
    print(i)

print()

for i in enumerate(arr, start=1):
    print(i)

print()

for idx, value in enumerate(arr, start=1):
    print("{} : {}".format(idx, value))

#%% 리스트 컴프리헨션 => 리스트 내포
# 하나 이상의 이터레이터부터 파이썬의 자료 구조 만들기
# 이터레이터 => 하나 씩 가지고 나올 수 있는 것

# 리스트 생성하기

# 첫 번째
# a = [1,2,3,4,........]

# 두 번째
a = []
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)
a.append(7)

# 세 번째
a = []
for n in range(1, 11):
    a.append(n)

# 네 번째
print(list("abcdefghijklmn"))
a = list(range(1, 101))
print(a)

print()

# 다섯번째 - 컴프리핸션
print("--- comprehension ---")
numbers = [x for x in range(1, 101)]
print(numbers)

#%%
# 1~5까지 숫자 중에서 홀수만 출력
numbers = [x for x in range(1, 6) if x % 2 == 1]
print(numbers)