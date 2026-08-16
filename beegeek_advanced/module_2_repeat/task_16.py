desicion_Timur = input()
desicion_Ruslan = input()

if desicion_Timur == desicion_Ruslan:
    print('ничья')
else:
    if desicion_Timur == 'камень':
        if desicion_Ruslan == 'ножницы' or desicion_Ruslan == 'ящерица':
            print('Тимур')
        else:
            print('Руслан')
    elif desicion_Timur == 'бумага':
        if desicion_Ruslan == 'камень' or desicion_Ruslan == 'Спок':
            print('Тимур')
        else:
            print('Руслан')
    elif desicion_Timur == 'ножницы':
        if desicion_Ruslan == 'бумага' or desicion_Ruslan == 'ящерица':
            print('Тимур')
        else:
            print('Руслан')
    elif desicion_Timur == 'ящерица':
        if desicion_Ruslan == 'бумага' or desicion_Ruslan == 'Спок':
            print('Тимур')
        else:
            print('Руслан')
    elif desicion_Timur == 'Спок':
        if desicion_Ruslan == 'ножницы' or desicion_Ruslan == 'камень':
            print('Тимур')
        else:
            print('Руслан')