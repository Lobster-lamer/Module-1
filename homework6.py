from consoleTextStyle import ConsoleTextStyle as CTS


def start_talking(data_baseXD: dict,
                  stop_word: str):
    while 1:
        print(CTS.Color.WHITE, end="")
        keyboard_input = input(">>")
        if keyboard_input == stop_word:
            break
        print(CTS.Color.PURPLE +
              data_baseXD.get(keyboard_input, "Не совсем понимаю, о чём вы говорите... Ну да пофиг"))


answerer = {
    "Привет!": "Здравствуйте! Чем я могу помочь?",
    "Скажи как пройти к библиотеке": "Вводите C:/Users/Ваш пользователь/PycharmProjects/pythonProject/"
                                     "Ваше название библиотеки",
    "Сколько времени?": "Не могу ответить на этот вопрос, так как не понимаю про какой часовой пояс вы спрашиваете,"
                        " а спросить вас в ответ - лень",
    "Что ты умеешь?": "Быть ленивым куском кода",
    "Гыъь)": "ГЫЪЬ)"
}

if __name__ == "__main__":
    print("Тыак, интересно что за разговорного бота он написал...\nСеръёзно? Словарь? Ладно, что там в словаре есть?")
    CTS.colorful_text(answerer, CTS.Color.PURPLE)
    print("Какой ленивый словарь! Почти ничего нет!")
    print("Ладно, давай попробуем запустить бота, что ли?\n")
    CTS.colorful_text(answerer["Привет!"], CTS.Color.PURPLE)
    start_talking(answerer, "Ой, да пошёл ты!")
    print("\nКакая же хрень")
    print("Добавлю-ка то, что первое приходит в голову при виде этого")
    answerer.update({"Ты - говно": "В этом и была задумка",
                     "Ты - ленивый": "Я бы что-нибудь ответил, но мне лень"})
    print("О, а что это за хрень?")
    print(answerer.pop("Гыъь)"))
    print("Прикольно, но нафиг оно в словаре нужно, шо там у нас получилось?")
    CTS.colorful_text(answerer, CTS.Color.PURPLE)
    print("Попробуем пообщаться...\n")
    CTS.colorful_text(answerer["Привет!"], CTS.Color.PURPLE)
    start_talking(answerer, "Ну и хрень")
    print("Надо удалить весь этот код, пока никто не увидел")
