from logger import *

def interface():
    with open('telephone_directory.txt', 'a', encoding='utf-8'):
        pass

    var = 0
    while var != '4':
        print(
            'Выберите возможные варианты:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Выход'
             )
        print()
        var = input('Выберите вариант действия: ')
        while var not in ('1', '2', '3', '4'):
            print('Некорректный ввод')
            var = input('Выберите вариант действия: ')
        print()

        match var:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                print('До свидания')
        print()