def sum_digits(s):
  sum = 0
  for i in s:
    try:
      b = int(i)
    except:
      b = 0
    sum += b
  return sum


print(sum_digits("Hello world!"))
print(sum_digits("He11o wor1d!"))
print(sum_digits("123"))
print(sum_digits("abc1efg2hij3"))
print(sum_digits("10 + 3 > -17.5"))
