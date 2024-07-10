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

girl_interest_set = {"Бухать", "Гулять", "Кодить"}

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
    print("Ну и хрень")
    print("Надо удалить весь этот код, пока никто не увидел\n")
    CTS.colorful_text("Привет, красавчик!", CTS.Color.CYAN)
    print("ЖЕНЩИНА!!!")
    CTS.colorful_text("Не хочет ли такой красивый стереотипный программист заплатить за мой кофе?",
                      CTS.Color.CYAN)
    print(CTS.ITALIC + "Странно, от меня не только не убежала девушка, но и сама подошла! похоже на обман!\n"
          + CTS.REGULAR + "А чем ты интересуешься?")
    CTS.colorful_text("sdfafghdsdfsxgfdsfg", CTS.Color.CYAN)
    print(CTS.ITALIC + "Не понимаю я женщин( Ладно, запрошу множество её интересов... Как оно там..."
          + CTS.REGULAR + "requst.get(interest)... SUDO!")
    CTS.colorful_text(girl_interest_set, CTS.Color.BLUE)
    print("КОДИТЬ!!! ОНА ЛЮБИТ КОДИТЬ!!!... Хотя я б кое чё добавил...")
    girl_interest_set.add("Warhammer 40 000")
    print(girl_interest_set)
    print("О!.. Ещё бы я кое-что убрал бы...")
    girl_interest_set.discard("Бухать")
    girl_interest_set.remove("Гулять")
    CTS.colorful_text(girl_interest_set, CTS.Color.BLUE)
    CTS.colorful_text("БОЛЬШЕ ЧЕРЕПОВ БОГУ ЧЕРЕПОВ!!!", CTS.Color.CYAN)
    print("О! Вот теперь шикарно!")
