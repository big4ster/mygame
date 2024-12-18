import game

while True:
    print('''
Привет! Изучаю python и пробую писать мини игры
1. Камень - ножницы - бумага
2. Орел или решка
3. Угадай число
4. Выход
    ''')
    try:
        user_choise = int(input('Выберите пункт меню: '))
    except ValueError:
        print("Некорректный ввод! Введите число от 1 до 4.")
        continue
    if user_choise in [1, 2, 3, 4]:
        if user_choise == 1:
            game.stone_game()
        elif user_choise == 2:
            game.coin()
        elif user_choise == 3:
            game.guessNumber()
        elif user_choise == 4:
            print('До свидания')
            break

        else: print('Некорректный параметр')

