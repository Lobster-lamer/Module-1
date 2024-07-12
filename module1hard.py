from consoleTextStyle import ConsoleTextStyle as CTS


print("Блин, преподы не хотят говорить, что у меня по оценкам и что у меня выходит в четверти, что делать?")
CTS.colorful_text("ТИММИ!!!", CTS.Color.YELLOW)
print("Точно! Тимми, ты прав! Давай взломаем их базу данных!")
CTS.colorful_text("ТИММИ!!!\n", CTS.Color.YELLOW)

grades = [[2, 2, 3, 3, 2, 2], [5, 4, 4, 5, 5], [3, 3, 4, 5], [5, 5, 5, 5, 4, 5, 5]]
students = {"Валера", "Ибрагим", "TIMMY!", "Иосиф Висарионович Черномырдин"}

CTS.colorful_text(f"Оценки учеников в алфавитном порядке: {grades}\n"
                  f"Ученики: {students}", CTS.Color.BLUE)
print("\nЧТО ЭТО ЗА ХРЕНЬ?!")
CTS.colorful_text("ТИММИ!", CTS.Color.YELLOW)
print("Теперь понятно, почему преподы молчат... Они сами нифига здесь не понимают!\n"
      "Блин, я это всё же переделаю слегка...\n")

students = list(students)
students.sort()
students_grades = {students[student_number]: grades[student_number] for student_number in range(len(students))}

CTS.colorful_text(f"Ученики и их оценки: {students_grades}", CTS.Color.BLUE)
print("\nВо! теперь с этим хоть работать можно!.. Хрень конечно, но...")
CTS.colorful_text("ТИММИ!!!", CTS.Color.YELLOW)
print("Согласен. Давай узнаем что выходит в четверти...")

average_grades = list(map(lambda x: sum(x)/len(x), grades))

students_average_grades = {students[student_number]:
                           average_grades[student_number] for student_number in range(len(students))
                           }

CTS.colorful_text(f"\nУченики и их ожидаемые оценки в четверти: {students_average_grades}\n",
                  CTS.Color.BLUE)

CTS.colorful_text("ТИММИ!!!", CTS.Color.YELLOW)
print("Так, Тимми, медленно положи свои слова на землю и пни их мне ногой, спокойно, нам не нужны неприятности")
CTS.colorful_text("ТИММИ!!!", CTS.Color.YELLOW)
print("Ладно, может ты и прав.")
