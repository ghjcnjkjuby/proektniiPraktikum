import os
print("Стандартная директория: " + str(os.getcwd()))
print("Имя: " + str(os.getlogin()))
while(True):
    try:
        dir = input("Укажите путь к директории:")
        print("Выбранная директория:" + dir)
        print("Файлы/папки в данной директории:")
        print(os.listdir(dir))
        nextOperation = input("Для просмотра другой директории напишите: другая\nДля выхода напишите: выход\n")
        if(nextOperation == "выход"):
            break
        elif(nextOperation == "другая"):
            pass
        elif(nextOperation == nextOperation):
            break
    except (FileNotFoundError):
        print("Такой директории нет!")
