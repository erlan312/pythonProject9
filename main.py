from decouple import config
from logic import play_game

if __name__ == "__main__":
    # Считывание конфигурации из settings.ini
    min_number = config("min_number", cast=int)
    max_number = config("max_number", cast=int)
    attempts = config("attempts", cast=int)
    initial_capital = config("starting_capital", cast=int)

    print("Добро пожаловать в игру 'Угадай число'!")
    print(f"Диапазон чисел: {min_number} - {max_number}")
    print(f"Количество попыток: {attempts}")
    print(f"Стартовый капитал: {initial_capital} рублей\n")

    play_game(min_number, max_number, attempts, initial_capital)

