# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define sir = Character('Сергиц', color = "#15c3e6")
define wb = Character('Сотрудник банка', color = "#11e039")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene sberstreet

    show sir 

    sir "Пора оформить себе карту чтобы донатить в бравл стас"

    hide sir

    scene sberbank
    with fade

    show sir:
        xalign 0.8

    show wb:
        xalign 0.2



    menu:
        wb "Здравствуйте, чем могу помочь?"

        "Я хочу оформить карту Сбербанка":
            jump wannacard

        "Иди нахер":
            jump poshel_nah
    

    return


label poshel_nah:
    wb "Иди отсюда конченный"
    return


label wannacard:
    menu:
        wb "Для начала назовите свое имя"


        "Сергий Балокин":
            jump chestnost

        "Сергей Балакин":
            jump chestnost

        "Сергиц":
            jump checkage

        "Я передумал":
            jump poshel_nah



    return

label chestnost:
    wb "Просьба отвечать честно!"
    jump wannacard
    return


label checkage:
    menu:
        wb "Сколько вам лет?"

        "28":
            jump poshel_nah
        "13":
            wb "К сожалению, вы еще не достаточно взрослый, но мы сделаем вам карту SberKids!"
            jump phonecard
        "Я передумал":
            jump poshel_nah
    return


label phonecard:
    menu:
        wb "Теперь скажите ваш мобильный телефон..."

        "+79303516978":
            wb "Хорошо, секунду..."
            jump codeword

        "Я передумал":
            jump poshel_nah
    return


label codeword:
    menu:
        wb "Теперь, придумайте кодовое слово"

        "gay":
            wb "Я уже догадывалась... кхм кхм."
            jump donecard


        "бебра228":
            wb "Интересная фантазия..."
            jump donecard



        "Я передумал":
            jump poshel_nah
    return


label donecard:
    wb "Вот ваша карта, до свидания"

    sir "До свидания"

    hide wb
    hide sir

    scene home
    with fade

    show sir

    sir "Ураа! Теперь я самый крутой"

    return