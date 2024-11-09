"""1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.

2. Добавить сеттеры и геттеры к существующим атрибутам.

3. Добавить в класс Computer метод make_computations, в котором бы выполнялись арифметические вычисления с атрибутами объекта cpu и memory.

4. Создать класс Phone (телефон) с приватным полем sim_cards_list (список сим-карт)

5. Добавить сеттеры и геттеры к существующему атрибуту.

6. Добавить в класс Phone метод call с входящим параметром sim_card_number и call_to_number, в котором бы распечатывалась симуляция звонка в зависимости от переданного номера сим-карты (например: если при вызове метода передать число 1 и номер телефона, распечатывается текст “Идет звонок на номер +996 777 99 88 11” с сим-карты-1 - Beeline).

7. Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.

8. Добавить метод в класс SmartPhone use_gps с входящим параметром location, который бы распечатывал симуляцию построения маршрута до локации.

9. В каждом классе переопределить магический метод __str__ которые бы возвращали полную информацию об объекте.

10. Перезаписать все магические методы сравнения в классе Computer (6 шт.), для того чтоб можно было сравнивать между собой объекты, по атрибуту memory.

11. Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона

12. Распечатать информацию о созданных объектах.

13. Опробовать все возможные методы каждого объекта (например: use_gps, make_computations, call, а также магические методы).

14. В репозитории вашего проекта с дз удалить папки .idea, .venv и __pycache__

15. Создать файл .gitignore и вписать в него ненужные папки для репозитория"""

class Computer:
    def __init__(self, cpu, memory):
        self.cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        if value <= 0:
            raise ValueError("CPU должно быть положительным числом")
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        if value <= 0:
            raise ValueError("Memory должно быть положительным числом")
        self.__memory = value

    def make_computations(self):
        # Более реалистичное вычисление
        result = self.cpu + self.memory
        return f"Выполнение вычислений с CPU {self.cpu} и Memory {self.memory}: {result}"

    def __str__(self):
        return f"Computer(CPU: {self.cpu}, Memory: {self.memory})"

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory


class Phone:
    def __init__(self, sim_cards_list):
        if not all(isinstance(card, str) for card in sim_cards_list):
            raise ValueError("Список сим-карт должен содержать только строки с именами операторов.")
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.sim_cards_list):
            carrier = self.sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {carrier}")
        else:
            print("Некорректный номер сим-карты")

    def __str__(self):
        return f"Phone(SIM Cards: {', '.join(self.sim_cards_list)})"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до {location}")

    def __str__(self):
        return f"SmartPhone(CPU: {self.cpu}, Memory: {self.memory}, SIM Cards: {', '.join(self.sim_cards_list)})"


computer = Computer(cpu=3.5, memory=16)
phone = Phone(sim_cards_list=["Beeline", "Megafon"])
smartphone1 = SmartPhone(cpu=2.8, memory=8, sim_cards_list=["Beeline", "MTS"])
smartphone2 = SmartPhone(cpu=3.0, memory=12, sim_cards_list=["Megafon", "MTS"])

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

print(computer.make_computations())
phone.call(1, "+996 777 99 88 11")
smartphone1.use_gps("Манас")

print(computer == smartphone1)
print(computer < smartphone2)
print(smartphone1 < smartphone2)