from data_create import *

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
