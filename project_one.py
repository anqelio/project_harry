import random
try:
    sum_1=0
    sum_2=0
    wizard_one = input('Какой первый волшебник: ')
    wizard_two = input('Какой второй волшебник: ')
    duel = input('Кто победил в дуэли: ')
    duel_int = random.randint(3,10)
    riddle = duel = input('Кто разгадал загадку: ')
    riddle_int = random.randint(30,50)
    dexterity = input('Кто прошёл полосу препятствий: ')
    dexterity_int = 40
    honesty = input('Участник играл честно: ')
    honesty_int = 1
    help = input('Получал поддержку друзей: ')
    help_int = 1
    sum_1 += riddle_int
    sum_2 += help_int
    sum_first = duel_int + riddle_int + dexterity_int + honesty_int + help_int + sum_1
    sum_second = duel_int + riddle_int + dexterity_int + honesty_int + help_int + sum_2
    if duel and riddle and dexterity == wizard_one:
        print('За первое состязание он получил - ',duel_int)
        print('За второе состязание он получил - ',riddle_int)
        print('За третье состязание он получил - ',dexterity_int)
        print('За помощь друзей он получил - ', help_int,'и за честность - ',honesty_int)
        print(sum_first, ' - сумма баллов первого волшебника, он победил')
        print(sum_second, ' - сумма баллов второго волшебника, он проиграл')
    elif duel and riddle and dexterity == wizard_two:
        print('За первое состязание он получил - ', duel_int)
        print('За второе состязание он получил - ', riddle_int)
        print('За третье состязание он получил - ', dexterity_int)
        print('За помощь друзей он получил - ', help_int, 'и за честность - ', honesty_int)
        print(sum_second, ' - сумма баллов второго волшебника, он победил')
        print(sum_first, ' - сумма баллов первого волшебника, он проиграл')
    else:
        print('Состязания не было')
except ValueError as e:
    print('Некорректный ввод')