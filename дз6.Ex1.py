def flexible_get(l, i):
    s = len(l)
    if i % 1 != 0:
        i = round(i)

    if i == s or i < 0 or i > s:
        print('')
    else:
        print(l[i])

flexible_get(['a', 'b', 'c'], 0)
flexible_get(['a', 'b', 'c'], 100)
flexible_get(['a', 'b', 'c'], 0.17)
