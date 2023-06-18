def pal(abc):
    if abc == abc[::-1]:
        print(bool(1))
    else:
        print(bool(0))

pal(str(input('Введите слово: ')).lower().replace(' ', ''))