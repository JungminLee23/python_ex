# %d : 정수, %f : 실수, %s : 문자열, %c : 문자
print("%d" % 100)
print("%5d" % 100)
print("%05d" % 100)
print()
print("%5s" % "hi")
print("%s" % "hi")
print()
print("%-8.2f" % 123.21)
print("%8.2f" % 123.21)
print("%8.2f" % 123.2134567)

print()


print("I eat %d apples" % 3)
print("I eat %s apples" % "five")
number = 4
print("I eat %d apples" % number)
print("I eat", number, "apples")
print()

print("%d : %s" % (1, "홍길동"))

print("%d : %s - %0.2f" % (2, "김성호", 93.25))
print()

print("Test 1 : %c" % "t")
print()

# 비율 : 98%
print("비율 : %d%%" % 98)
