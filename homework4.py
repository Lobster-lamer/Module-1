from consoleTextStyle import ConsoleTextStyle as CTS


def purple_text(func, func_container):
    print(CTS.color["PURPLE"], end="")
    func(func_container)
    print(CTS.color["WHITE"], end="")


def cyan_text(func, func_container):
    print(CTS.color["DARKCYAN"], end="")
    func(func_container)
    print(CTS.color["WHITE"], end="")


def environment_sound(func_container):
    print(CTS.color["GREEN"]+CTS.ITALIC)
    print("--", end="")
    print(func_container, end="")
    print("--")
    print(CTS.REGULAR)


dialog_phrase = "-Здравствуйте, Вас беспокоит защита сбербанка!"
print("-Алло?")
purple_text(print, dialog_phrase)
print("-Я не понял, что вы сказали, повторите ещё раз")
purple_text(print, dialog_phrase.upper())
print("-НЕ ПОВЫШАЙТЕ НА МЕНЯ РЕГИСТР!")
purple_text(print, dialog_phrase.lower)
print("-НЕ ПОНИЖАЙТЕ НА МЕНЯ РЕГИСТР! ПОЧЕМУ ВЫ ТАК МЕДЛЕННО ГОВОРИТЕ? ДУМАЕТЕ Я ТУПОЙ?")
purple_text(print, dialog_phrase.replace(" ", ""))
print("-ПОЧЕМУ ВЫ ТАК БЫСТРО ГОВОРИТЕ?")
purple_text(print, dialog_phrase[0:2]+"...")
print("-Всё-всё, я внимательно вас слушаю")
purple_text(print, "-..."+dialog_phrase[-2:])
print("-Ну куда вы так спешите? Давайте ещё раз...")
purple_text(print, "-ОЙ, ДА ИДИТЕ НАФИГ!!!")
environment_sound("звонок окончен")
print("-Гы-гы) Нефиг мне звонить)")
cyan_text(print, "-Кто это был?")
print("-Звонили мошенники, сказали:\"" + dialog_phrase[-len(dialog_phrase)+1:] + "\"")
print("..." + "\"" + dialog_phrase[-len(dialog_phrase)+1:], "\"... Ого! Эти люди становятся умнее, фразу из " +
      str(len(dialog_phrase)) + " букв выучили!\n ...Так! А кто меня спрашивал: \"Кто это был?\"")
environment_sound("играет хоррор музыка")
