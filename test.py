n = int(input("Type kol: "))

a = 0
b = 1

for i in range(n):
    print("%d %d" % (i + 1, b))
    a, b = b, a + b