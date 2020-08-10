# 딕션어리(dict)
# key, value 형태
# 순서 없음, 중복 안됨, 수정 삭제 가능
# 자바의 map과 같음

#%%
# key : value 형태로 작성
# key 값은 정수형, 문자형
dict1 = {"name": "Park", "age": 12}
print(dict1)

dict2 = {0: "Hello", 1: "Python", 2: "Coding"}
print(dict2)

dict3 = {"arr": [1, 2, 3, 4, 5]}
print(dict3)

dict4 = {"arr": (1, 2, 3, 4, 5)}
print(dict4)

#%%
# dict에서 특정 키의 값 출력하기 - 권장 방식은 get() 임.
# get() : 없는 키 값일 때 None으로 돌려 줌
print(dict1["name"])
# print(dict1["addr"])  # key가 없는데 찾으라해서 에러가 남
print(dict1.get("addr"))

#%%
# dict에 내용 추가하기
dict1["birth"] = "1115"
print(dict1)

dict2[3] = [4, 5, 6]
print(dict2)

dict4["test"] = (8, 9, 10)
print(dict4)

#%% 삭제
del dict1["birth"]
print(dict1)


#%% key 값만 가져오기
print(dict1.keys())
print(dict2.keys())
print(dict3.keys())
print(dict4.keys())

#%% dict value 값 가져오기
print(dict1.values())
print(dict2.values())
print(dict3.values())
print(dict4.values())  # 이렇게 가져올 때 리스트 방식으로 가져온다.


#%%
# key, value 형태로 가져오기
print(dict1.items())
print(dict2.items())
print(dict3.items())
print(dict4.items())

#%% 해당 키가 딕션어리 안에 있는지 확인
print("name" in dict1)
print(5 in dict2)

#%% dict 안의 모든 값 지우기
dict1.clear()
print(dict1)

#%%
myInfo = {"name": "kim", "age": 24, "city": "seoul"}
for k in myInfo.keys():
    print(k, end=" ")
print()
for v in myInfo.values():
    print(v, end=" ")
print()
for k, v in myInfo.items():
    print(k, v, end=" ")

#%%
# 4계절을 대표하는 과일을 dict 구조로 생성
# {"봄" : "딸기", ........}
# 가을의 과일이 무엇인지 출력하기
fruit_dict = {"봄": "딸기", "여름": "수박", "가을": "사과", "겨울": "귤"}
# 사과가 포함되었는지 확인하기

# print(fruit_dict["가을"])

# for v in fruit_dict.values():
#     if v == "사과":
#         print("포함되어 있음")

# 가을의 과일 무엇인지
for k in fruit_dict.keys():
    if k == "가을":
        print(fruit_dict[k])

# 사과가 포함 되었는지 확인
for v in fruit_dict.values():
    if v == "사과":
        print("사과가 포함됨")
        break
else:
    print("사과가 포함되지 않음")

#%%
# comprehension
fruit = {f for f in fruit_dict.values()}
print(fruit)

fruit = {f for f in fruit_dict.values() if f != "사과"}
print(fruit)

fruit = {(k, v) for (k, v) in fruit_dict.items()}
print(fruit)
