from random import randint, choice

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f"{self.__name} health: {self.health} damage: {self.damage}"


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    @property
    def defence(self):
        return self.__defence

    def __str__(self):
        return "BOSS " + super().__str__() + f" defence: {self.__defence}"


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "REVIVE")

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health == 0:
                print(
                    f"Witcher {self.name} revived {hero.name} by sacrificing himself."
                )
                hero.health = 100
                self.health = 0
                break


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "BOOST")

    def apply_super_power(self, boss, heroes):
        boost_amount = randint(5, 15)
        for hero in heroes:
            if hero != self and hero.health > 0:
                hero.damage += boost_amount
        print(f"Magic {self.name} boosted heroes by {boost_amount}.")


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "STEAL_HEALTH")

    def apply_super_power(self, boss, heroes):
        if round_number % 2 == 0:
            stolen_health = randint(10, 30)
            boss.health -= stolen_health
            target_hero = choice([hero for hero in heroes if hero.health > 0])
            target_hero.health += stolen_health
            print(
                f"Hacker {self.name} stole {stolen_health} health from boss and gave it to {target_hero.name}."
            )


class Avrora(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "INVISIBILITY")
        self.__is_invisible = False
        self.__invisible_rounds = 0
        self.__used_invisibility = False

    def apply_super_power(self, boss, heroes):
        if not self.__used_invisibility:
            self.__is_invisible = True
            self.__invisible_rounds = 2
            self.__used_invisibility = True
            print(f"Avrora {self.name} became invisible for 2 rounds.")
        elif self.__invisible_rounds > 0:
            self.__invisible_rounds -= 1
            if self.__invisible_rounds == 0:
                self.__is_invisible = False
                print(f"Avrora {self.name} is now visible again.")

    def attack(self, boss):
        if not self.__is_invisible:
            super().attack(boss)

    @property
    def health(self):
        return super().health


    @health.setter
    def health(self, value):
        if not self.__is_invisible:
            super(Avrora, type(self)).health.fset(self, value)


class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "STUN")

    def apply_super_power(self, boss, heroes):
        if randint(1, 5) == 1:
            boss.damage = 0
            print(f"Thor {self.name} stunned the boss!")


round_number = 0


def show_statistics(boss, heroes):
    print(f"ROUND - {round_number} ------------")
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print("Heroes won!!!")
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print("Boss won!!!")
        return True
    return False


def start_game():
    boss = Boss(name="Dragon", health=1000, damage=50)
    witcher = Witcher(name="Geralt", health=200, damage=0)
    magic = Magic(name="Merlin", health=290, damage=10)
    hacker = Hacker(name="Neo", health=250, damage=5)
    avrora = Avrora(name="Avrora", health=240, damage=15)
    thor = Thor(name="Thor", health=270, damage=20)
    heroes_list = [witcher, magic, hacker, avrora, thor]

    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()