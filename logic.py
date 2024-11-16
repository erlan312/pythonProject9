
import random
from decouple import config

def play_game(min_number, max_number, attempts, initial_capital):
    capital = initial_capital
    print(f"Начальный капитал: {capital} рублей.")

    for attempt in range(1, attempts + 1):
        print(f"\nПопытка {attempt} из {attempts}")
        bet = int(input("Введите ставку: "))
        if bet > capital:
            print("Ставка не может быть больше текущего капитала!")
            continue

        guess = int(input(f"Угадайте число от {min_number} до {max_number}: "))
        number = random.randint(min_number, max_number)
        print(f"Загаданное число: {number}")

        if guess == number:
            print("Вы угадали! Ставка удваивается.")
            capital += bet
        else:
            print("Вы не угадали! Ставка проиграна.")
            capital -= bet

        print(f"Текущий капитал: {capital} рублей.")
        if capital <= 0:
            print("Капитал закончился. Игра завершена.")
            break

    if capital > 0:
        print(f"Игра окончена. Ваш финальный капитал: {capital} рублей.")
    else:
        print("Вы проиграли все деньги.")