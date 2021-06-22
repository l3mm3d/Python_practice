class Todo:
    def __init__(self, title, desc, iscomplete):
        self.title = title
        self.description = desc
        self.iscomplete = iscomplete

    def __str__(self):
        return self.title + ',' + self.description + ',' + self.iscomplete

def main():
    while True:
        print('Добро пожаловать в скрипт для учёта дел')
        print('1. Открыть файл для просмотра списка дел')
        print('2. Открыть файл для просмотра и дозаписи списка дел')
        print('3. Открыть файл и перезаписать его')
        print('11. Открыть файл и вывести содержимое, отсортированное в алфавитном порядке по названию.')
        print('12. Открыть файл и вывести содержимое, отсортированное в алфавитном порядке по описанию.')
        print('21. Открыть файл и вывести только выполненные задания')
        print('22. Открыть файл и вывести только невыполненные задания')
        print('0. Выход')
        command = input()
        file = ''
        isCorrect = False

        if command == '1':
            while not isCorrect:
                print('Введите имя файла для открытия')
                filename = input()
                try:
                    file = open(filename, mode='r')
                    isCorrect = True
                except FileNotFoundError:
                    print('Некорректное имя файла')
            for line in file:
                print(*line.split(','), sep='  |  ')

        elif command == '2':
            while not isCorrect:
                print('Введите имя файла для открытия')
                filename = input()
                try:
                    file = open(filename, mode='a')
                    isCorrect = True
                except FileNotFoundError:
                    print('Некорректное имя файла')
            print('Введите данные нового дела:')
            tmp_todo = Todo(input('Title:'), input('Description:'), input('isComplete:'))
            file.writelines(str(tmp_todo))

        elif command == '3':
            while not isCorrect:
                print('Введите имя файла для открытия')
                filename = input()
                try:
                    file = open(filename, mode='w')
                    print('Файл очищен и готов для записи новых данных')
                    isCorrect = True
                except FileNotFoundError:
                    print('Некорректное имя файла')
            print('Введите данные нового дела:')
            tmp_todo = Todo(input('Title:'), input('Description:'), input('isComplete:'))
            file.write(str(tmp_todo))

        elif command == '11':
            while not isCorrect:
                print('Введите имя файла для открытия')
                filename = input()
                try:
                    file = open(filename, mode='r')
                    isCorrect = True
                except FileNotFoundError:
                    print('Некорректное имя файла')
            array = list()
            for line in file:
                tmp = Todo(*line.replace("\n", "").split(','))
                array.append(tmp)
            array = sorted(array, key=lambda x: x.title)
            for el in array:
                print(el.title + " | " + el.description + " | " + el.iscomplete)

        elif command == '12':
            while not isCorrect:
                print('Введите имя файла для открытия')
                filename = input()
                try:
                    file = open(filename, mode='r')
                    isCorrect = True
                except FileNotFoundError:
                    print('Некорректное имя файла')
            array = list()
            for line in file:
                tmp = Todo(*line.replace("\n", "").split(','))
                array.append(tmp)
            array = sorted(array, key=lambda x: x.description)
            for el in array:
                print(el.title + " | " + el.description + " | " + el.iscomplete)

        elif command == '21':
            while not isCorrect:
                print('Введите имя файла для открытия')
                filename = input()
                try:
                    file = open(filename, mode='r')
                    isCorrect = True
                except FileNotFoundError:
                    print('Некорректное имя файла')
            array = list()
            for line in file:
                tmp = Todo(*line.replace("\n", "").split(','))
                array.append(tmp)
            array = [ x for x in array if x.iscomplete == 'True']

            for el in array:
                print(el.title + " | " + el.description + " | " + el.iscomplete)

        elif command == '22':
            while not isCorrect:
                print('Введите имя файла для открытия')
                filename = input()
                try:
                    file = open(filename, mode='r')
                    isCorrect = True
                except FileNotFoundError:
                    print('Некорректное имя файла')
            array = list()
            for line in file:
                tmp = Todo(*line.replace("\n", "").split(','))
                array.append(tmp)
            array = [x for x in array if x.iscomplete == 'False']
            for el in array:
                print(el.title + " | " + el.description + " | " + el.iscomplete)

        elif command == '0':
            break

        else:
            print("Некорректный ввод")


if __name__ == "__main__":
    main()
