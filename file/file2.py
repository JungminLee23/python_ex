# 파일 읽기
#%%
f = open("../resource/test1.txt", "r", encoding="utf-8")
print(f.read())
f.close()

#%%
with open("../resource/test1.txt", "r", encoding="utf-8") as f:
    print(f.read())

#%%
with open("../resource/review.txt", "r", encoding="utf-8") as f:
    for c in f:
        print(c.strip())

#%% readline() : 줄 단위로 읽어오기
with open("../resource/review.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    while line:
        print(line, end="")
        line = f.readline()

#%% readlines()
with open("../resource/review.txt", "r", encoding="utf-8") as f:
    content = f.readlines()
    for c in content:
        print(c, end="")

#%% score.txt 읽어와서 평균을 구한 뒤 화면에 출력
with open("../resource/score.txt", "r", encoding="utf-8") as f:
    score = []
    for num in f:
        score.append(int(num))

print("평균 : ", sum(score) / len(score))
print("평균 : %.2f" % (sum(score) / len(score)))

#%% score.txt 읽어와서 총 합과 평균을 구한 후 구한 결과 값을 result.txt에 쓰기
# 총합 : 790
# 평균 : 79.00

with open("../resource/score.txt", "r", encoding="utf-8") as f:
    score = []
    for num in f:
        score.append(int(num))

with open("../resource/result.txt", "w", encoding="utf-8") as f:
    f.write("총합 : %d \n" % (sum(score)))
    f.write("평균 : %.2f" % ((sum(score) / len(score))))


#%% 특정 경로에 파일을 읽어서 사용자가 지정하는 폴더로 복사
import os  # 운영체제와 관련된 기능을 가진 모듈(폴더 생성, 폴더 목록보기)

content = ""
fName = ""
fPath = "D:/pythonsource/resource"
# 사용자에게 읽을 파일을 입력받고 저장할 폴더와 이름도 입력받기.
fName = input("읽을 파일 이름 입력")
savePath = input("저장할 폴더 경로와 이름 입력")

fullFile = fPath + "/" + fName
# 파일이 존재하면 읽은 후 사용자가 입력한 저장 폴더에 읽은
if os.path.exists(fullFile):
    with open(fullFile, "r", encoding="utf-8") as f:
        for i in f.readlines():
            content += i
    # 파일을 저장하기
    with open(savePath, "w", encoding="utf-8") as r:
        r.write(content)

# os.path.exists("D:/temp/test.txt")  # 이 경로에 그 파일이 존재하는지 여부 물어봄 True/False

#%%
# 선생님 방법
import os  # 운영체제와 관련된 기능을 가진 모듈(폴더 생성, 폴더 목록보기)

content = ""
fName = ""
fName = input("일어올 파일명을 입력해주세요.")
if os.path.exists(fName):
    with open(fName, "r", encoding="utf-8") as inFp:
        content = inFp.read()

    oName = input("저장할 폴더와 이름을 입력하세요 ")
    with open(oName, "w", encoding="utf-8") as outFp:
        outFp.writelines(content)
else:
    print("%s 파일이 없습니다." % fName)

#%% info.txt 파일을 읽어 BMI 지수를 계산한 후 화면에 출력하기
# bmi 지수 계산 = 체중 / (키/100)**2
# bmi 지수가 25 이상이면 과체중
#            18.5 이상이면 정상체중
#                          저체중

# 출력결과
# 이름 : 가나
# 몸무게 : 44
# 키 : 150
# BMI : 12.~~
# 결과 : 저체중

import os

content = ""
list_hu = []
with open("../resource/info.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    while line:
        list1 = line.split(", ")
        list1[2] = list1[2].strip("\n")
        list_hu.append(list1)
        line = f.readline()


list_bmi = []
with open("../resource/save/bmi.txt", "w", encoding="utf-8") as w:
    for i in list_hu:
        bmi = int(i[2]) / (int(i[1]) / 100) ** 2
        if bmi >= 25:
            i[2] = "과체중"
        elif bmi >= 18.5:
            i[2] = "정상체중"
        else:
            i[2] = "저체중"
        i[1] = str(bmi)
        w.writelines(i)
        w.write("\n")
# ????
#%% 쌤방법
with open("../resource/info.txt", "r", encoding="utf-8") as f:
    for info in f:
        name, weight, height = info.strip().split(", ")
        result = ""
        bmi = int(weight) / (int(height) / 100 ** 2)
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        print(
            "\n".join(["이름 : {}", "몸무게 : {}", "키 : {}", "BMI : {}", "결과 : {}"]).format(
                name, weight, height, bmi, result
            )
        )

#%% 이진 파일
# b => binary 파일
data = ""
try:
    with open("c:/windows/notepad.exe", "rb") as f1:
        data = f1.read()

    with open("c:/temp/notepad.exe", "wb") as f2:
        f2.write(data)
except:
    print("복사 실패")

