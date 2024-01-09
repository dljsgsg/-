# 1
a = int(input("write first number"))
b = int(input("write second number"))
for i in range(a, b + 1):
    print(i)

# 2
a = int(input("write first number"))
b = int(input("write second number"))
for i in range(a, b + 1):
    if (i % 2 != 0):
        print(i)
        # 3
a = int(input("write first number"))
b = int(input("write second number"))
for i in range(a, b + 1):
    if (i % 2 == 0):
        print(i)
        # 4
a = int(input("write first number"))
b = int(input("write second number"))
while b > a:
    print(b)
    b -= 1
#5
a = int(input("write first number"))
b = int(input("write second number"))
if a > b:
    for i in range(b, a + 1):
        if i % 2 != 0:
            print(i)
else:
    for i in range(a, b + 1):
        if i % 2 != 0:
            print(i)




