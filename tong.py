import math
s=0
for i in range(100):
    a = input()
    s += a
    if a == 0:
        break
print(s)
n = s
for i in range(100):
    a = input()
    s = s - a
    if a == 0:
        break
print(n / 2 - s)