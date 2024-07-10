from consoleTextStyle import ConsoleTextStyle as CTS


def scammer_text(func_container):
    CTS.colorful_text(func_container, CTS.Color.PURPLE)


def environment_sound(func_container):
    print(CTS.Color.GREEN+CTS.ITALIC)
    print("--", end="")
    print(func_container, end="")
    print("--")
    print(CTS.REGULAR)


dialog_phrase = "-Здравствуйте, Вас беспокоит защита сбербанка!"
print("-Алло?")
scammer_text(dialog_phrase)
print("-Я не понял, что вы сказали, повторите ещё раз")
scammer_text(dialog_phrase.upper())
print("-НЕ ПОВЫШАЙТЕ НА МЕНЯ РЕГИСТР!")
scammer_text(dialog_phrase.lower)
print("-НЕ ПОНИЖАЙТЕ НА МЕНЯ РЕГИСТР! ПОЧЕМУ ВЫ ТАК МЕДЛЕННО ГОВОРИТЕ? ДУМАЕТЕ Я ТУПОЙ?")
scammer_text(dialog_phrase.replace(" ", ""))
print("-ПОЧЕМУ ВЫ ТАК БЫСТРО ГОВОРИТЕ?")
scammer_text(dialog_phrase[0:2]+"...")
print("-Всё-всё, я внимательно вас слушаю")
scammer_text("-..."+dialog_phrase[-2:])
print("-Ну куда вы так спешите? Давайте ещё раз...")
scammer_text("-ОЙ, ДА ИДИТЕ НАФИГ!!!")
environment_sound("звонок окончен")
print("-Гы-гы) Нефиг мне звонить)")
CTS.colorful_text("-Кто это был?", CTS.Color.CYAN)
print("-Звонили мошенники, сказали:\"" + dialog_phrase[-len(dialog_phrase)+1:] + "\"")
print("..." + "\"" + dialog_phrase[-len(dialog_phrase)+1:], "\"... Ого! Эти люди становятся умнее, фразу из " +
      str(len(dialog_phrase)) + " букв выучили!\n ...Так! А кто меня спрашивал: \"Кто это был?\"")
environment_sound("играет хоррор музыка")
