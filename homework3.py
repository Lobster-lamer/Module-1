from consoleTextStyle import ConsoleTextStyle as CTS


class Person:
    def __init__(self, name:str,
                 age: int,
                 is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student


if __name__ == "__main__":
    Student1 = Person("Dude", 666, True)
    print(f"Hey, {CTS.color["PURPLE"]}{Student1.name}{CTS.color["WHITE"]}, you've been "
          f"{CTS.color["PURPLE"]}{Student1.age}{CTS.color["WHITE"]} yesterday!")
    Student1.age += 1
    print(f"Today your birthday! So, HAPPY {CTS.color["PURPLE"]}{Student1.age}{CTS.color["WHITE"]}th"
          f" BIRTHDAY, Hell's baron!")
    if Student1.is_student:
        print("Don't forget, that you're a student now, loser")
    else:
        print("Don't forget that you're must working here for eternity")