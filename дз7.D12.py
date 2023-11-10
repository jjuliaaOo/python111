sovm = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        sovm[city] = country

for i in range(int(input())):
    print(sovm[input()])
