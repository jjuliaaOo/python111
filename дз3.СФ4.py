import math
f = open('C:/Users/admin/Desktop/СФ4.txt', 'r')
t=[]

for line in f:
  t.append(int(line))
n = len(t)

f1 = open('result.txt', 'w')

for i in range(n-1, 0, -1):
  f1.write(str(t[i]))
  f1.write('\n')

f1.close()
