# 파이썬 데이터 타입
# 정수형
# 문자형 : '', "" 둘 다 허용 , '''...''', """...""" 둘 다 허용
#%%
a = "Life is too short, You need Python"
a = """\
    여러줄 표현 시 사용\
    Life is too short, You need Python
"""
print(a)

#%% 문자열 응용
# + : 결합
print("Python " + "is Fun")

# * : 복제
print("파이썬" * 2)

#%%
print("*" * 50)
print("My Program")
print("*" * 50)

#%% 인덱싱
str1 = "Life is too short"
print(str1[3])  # 기준 : 왼쪽
print(str1[-3])  # 기준 : 오른쪽

#%% 슬라이싱 - 중요도 높음
str1 = "Life is too short"
print("str1[0:4] : ", str1[0:4])  # 4 포함 안됨

print("str1[5:7] : ", str1[5:7])  # 7 포함 안됨

print("str1[8:11] : ", str1[8:11])  # 11 포함 안됨

print("str1[0:-4] : ", str1[0:-4])  # -4 포함 안됨. 뒤에서부터 셈

print("str1[:] : ", str1[:])  # 시작, 끝 값 없음(전체 문자열)

print("str1[:17] : ", str1[:15])  # 시작 값 없음

print("str1[3:] : ", str1[3:])  # 끝 값 없음

#%%
# 문자열 길이 len()...
print(len(str1))

#%%
str2 = "20200804Rainny"
# 출력문 20200804
print(str2[:8])

# Rainny만 나오게
print(str2[8:])

# 2020-08-04
year = str2[:4]
month = str2[4:6]
day = str2[6:8]
print(year, month, day, sep="-")

#%%
# 주민등록번호에서 8번째 자리 숫자를 사용해서
# 남자, 여자 판별하기
# 1, 3 -> 남 / 2, 4 -> 여

str1 = "901205-3234567"

# if str1[7:8] == "1" or str1[7:8] == "3":
#     print("남")
# else:
#     print("여")

if int(str1[7]) % 2 == 1:
    print("남")
else:
    print("여")
# %%
# 각 문자의 끝에 $ 찍기
str1 = "대한민국"  # 대$한$민$국$ 나오도록
str2 = ""
for i in range(4):
    str2 += str1[i] + "$"
print(str2)

#%%
# 숫자를 입력 받아 해당 숫자만큼 하트 모양 찍기
input1 = input("출력할 숫자들 입력")
print(input1)
sli = ""
i = 0
while i != len(input1):
    sli = input1[i]
    for j in range(int(sli)):
        print("★", end=" ")
    print()
    i += 1

#%%
# 쌤 방식
# 문자의 길이 => 반복 횟수
str3 = input("숫자를 입력하세요 : ")

# 만약 12543이면  5개 => ★ 5번 출력
for i in range(0, len(str3)):
    for s in range(0, int(str3[i])):
        print("★", end=" ")
    print()

#%%
# 문자열 관련 함수 - 1. count : 문자열에 포함 된 특정 문자열의 개수
str1 = "hobby"
print("str1에 포함 된 b 문자열 개수 : ", str1.count("b"))

#%%
# 문자열 관련 함수 - 2. find : 문자열 찾기
str1 = "Python is best Choice"
print("b가 시작되는 첫 번째 위치 : ", str1.find("b"))
print("o가 시작되는 첫 번째 위치 : ", str1.find("o"))
print("k가 시작되는 첫 번째 위치 : ", str1.find("k"))  # -1을 돌려줌(못찾는 경우)

print("6번째 이후로 o가 시작되는 위치 : ", str1.find("o", 6))

#%%
# 문자열 관련 함수 - 3. index : 문자열 찾기
print("b가 시작되는 첫 번째 위치 : ", str1.index("b"))
print("o가 시작되는 첫 번째 위치 : ", str1.index("o"))
print("k가 시작되는 첫 번째 위치 : ", str1.index("k"))  # 여기서 에러 남 못찾으면 에러 발생

#%%
# 문자열 관련 함수 - 4. startwith / endwith : 문자열 찾기
# 특정 문자열로 시작 혹은 끝나는지 확인

