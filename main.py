from decouple import Config, RepositoryIni
from logic import play_game

config = Config(RepositoryIni("settings.ini"))


def main():

    min_number = config("min_number", cast=int)
    max_number = config("max_number", cast=int)
    attempts = config("attempts", cast=int)
    starting_capital = config("starting_capital", cast=int)

    play_game(min_number, max_number, attempts, starting_capital)


if __name__ == "__main__":
    main()
