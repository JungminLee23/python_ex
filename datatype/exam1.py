#%%
# q1) A 학급에 총 10명의 학생이 있다.이 학생들의 중간고사 점수는
#     다음과 같다. A 학급의 평균을 구하시오
#     70, 60, 55, 75, 95, 90, 80, 85, 100
#     [조건] 중간고사 점수를 리스트로 생성하고 평균 구하기

# a_list = [70, 60, 55, 75, 95, 90, 80, 85, 100]
# avg = 0
# for i in range(len(a_list)):
#     avg += a_list[i - 1]
# print(avg / len(a_list))

a_list = [70, 60, 55, 75, 95, 90, 80, 85, 100]
print("A 학급 평균 : %.2f" % (sum(a_list) / len(a_list)))

#%%
# q2) 아래 문자열의 길이를 구하시오.
#     str1 = "dk2jddlfjalfjalfnelfnlsdflbjgaeijrfwjdfufdidjck"
str1 = "dk2jddlfjalfjalfnelfnlsdflbjgaeijrfwjdfufdidjck"
print(len(str1))

#%%
# q3) 화면에 * 기호 100개를 표시하기
for i in range(10):
    print("*" * 10)


#%%
# q4) 문자열 30을 각각 정수형, 실수형, 문자형으로 변경해서 출력하기
str1 = "30"
print(str1)
print("정수형 : ", int(str1))
print("실수형 : ", float(str1))
print("문자형 : ", str(str1))

#%%
# q5) 문자열 Niceman 에서 man 문자열만 출력하기
str = "Niceman"
print(str[-3:])


#%%
# q6) 문자열 http://www.daum.net 에서 http:// 제거하고 출력하기
str1 = "http://www.daum.net"
print(str1.split("//")[1])

# print(str1.replace("http://", ""))

#%%
# q7) 문자열 abcdefghijklmn 에서 슬라이싱을 이용해 "cde" 만 출력하기
str = "abcdefghijklmn"
print(str[2:5])

#%%
# q8) 다음 리스트에서 "Apple" 항목만 삭제하고 출력하기
#     ["Banana", "Apple", "Orange", "Grape"]

list1 = ["Banana", "Apple", "Orange", "Grape"]
list1.remove("Apple")  # del list1[1]
print(list1)

#%%
# q9) 다음 리스트에서 '정' 글자만 제외하고 출력하기
#     ["갑", "을", "병", "정", "경"]
list1 = ["갑", "을", "병", "정", "경"]

for str in list1:
    if str != "정":
        print(str, end=" ")

print("\n~~~~~ 컴프리핸션 ~~~~~~~\n")
list2_1 = [str for str in list1 if str != "정"]
print(list2_1)

#%%
# q10) 다음 리스트에서 5글자 이상의 단어만 출력하기
#      ["nice", "study", "python", "anaconda", "!"]
list1 = ["nice", "study", "python", "anaconda", "!"]
# 1번 방법
for i in range(len(list1)):
    if len(list1[i]) >= 5:
        print(list1[i])

# 그냥 for문을 str로 바로
for str in list1:
    if len(str) >= 5:
        print(str, end=" ")

print("\n~~~~~ 컴프리핸션 ~~~~~~~\n")
list2_1 = [str for str in list1 if len(str) >= 5]
print(list2_1)

#%%
# q11) 아래 리스트에서 소문자만 출력하기
#      ["A", "b", "c", "D", "e", "F", "G", "h"]
list1 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for i in range(len(list1)):
    if list1[i].islower():
        print(list1[i])

print("\n 컴프리핸션")
list2_1 = [str for str in list1 if str.islower()]
print(list2_1)

#%%
# q12) 아래 리스트에서 소문자는 대문자로 대문자는 소문자로 출력하기
#      ["A", "b", "c", "D", "e", "F", "G", "h"]
list1 = ["A", "b", "c", "D", "e", "F", "G", "h"]
list2 = []
for i in range(len(list1)):
    if list1[i].islower():
        str = list1[i].upper()
        list2.append(str)
    else:
        str = list1[i].lower()
        list2.append(str)
print(list2)

#%%
# q13) 주차장 프로그램 작성하기
#
car_list = ["A", "B", "C", "D", "E"]
car_num = 0
parking_list = []
select = -1
while select != 3:
    select = int(input("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 : "))
    if select == 1:
        if car_num >= 5:
            print("주차장 꽉 참")
        else:
            parking_list.append(car_list[car_num])
            print(car_list[car_num], "자동차 들어감. 주차장 상태 ==> ", parking_list)
            car_num += 1
    elif select == 2:
        if car_num <= 0:
            print("빠져나갈 자동차가 없음")
        else:
            parking_list.pop()
            print(car_list[car_num - 1], "자동차 나감. 주차장 상태 ==> ", parking_list)
            car_num -= 1
    elif select == 3:
        print("프로그램 종료")

print("The end")

#%%
# 문자 -> 아스키 코드
paking_lot = []
top, car_name = 0, "A"
print("문자 -> 아스키코드 : ", ord("A"))

# 아스키 코드 -> 문자
print(chr(65))

#%%
parking_lot = []
top, car_name = 0, "A"

while True:
    no = int(input("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 : "))

    if no <= 3:
        if no == 1:
            if top >= 5:
                print("주차장 꽉 찼음")
            else:
                parking_lot.append(car_name)
                print("%c 자동차 들어감. 주차장 상태 ==> %s" % (car_name, parking_lot))
                top += 1
                car_name = chr(ord(car_name) + 1)

        elif no == 2:
            if top <= 0:
                parking_lot.pop()
                print("%c 자동차 나감. 주차장 상태 ==> %s" % (car_name, parking_lot))
            else:
                print("빠져 나갈 자동차가 없음")
        else:
            print("프로그램 종료")
            break
    else:
        print("번호를 확인해 주세요")

