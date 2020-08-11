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
