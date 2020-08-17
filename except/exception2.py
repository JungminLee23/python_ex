# 예외 처리
# try ~ except 제공
# try ~ except ~ else
# try ~ except ~ else ~ finally

# try 예외발생코드 except 예외처리코드
# try 예외발생코드 finally 예외와 상관없이 처리 코드
# try 예외발생코드 except 예외처리코드 else 예외가 안나는 경우 코드
# try 예외발생코드 except 예외처리코드
#                  else 예외가 안나는 경우 코드 finally 예외와 상관없이 처리 코드

#%% ValueError
name = ["Kim", "Park", "Lee"]
try:
    z = "Let"
    x = name.index(z)
    print("{} Found it! in name {}".format(z, x + 1))
except:
    print("오류발생")

#%% 더 정확하게
name = ["Kim", "Park", "Lee"]
try:
    z = "Let"
    x = name.index(z)
    print("{} Found it! in name {}".format(z, x + 1))
except ValueError:
    print("오류발생")


#%%
try:
    number_input = int(input("정수 입력 >> "))
    print("원 반지름 : ", number_input)
    print("원 둘레 : ", 2 * 3.14 * number_input)
    print("원 넓이 : ", 3.14 * number_input * number_input)
except:
    print("입력값을 확인해 주세요")

#%%
try:
    dict = {"name": "Kim", "age": 25, "city": "seoul"}
    print(dict["hobby"])  # KeyError : key 값 없는데 쓰면 이런 에러 남
except KeyError:
    print("찾으려는 키가 없습니다.")


#%%
name = ["Kim", "Park", "Lee"]
try:
    z = "Let"
    x = name.index(z)
    print("{} Found it! in name {}".format(z, x + 1))
except Exception:  # 어떤 에외가 나는지 모를 때
    print("오류발생")
else:  # 예외가 없을 때 실행
    print("종료")

#%%
name = ["Kim", "Park", "Lee"]
try:
    z = "Let"
    x = name.index(z)
    print("{} Found it! in name {}".format(z, x + 1))
except Exception:
    print("오류발생")
else:
    print("종료")
finally:
    print("무조건 실행")

#%%
try:
    print("Try")
finally:
    print("Finally")


#%%
name = ["Kim", "Park", "Lee"]
try:
    z = "Let"
    x = name.index(z)
    print("{} Found it! in name {}".format(z, x + 1))
except ValueError:
    pass
except IndexError:
    pass
except Exception:
    print("오류발생")

else:
    print("종료")
finally:
    print("무조건 실행")

#%%
try:
    number_input = int(input("정수 입력"))
except Exception as e:
    print(e)  # 에러메시지를 언어 자체가 제공하는걸로 출력

#%% 예외 직접 발생
try:
    a = "333"
    if a == "Kim":
        print("정답")
    else:
        raise ValueError  # ValueError 강제 발생시킴
except ValueError as v:
    print(v, "?")
else:
    print("종료")

#%%
numbers = [52, 273, 32, 103, 90, 1, 10, 275]

# 32라는 값이 있는지 확인한 후 위치 출력
# 10000 이라는 값이 있는지 확인한 후 위치 출력
# 값이 없는 경우 나올 수 있는 예외 처리하기
# 값이 없는 경우 출력문 => "리스트 내부에 없는 값입니다."

try:
    print("{}는 {} 위치에 있음".format(32, numbers.index(32)))
    print("{}는 {} 위치에 있음".format(10000, numbers.index(10000)))
except:
    print("리스트 내부에 없는 값입니다.")

# for num in numbers:
#     try:
#         if num == 32:
#             print("h")
#         elif num == 10000:
#             print("s")
#         else:
#             raise ValueError
#     except ValueError as v:
#         print("리스트 내부에 없는 값입니다.")

