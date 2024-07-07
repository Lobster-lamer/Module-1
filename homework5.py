import datetime
from consoleTextStyle import ConsoleTextStyle as CTS


def str_to_date(date_in_str: str) -> datetime.date:
    date_list = date_in_str.split(".")
    try:
        date_list = list(map(int, date_list))
    except ValueError:
        print("There is string in date")
    try:
        return datetime.date(date_list[0], date_list[1], date_list[2])
    except ValueError:
        print("invalid date")


class RoomRenter:
    def __init__(self, name: str,
                 room_number: int,
                 check_in_date: datetime.date):
        self.name = name
        self.room_number = room_number
        self.check_in_date = check_in_date

    def __str__(self):
        return CTS.colorful_str(f"Имя: {self.name},"
                          f" номер комнаты: {self.room_number},"
                          f" заехал: {self.check_in_date}", "BLUE")


if __name__ == "__main__":
    immutable_var = "Dude", 12, str_to_date("2024.07.10"), 7
    print("Есть у нас должник надо в старой структуре записи наших постояльцев изменить ему имя")
    try:
        immutable_var[0] = "Должник"
    except TypeError:
        CTS.colorful_text("Ну нельзя менять неизменняемое содержимое tuple объектов, ну ты шо?",
                          "RED")
    print("Вот так вот!(")

    immutable_var = (RoomRenter("Dude", 1, str_to_date("2024.07.10")),
                     RoomRenter("Another dude", 2, str_to_date("2024.07.11")))
    print("\nТыак, мы поменяли структуру записи постояльцев, ща заменим)")
    immutable_var[1].name = "Должник"
    for room_renter in immutable_var:
        print(room_renter)
    print("Чётко) О, к нам новый постоялец, добавим его... А как?(\nЛадно, видно надо опять менять структуру(\n")

    print("Тыак, структуру поменяли")
    mutable_var: list = list(immutable_var)
    for room_renter in mutable_var:
        print(room_renter)
    print("Вроде работает, добавим нового постояльца")
    mutable_var.append(RoomRenter("Zergling", 3, str_to_date("2024.07.12")))
    print(mutable_var[-1])
    print("Каеф) Всё работает) Имя у него какое-то странное...")

    print("\nЗараза, он всех сожрал. Надо всех выписать( И с самим зерглингом что-то сделать. Как его вообще заселили?!")
    mutable_var.remove(mutable_var[0])
    mutable_var.remove(mutable_var[0])
    for room_renter in mutable_var:
        print(room_renter)