# format() : python3 지원
#            대체 될 부분에 {} 표시를 해주면 된다.
print("{} and {}".format("You", "me"))
print()

print("{1} and {0}".format("You", "me"))
print()

print("{1} and {0} and {1}".format("You", "me"))
print()

print("I eat {0} apples".format(3))
print()

print("{var1} and {var2}".format(var1="You", var2="me"))
print()

print("I ate {} apples. so I was sick for {day} days".format(10, day=3))
print()

print("Test1 : {0:5d}, Price : {1: 4.2f}".format(776, 6534.123))
print()
