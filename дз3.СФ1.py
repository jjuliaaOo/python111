import math
f = open("C:\Users\trety\OneDrive\Рабочий стол\СФ1.txt", 'r')
max = 0
t=[]

for line in f:
  t.append(int(line))
n = t[0]
for i in range(1, n+1):
  if t[i] >= max:
    max = t[i]
f.close()

a = abs(max)
j = 0
while a > 0:
  if a % 10 == 0:
    j = j + 1
  a = a // 10

f1 = open('result.txt', 'w')
f1.write(str(j))
f1.close()
