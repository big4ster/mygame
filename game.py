import random
def stone_game():
    stone = 0
    paper = 1
    scissors = 2
    gamelist = ['Камень', 'Бумага', 'Ножницы']
    usercount = 0
    pccount = 0
    while usercount < 3 and pccount < 3:
        try:
            user_choise = int(input('1.Камень \n2.Бумага \n3.Ножницы\nВведите цифру: ')) - 1
        except ValueError:
            print("Некорректный ввод! Введите число от 1 до 3.")
            continue
        pc_choice = random.randint(1, 3) - 1
        if user_choise in [0, 1, 2]:
            print(f'Игрок показал: {gamelist[user_choise]}')
            print(f'PC показал: {gamelist[pc_choice]}')
            if user_choise == pc_choice:
                print('Ничья! Перекидываем')
            elif user_choise == paper and pc_choice == stone or user_choise == scissors and pc_choice == paper or pc_choice == stone and user_choise == scissors:
                usercount += 1
                print(f'Игрок победил! {gamelist[user_choise]} бьет {gamelist[pc_choice]}')
            else:
                pccount += 1
                print(f'PC победил! {gamelist[pc_choice]} бьет {gamelist[user_choise]}')
            print(f'\n      Игровой счет')
            print(f'*** PC *** | *** Игрок ***')
            print(f'    {pccount}      |       {usercount}    ')
        else: print('Некорректный параметр')
    if usercount == 3:
        print('Игрок победил!')
    else: print('Машина выиграла!')

### Start Орел или решка
def coin():
    coin = 0
    coin_v = ['Орел', 'Решка']
    print('''     *****  ***  *****
    *** ~ Орел или решка ~ ***
         *****  ***  *****
    ''')
    print('для выхода нажмите "1"')
    while True:
        coin = input('Нажмите Enter для подбрасывания монеты!')
        if coin == '1':
            break
        elif coin != '':
            print('Ошибка! Нужно просто нажать \"Enter\"')
        else:
            coin_up = random.choice(coin_v)
            print(coin_up)
### End Орел или решка
#Угадай число
def guessNumber():
    number = random.randint(1, 100)

    count = 0
    print('Я загадал число от 1 до 100,\nпопробуй угадай, что это за число!')
    while True:
        count += 1
        mynumber = input('Введите ответ: ')
        if mynumber.isdigit():
            mynumber = int(mynumber)
            if mynumber > 100 or mynumber < 1:
                print('Введите число из диапазона от 1 до 100')
                continue
            difference = abs(number - mynumber)
            if mynumber == number:
                print('Поздравляю, вы угадали число!')
                print(f'Вы справились за {count} попыток')
                break

            if 1 <= difference <= 4:
                print('очень горячо')
            elif 5 <= difference <= 10:
                print('горячо')
            elif 11 <= difference <= 20:
                print('тепло')
            elif 21 <= difference:
                print('очень холодно')
        elif mynumber == 'q':
            break
        else:
            print('Ошибка! Введите число\nДля выхода отправьте \'q\'')
#End Угадай число