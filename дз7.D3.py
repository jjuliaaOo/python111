posl = input('Введите последовательность нуклеотидов: ')
a1 = {'A': 'A', 'U': 'T', 'C': 'C', 'G': 'G'}
a2 = {'A': 'T', 'U': 'A', 'C': 'G', 'G': 'C'}

print(''.join(map(a1.get, posl)))
print(''.join(map(a2.get, posl)))
