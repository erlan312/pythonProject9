"home work:"

"""
1. Создать класс Person с атрибутами full_name, age, is_married

2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке

3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который был бы словарем, где ключ это название урока, а значение - оценка.

4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам

5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience. 

6. Добавить в класс Teacher атрибут уровня класса base_salary.

7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к базовой зарплате прибавляется бонус 5% за каждый год опыта свыше 3-х лет.

8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату

9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики добавляются в список и список возвращается функцией как результат.

10. Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике с его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам.
""""""   
 _                                   _
| |_  ___ _ __  ___  __ __ _____ _ _| |__
| ' \/ _ \ '  \/ -_) \ V  V / _ \ '_| / /
|_||_\___/_|_|_\___|  \_/\_/\___/_| |_\_\

"""


import os


class Person:
    def __init__(self, fullName, age, isMarried=False) -> None:
        self.fullName = fullName
        self.age = age
        self.isMarried = isMarried
        self.yesNO = {"n": False, "no": False, "y": True, "yes": True}

    def introduceMyself(self):
        if self.yesNO.get(str(self.isMarried).lower(), False):
            return f"Hello,\nmy name is\n{'-' * 20}\n{self.fullName}\nI'm {self.age} years old\nI'm married"
        else:
            return f"Hello,\nmy name is\n{'-' * 20}\n{self.fullName}\nI'm {self.age} years old\nI'm single"

    def __str__(self) -> str:
        return self.introduceMyself()


class Students(Person):
    def __init__(self, fullName, age, marks=None, isMarried=False) -> None:
        super().__init__(fullName, age, isMarried)
        self.marks = marks if marks else {}

    def showMarks(self):
        return "\n".join(
            f"subject: {key}, mark: {value}" for key, value in self.marks.items()
        )

    def infoStudents(self):
        return f"{super().__str__()}"

    def NormalBall(self):
        os.system("cls" if os.name == 'nt' else "clear")  # Для очистки экрана в зависимости от ОС
        if self.marks:
            return f"{self.fullName} normal ball is {sum(self.marks.values()) / len(self.marks):.2f}"
        return f"{self.fullName} has no marks."

    def __str__(self) -> str:
        os.system("cls" if os.name == 'nt' else "clear")
        return super().__str__() + f"\n{'-' * 30}" + f"\n{self.showMarks()}"


class Teachers(Person):
    def __init__(self, fullName, age, experience, baseSalary, isMarried=False) -> None:
        super().__init__(fullName, age, isMarried)
        self.experience = experience
        self.baseSalary = baseSalary
        self.bonuses = 0

    def Bonus(self):
        bonusYears = max(0, self.experience - 3)
        bonus = self.baseSalary * 0.05 * bonusYears
        self.bonuses += bonus
        return self.bonuses

    def __str__(self) -> str:
        return (
            super().__str__()
            + f"\nexperience: {self.experience} years\nbase salary: {self.baseSalary}\nbonus: {self.bonuses:.2f}"
        )


gojoSatoru = Teachers("Gojo Satoru", 28, 5, 1000)
gojoSatoru.Bonus()
gojoSatoru.Bonus()
gojoSatoru.Bonus()

print(gojoSatoru)

def create_students():
    students = []
    student1 = Students("Erlan", 20, {"Math": 4, "Physics": 5, "Chemistry": 3})
    student2 = Students("Aktan", 19, {"Math": 5, "Biology": 4})
    student3 = Students("Aziz", 21, {"Math": 3, "Geography": 4, "History": 5})

    students.extend([student1, student2, student3])

    return students

students_list = create_students()
for student in students_list:
    print(student)
    print(student.NormalBall())
    print()