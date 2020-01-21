import shutil
bool = True
while(True):
    while(bool == True):
        action = input("Напишите старт/start чтобы начать операцию!\n")
        if(action == "старт" or action == "start"):
            bool = False
        else:
            print("Ошибка в стартовом слове!")
    first = input("Путь файла,который надо скопировать:")
    second = input("Путь куда копировать:")
    try:
        if(action == "старт" or action == "start"):
            shutil.copy(first, second)
            bool = True
        else:
            print("Ошибка в стартовом слове!")
            bool = True
    except (FileNotFoundError):
        print("Неправильно указан путь!")
        bool = True
    nextOperation = input("Для просмотра продолжения напишите: продолжить\nДля выхода напишите: выход\n")
    if(nextOperation == "выход"):
        break
    elif(nextOperation == "другая"):
        pass
    elif(nextOperation == nextOperation):
        break
    