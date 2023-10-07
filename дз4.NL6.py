numbers = [int(a) for a in input().split()]
x = set()
for i in numbers:
    if i in x:
        print('YES')
    else:
        print('NO')
        x.add(i)
