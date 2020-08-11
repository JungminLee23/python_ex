# 기본 입출력
# 기본출력 - print()
# 기본입력 - input()

# 파일 입출력
# txt 파일, json 파일, xml 파일
# open("파일경로", "모드", encoding = "")
# 모드 : r(read), w(write), a(append)
# 파일 출력 : write(), writelines()
# 파일 입력 : read(), readline(), readlines()

#%% 파일 생성
f = open("../resource/test1.txt", "w")
f.close()

#%% 파일 생성 후 쓰기
# f = open("../resource/test1.txt", "w", encoding="utf-8")
# print(dir(f))

# f.write("abdfslfaefndsklfnls\n")
# f.write("안녕하세요")
# f.close()

with open("../resource/test1.txt", "w", encoding="utf-8") as f:
    f.write("abdfslfaefndsklfnls\n")
    f.write("안녕하세요")

#%% 1~10까지 파일에 쓰기 파일 이름은 number

# f = open("../resource/number.txt", "w", encoding="utf-8")
# for i in range(1, 11):
#     f.write("%d " % (i))
# f.close()

with open("../resource/number.txt", "w", encoding="utf-8") as f:
    for i in range(1, 11):
        f.write("%d " % (i))


#%%
# 기존 파일에 내용 덧붙이기
f = open("../resource/test1.txt", "a", encoding="utf-8")
for i in range(1, 11):
    f.write("반갑습니다. \n")
f.close()

#%% with : close()를 자동으로 해줌
# with open("경로", "모드", encoding ="") as f:
# 해야할 작업들


#%% 리스트를 파일에 쓰기
with open("../resource/list1.txt", "w", encoding="utf-8") as f:
    list1 = ["홍길동", "김길동", "고양이"]
    # for i in list1:
    #     f.write(i + "\n")
    f.writelines(list1)

#%% dict 쓰기
with open("../resource/dict1.txt", "w", encoding="utf-8") as f:
    dict1 = {"name": "hong", "age": 24, "addr": "서울"}
    f.writelines(dict1)
    for k, v in dict1.items():
        f.writelines("{} : {} \n".format(k, v))

#%% 1000명의 이름과 키, 몸무게를 랜덤하게 생성한 후 쓰기
import random

names = list("가거고구기나너노누니다라마바사아자차카타파하")

with open("../resource/info.txt", "w", encoding="utf-8") as f:
    for i in range(1000):
        # 랜덤 이름 생성
        name = random.choice(names) + random.choice(names)
        # 랜덤 키 생성
        height = random.randrange(150, 190)
        # 랜덤 몸무게 생성
        weight = random.randrange(40, 100)
        f.writelines("{}, {}, {}\n".format(name, height, weight))
