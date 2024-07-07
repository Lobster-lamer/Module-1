class ConsoleTextStyle:
    """
    Класс используется для добавления наклона, жирности, подчёркивания и раскраски текста в консоли.

    И всё.
    """
    color = {"PURPLE": '\033[95m',
    "CYAN": '\033[96m',
    "DARKCYAN": '\033[36m',
    "BLUE": '\033[94m',
    "GREEN": '\033[92m',
    "YELLOW": '\033[93m',
    "RED": '\033[91m',
    "WHITE" : '\033[0m'}

    BOLD = "\x1B[1m"
    ITALIC = "\x1B[3m"
    UNDERLINE = "\x1B[4m"

    REGULAR = "\x1B[0m"

    @staticmethod
    def colorful_text(print_container, text_color):
        """
        Сразу выводит в консоль покрашенный текст

        :param print_container: выводимый текст
        :param text_color: цвет из переменной класса color (доделать)
        """
        print(ConsoleTextStyle.color[text_color], end="")
        print(print_container, end="")
        print(ConsoleTextStyle.color["WHITE"])

    @staticmethod
    def colorful_str(print_container: str,
                     text_color: str) -> str:
        """
            Выводит покрашенный str

            :param print_container: выводимый текст
            :param text_color: цвет из переменной класса color (доделать)
            :return: Покрашенный текст в str
        """
        return ConsoleTextStyle.color[text_color] + print_container + ConsoleTextStyle.color["WHITE"]