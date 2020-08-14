#%%
import pi1

number1 = float(pi1.number_input())
# 여기서 float를 붙여주는 이유는 그냥 실행하면
# can't multiply sequence by non-int of type 'float'
# 이 에러가 뜨기 때문이다.

print("둘레 : ", pi1.get_circumference(number1))
print("면적 : ", pi1.get_circleArea(number1))
