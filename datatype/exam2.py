# exam2.py

#%%
# A : 90, B:80, C:70 의 형태를 dict 구조로 생성한 후 key : value 형태로 출력한다.
dict1 = {"A": 90, "B": 80, "C": 70}
print(dict1)

#%%
# 위의 dict에서 B 키에 해당하는 값만 출력한다.
print(dict1["B"])

#%%
# B키 값을 삭제한 후, 전체 dict를 출력한다.
del dict1["B"]
print(dict1)

#%%
# 다음 항목을 dict 로 생성하기
# 성인 - 10000, 청소년 - 7000, 아동 - 3000
price = {"성인": 10000, "청소년": 7000, "아동": 3000}
print(price)

#%%
# 위에서 선언한 dict에 소아 - 0 항목 추가 한 후 출력하기
price["소아"] = 0
print(price)

#%%
# 위에서 선언한 dict의 key 값만 출력하기
print(price.keys())

#%%
# 위에서 선언한 dict의 value 값만 출력하기
print(price.values())

#%%
# foods 라는 딕셔너리를 생성하고, 각 음식에 맞는 value를 출력하기
# foods = {
#   "떡볶이" : "튀김",
#   "짜장면" : "단무지",
#   "라면" : "김치",
#   "피자" : "피클",
#   "맥주" : "땅콩"
#   "치킨" : "맥주",
#   "삼겹살" : "상추"
# }
# 사용자에게 좋아하는 음식을 고르게 한 후, 그 음식과 궁합이 맞는 음식 출력하기
# 입력 값이 "끝" 이라는 글자가 들어오면 반복문 종료
# 키 값이 없는 음식을 고르면 "다른 음식을 선택해 주세요" 출력
foods = {
    "떡볶이": "튀김",
    "짜장면": "단무지",
    "라면": "김치",
    "피자": "피클",
    "맥주": "땅콩",
    "치킨": "맥주",
    "삼겹살": "상추",
}
key = ""
while True:
    key = input("좋아하는 음식을 입력하세요 : ")
    if key in foods.keys():

        print("이 음식과 맞는 음식은 %s 입니다." % (foods[key]))
    elif key == "끝":
        print("종료합니다.")
        break
    else:
        print("다른 음식을 선택해주세요")

#%%
# 선생님 ver
while True:
    food = input(str(list(foods.keys())) + " 중 좋아하는 것은?")
    if food in foods:
        print("%s의 궁합 음식은 %s 입니다." % (food, foods[food]))
    elif food == "끝":
        break
    else:
        print("다른 음식을 선택해 주세요")
