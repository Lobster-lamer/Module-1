from consoleTextStyle import ConsoleTextStyle as CTS


class CourseStatistic:

    def __init__(self,
                 exercise_done,
                 hours_spend,
                 course_name):
        self.exercise_done: int = exercise_done
        self.hours_spend: float = hours_spend
        self.course_name: str = course_name
        self.hours_per_exercise: float = self.hours_spend / self.exercise_done


if __name__ == "__main__":
    python_course_stat = CourseStatistic(12, 1.5, "Python")
    print("ПОМОГИТЕ!!! МОЙ КОМП СЛЕДИТ ЗА МНОЙ!!! ОН ДАЖЕ ЗНАЕТ КАКОЙ Я КУРС ПРОХОЖУ!!!")
    print("САМИ СМОТРИТЕ!!!")
    print(f"{CTS.ITALIC}{CTS.Color.BLUE}Курс:{CTS.Color.PURPLE}{python_course_stat.course_name}{CTS.Color.BLUE},"
          f"всего задач:{CTS.Color.PURPLE}{python_course_stat.exercise_done}{CTS.Color.BLUE}, "
          f"затрачено часов: {CTS.Color.PURPLE}{python_course_stat.hours_spend}{CTS.Color.BLUE},"
          f" среднее время выполнения {CTS.Color.PURPLE}{python_course_stat.hours_per_exercise}{CTS.Color.BLUE} часа."
          f"{CTS.Color.WHITE}")
    print("ААААААААААААААААА!!!")
