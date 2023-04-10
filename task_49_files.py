""" Задача №49:
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
"""

import os
import json


def find_contact(contacts: list) -> dict:
    what = input('Кого ищем?\n>>> ')
    found = list(filter(lambda el: what in el['first_name'] or what in el['second_name'], contacts))
    if found:
        show_on_screen(found)
    else:
        print('Никого не нашли ;(')


def file_path(file_name='phone_book'):
    return os.path.join(os.path.dirname(__file__), f'{file_name}.txt')


def load_from_file():
    path = file_path()

    with open(path, 'r', encoding='UTF-8') as file:
        data = json.load(file)

    return data


def save_to_file(contact: list) -> None:
    path = file_path()

    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(contact, file, ensure_ascii=False)


def show_on_screen(contacts: list) -> None:
    decode_keys = dict(
        first_name='Имя:',
        second_name='Фамилия:',
        contacts='Телефон:'
    )
    pretty_text = str()
    for num, elem in enumerate(contacts, 1):
        pretty_text += f'Контакт №{num}:\n'
        pretty_text += '\n'.join(f'{decode_keys[k]} {v}' for k, v in elem.items())
        pretty_text += '\n________\n'
    print(pretty_text)


def create_contact_info():
    pass


def new_contact(contacts: list) -> None:
    contacts.append(
        dict(
            first_name=input('Введите имя контакта:\n>>> '),
            second_name=input('Введите фамилию контакта:\n>>> '),
            contacts=input('Введите номер телефона:\n>>> ')
        )
    )


def delete_contact(contacts: list) -> None:
    fn_remove = input('Имя контакта, который необходимо удалить?\n>>> ')
    sn_remove = input('Фамилия контакта, который необходимо удалить?\n>>> ')
    found = list(filter(lambda el: fn_remove in el['first_name'] and sn_remove in el['second_name'], contacts))
    
    if found:
        for contact in found:
            contacts.remove(contact)
        print(f'Контакт {fn_remove} {sn_remove} удалён!')
    else:
        print('Никого не нашли ;(')


def change_contact(contacts: list) -> None:
    fn_change = input('Имя контакта, который необходимо изменить?\n>>> ')
    sn_change = input('Фамилия контакта, который необходимо изменить?\n>>> ')
    found = list(filter(lambda el: fn_change in el['first_name'] and sn_change in el['second_name'], contacts))
    
    if found:
        for contact in found:
            idx = contacts.index(contact)
            contacts.remove(contact)
            contacts.insert(idx,
                dict(
                    first_name=input('Введите имя контакта:\n>>> '),
                    second_name=input('Введите фамилию контакта:\n>>> '),
                    contacts=input('Введите номер телефона:\n>>> ')
                )
    )
        print(f'Контакт {fn_change} {sn_change} изменён!')
    else:
        print('Никого не нашли ;(')  


def menu():
    commands = [
        'Показать все контакты',
        'Найти контакт',
        'Создать контакт',
        'Удалить контакт',
        'Изменить контакт'
    ]
    print('Укажите номер команды:')
    print('\n'.join(f'{n}. {v}' for n, v in enumerate(commands, 1)))
    choice = input('>>> ')

    try:
        choice = int(choice)
        if choice < 0 or len(commands) < choice:
            raise Exception('Такой команды пока нет ;(')
        choice -= 1
    except ValueError as ex:
        print('Я вас не понял, повторите...')
        menu()
    except Exception as ex:
        print(ex)
        menu()
    else:
        return choice


def main() -> None:
    print('Программа запущена...')
    data = load_from_file()
    #data = tests()

    command = menu()
    if command == 0:
        show_on_screen(data)
    elif command == 1:
        find_contact(data)
    elif command == 2:
        new_contact(data)
    elif command == 3:
        delete_contact(data)
    elif command == 4:
        change_contact(data)

    save_to_file(data)
    print('Конец программы!')


def tests():
    contact = dict(
        first_name='Иван',
        second_name='Иванов',
        contacts='123'
    )
    contact2 = dict(
        first_name='Петр',
        second_name='Петров',
        contacts='123'
    )
    contact3 = dict(
        first_name='Петр',
        second_name='Иванов',
        contacts='123'
    )
    contact4 = dict(
        first_name='Иван',
        second_name='Петров',
        contacts='123'
    )
    contacts = [contact, contact2, contact3, contact4]
    return contacts


if __name__ == '__main__':
    main()