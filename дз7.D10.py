n = int(input())
p = {}
for i in range(n):
    a1, a2 = input().split()
    p[a1] = a2
    p[a2] = a1
print(p[input()])