str1 = "Python is easy programming"
print(str1.startswith("P"))  # True
print(str1.endswith("h"))  # False

#%%
# 문자열 관련 함수 - 5. join : 문자열
a = ","
print("a", "b", "c", "d", "e", sep=a)  # 원래 이렇게 써야하는데
print("문자열 연결", a.join("abcde"))  # join을 쓰면 이렇게 된다.

#%%
# 문자열 관련 함수 - 6. upper / lower : 대문자 / 소문자
str1 = "abcde"
print("대문자로 변경 : ", str1.upper())
str2 = "ABCDE"
print("소문자로 변경 : ", str1.lower())

#%%
# 문자열 관련 함수 - 7. swapcase : 대소문자를 상호 변환
str1 = "Python Is Easy"
print(str1.swapcase())

#%%
# 문자열 관련 함수 - 8. title : 앞 문자를 대문자로 바꿔줌
str1 = "python is easy"
print(str1.title())

#%%
# 문자열 관련 함수 - 9. strip / lstrip / rstrip : 공백제거
str1 = "         hi"
print(str1.strip())
print(str1.lstrip())
str1 = "hi            "
print(str1.strip())
print(str1.rstrip())

str1 = "     hi           "
print(str1.strip())

#%%
# 문자열 관련 함수 - 10. replace : 문자열 바꾸기
str1 = "Life is too short"
print(str1.replace("Life", "Your leg"))

#%%
# 문자열 관련 함수 - 11. split : 특정 문자로 문자열 나누기
str1 = "Life is too short"
print(str1.split())  # 기준을 안줬을 때 공백이 기준
# ['Life', 'is', 'too', 'short'] (리스트)
print()

str1 = "Life:is:too:short"
print(str1.split(":"))  # ':'을 기준으로 자름
print()

print("".join(str1))
print()

str1 = "Life\nis\ntoo\nshort"
print(str1.splitlines())  # '\n'를 기준으로 자름

print("".join(str1.splitlines()))
# 리스트의 결과를 문자열로 변경

print()

#%%
# 문자열 관련 함수 - 12. center/ljust/rjust/zfill - 문자열 정렬

str1 = "파이썬"
print(str1.center(10, "*"))
print(str1.ljust(10, "*"))
print(str1.rjust(10, "*"))
print(str1.zfill(10))

#%%
# 문자열 관련 함수 - 13. 문자열 구성 파악
print("1234".isdigit())
print("abcd".isalpha())
print("abc123".isalnum())
print("abcd".islower())
print("ABCD".isupper())
print("     ".isspace())

#%%
# 대문자는 소문자로, 소문자는 대문자로 변경 후 출력하기
# name = "KennRY" swapcase() 사용하지 말기
name = "KennRY"
for i in name:
    if i.islower():
        print(i.upper(), end=" ")
    else:
        print(i.lower(), end=" ")

#%%
# 사용자로부터 년/월/일 형태의 데이터를 입력받고 10년 후의
# 날짜를 출력하여 보여주기
# 입력값이 2020/08/05 => 2030년 08월 05일
# date1 = input("날짜입력(년/월/일) 형태 : ")

# pos = date1.find("/")
# year = int(date1[0:pos]) + 10
# print("입력한 날짜의 10년 후는 %s" % (str(year) + "년" + date1[5:7] + "월" + date1[8:] + "일"))

# 리스트 형태일 때
date1 = input("날짜입력(년/월/일) 형태 : ")
date1 = date1.split("/")  # ['2020', '08', '05']
print(
    "입력한 날짜의 10년 후는 %s"
    % (str(int(date1[0]) + 10) + "년" + date1[1] + "월" + date1[2] + "일")
)


#%%
# 웹 사이트 주소를 이용한 비밀번호 생성하기
# https://naver.com => nav51!
# 규칙 1 : https:// 이부분은 제외
# 규칙 2 : 처음 만나는 점(.) 이후의 부분은 제외 => com 제외
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e' 개수
#           + "!" 구성

url = "https://naver.com"
url = url.replace("https://", "")
url = url[: url.find(".")]
e_count = url.count("e")

password = url[:3] + str(len(url)) + str(e_count) + "!"
print(password)

