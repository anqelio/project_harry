try:
    harry_one = input('У Гарри есть родители? ')
    harry_two = input('Они любят его? ')
    hermiona_one = input('У Гермионы есть успехи в учебе? ')
    hermiona_two = input('Её друзья рядом? ')
    nevill_one = input('У Невилла Долгопупса есть уверенность? ')
    nevill_two = input('Есть поддержка друзей? ')
    fred_one = input('Есть у Фреда и Джоржда Уизли смех? ')
    fred_two = input('Есть радость? ')
    if harry_one == 'да' and harry_two == 'да':
        print('Перед зеркалом Гарри Поттер')
    elif hermiona_one == 'да' or hermiona_two == 'да':
        print('Перед зеркалом Гермиона')
    elif nevill_one == 'да' or nevill_two == 'да':
        print('Перед зеркалом Невиллл Долгопупс')
    elif fred_one == 'да' or fred_two == 'да':
        print('Перед зеркалом Фред и Джордж Уизли')
except ValueError as e:
    print('Некорректный ввод')