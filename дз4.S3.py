def make_description(name, age, grade, favourite_food, hobbies):
    a = 'Меня зовут {}, мне {} лет. Средняя оценка {}. Из еды очень люблю {}. Мои хобби: {}, {} и {}.'.format(name, age, grade, favourite_food, hobbies[0], hobbies[1], hobbies[2])
    return a


description = make_description('Ник', 18, 7.4, 'ролл Калифорния', ['бадминтон', 'бас-гитара', 'прокрастинация'])
print(description)
