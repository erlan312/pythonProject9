import random


def play_game(min_number, max_number, attempts, starting_capital):
    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"Диапазон чисел: от {min_number} до {max_number}")
    print(
        f"У вас есть {attempts} попыток и стартовый капитал: {starting_capital} монет.\n"
    )

    secret_number = random.randint(min_number, max_number)
    current_capital = starting_capital

    for attempt in range(1, attempts + 1):
        print(f"Попытка {attempt}/{attempts}")
        print(f"Ваш текущий капитал: {current_capital} монет")

        try:
            bet = int(input("Введите вашу ставку: "))
            if bet <= 0 or bet > current_capital:
                print("Неверная ставка. Попробуйте снова.")
                continue

            guess = int(input(f"Введите ваше число ({min_number}-{max_number}): "))

            if guess == secret_number:
                print(f"Поздравляем! Вы угадали число {secret_number}!")
                current_capital += bet
                print(f"Ваш капитал удвоен: {current_capital} монет.")
                break
            else:
                print("Неверно!")
                current_capital -= bet
                if current_capital <= 0:
                    print("Ваш капитал исчерпан. Игра окончена.")
                    break
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
            continue

    print(f"Игра завершена. Загаданное число: {secret_number}")
    print(f"Ваш окончательный капитал: {current_capital} монет")
