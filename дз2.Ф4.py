x = input('Введите имя: ')
def guess_gender(name):
    if name[len(name) - 1] == 'а' or name[len(name) - 1] == 'я':
        g = 'Ms'
    else:
        g = 'Mr'
    return g
    
print(guess_gender(x))
