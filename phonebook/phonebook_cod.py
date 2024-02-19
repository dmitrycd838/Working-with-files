# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.
#
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Алгоритм решения здадачи.
# 1 Создание файла: +++
#   - открываем файл на дозапись. # a +++
# 2 Добавление контакта: +++
#   - запросить у пользователя данные +++
#   - открываем файл на дозапись # a +++
#   - добавить новый контакт +++
# 3 Вывод данных на экран:
#   - открыть файл на чтение # r
#   - считать файл
#   - вывести на экран
# 4 Поиск контакта:
#   - параметры поиска
#   - запросить данные для поиска
#   - открыть файл на чтение
#   - считать данные, сохнарить тх в переменную
#   - осуществить поиск контакта
#   - вывести на экран найденный контакт
# 5 Создать UI (юзер интерфейс)
#   - вывести меню на экран +++
#   - запросить у пользователя вариант действия
#   - запустить соответствующую функцию
#   - осуществить возможность выхода из программы


def lastname_input():
    return input('Введите фамилию контакта: ').title()


def name_input():
    return input('Введите имя контакта: ').title()


def patronymic_input():
    return input('Введите отчество контакта: ').title()


def phone_input():
    return input('Введите телефон контакта: ')


def address_input():
    return input('Введите город контакта: ').title()


def create_contact():
    lastname = lastname_input()
    name = name_input()
    patronymic = patronymic_input()
    phone = phone_input()
    address = address_input()
    return f'{lastname} {name} {patronymic}: {phone} \n{address}\n\n'


def add_contact():
    contact_str = create_contact()
    with open('telephone_directory.txt', 'a', encoding='utf-8') as file:
        file.write(contact_str)


def print_contacts():
    with open('telephone_directory.txt', 'r', encoding='utf-8') as file:
        contacts_str_search = file.read()
    # print([contacts_str_search])
        list_contacts = contacts_str_search.rstrip().split('\n\n')
    for n, cont in enumerate(list_contacts, 1):
        print(n, cont)


def search_contact():
    print(
        'Возможные варианты поиска:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчеству\n'
        '4. По номеру телефона\n'
        '5. По городу'
    )
    var = input('Выберите вариант поиска: ')
    while var not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод')
        var = input('Выберите вариант поска: ')
    i_var = int(var) - 1

    search = input('Введите данные для поиска: ').title()
    with open('telephone_directory.txt', 'r', encoding='utf-8') as file:
        contacts_str_search = file.read()
    # print([contacts_str_search])
    list_contacts = contacts_str_search.rstrip().split('\n\n')
    # print(list_contacts)

    for str_contact in list_contacts:
        lst_contact = str_contact.replace(':', '').split()
        if search in lst_contact[i_var]:
            print(str_contact)


def copy_contact():
    with open(r'C:\directory\pythonProject1\phonebook\telephone_directory.txt', 'r', encoding='utf-8') as file:
        all_contacts_str = file.read()
        contacts_list = all_contacts_str.rstrip().split('\n\n')

    for n, contact in enumerate(contacts_list, 1):
        print(n, contact)
    # print()

    one_cont_copy = int(input('Введите контакт по номеру для копирования: '))
    print()

    # for n, contact in enumerate(contacts_list, 1):
    #     if n == one_cont_copy:
    #         print(n, contact)
    with open('C:\\directory\\pythonProject1\\phonebook\\copy.txt', 'a', encoding='utf-8') as file:
        file.write (f'\n{contacts_list[one_cont_copy - 1]}\n')


def interface():
    with open('telephone_directory.txt', 'a', encoding='utf-8'):
        pass

    var = 0
    while var != '5':
        print(
            'Выберите возможные варианты:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Копировать контакт\n'
            '5. Выход'
        )
        print()
        var = input('Выберите вариант действия: ')
        while var not in ('1', '2', '3', '4', '5'):
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
                copy_contact()
            case '5':
                print('До свидания')
        print()


if __name__ == '__main__':
    interface()
