from sum1 import sum

# from sum1 import sum, safe_sum 이렇게 써야 아래 주석 처리 구문 사용 가능
print(sum(50, 55))
# sum1 모듈안에서 sum 함수만 사용하겠다고 선언했기 때문에 아래 구문 실행 불가
# print(sum1.safe_sum(50, "55"))
# print(sum1.safe_sum(50, 60))

