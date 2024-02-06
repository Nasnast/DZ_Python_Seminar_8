'''Задача №49. Решение в группах
Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной'''

# 1. Создание файла: +++
#     - открываем файл на дозапись # a +++
# 2. Добавление контакта: +++
#     - запросить у пользователя новый контакт +++
#     - открыть файл на дозапись # a +++
#     - добавить новый контакт +++
# 3. Вывод данных на экран: +++
#     - открыть файл на чтение # r +++
#     - считать файл +++
#     - вывести на экран +++
# 4. Поиск контакта:
#     - выбор варианта поиска
#     - запросить данные для поиска
#     - открыть файл на чтение
#     - считываем данные файла, сохранить их в переменную
#     - осуществляем поиск контакта
#     - выводим на экран найденный контакта
# 5. Создание UI:
#     - вывести меню на экран +++ 
#     - запросить у пользавателя вариант действия +++
#     - запустить соответствующую функцию +++
#     - осуществить возможность выхода из программы +++

def input_surname():
    return input('Введите фамилию контакта: ').title()

def input_name():
    return input('Введите имя контакта: ').title()

def input_patronymic():
    return input('Введите отчество контакта: ').title()

def input_phone():
    return input('Введите телефон контакта: ')

def input_address():
    return input('Введите адрес(город) контакта: ').title()

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic}: {phone}\n{address}\n\n'


def add_contact():
    contact_str = create_contact()
    with open("phonebook.txt", 'a', encoding='utf-8') as file:
        file.write(contact_str)
    
           
def print_contacts():
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        contacts_str = file.read()
    #print([contacts_str]) 
    contacts_list = contacts_str.rstrip().split('\n\n')
    for n, contact in enumerate(contacts_list, 1):
        print(n, contact)
    

def search_contact():
    print(
            'Возможные варианты поиска:\n'
            '1. По фамилии\n'
            '2. По имени\n'
            '3. По отчество\n'
            '4. По телефону\n'
            '5. По адресу(город)'
            )
    var = input('выберите вариант поиска: ')
    while var not in ('1', '2', '3', '4', '5'):
        print('некорректный ввод!')
        var = input('выберите вариант поиска: ')
    i_var = int(var) - 1    

    search = input('Введите данные для поиска: ').title()
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        contacts_str = file.read()
        contacts_list = contacts_str.rstrip().split('\n\n')
   

    for str_contact in contacts_list:
        lst_contact = str_contact.replace(':', '').split()
        if search in lst_contact[i_var]:
            print(str_contact)


def copy_contact(): 
    copy_str = int(input('Какую строку вы хотите скопировать? '))
    with open("phonebook.txt",'r', encoding='utf-8') as firstfile, open('new_phonebook.txt','a', encoding='utf-8') as secondfile: 
        contacts_str_1 = firstfile.read()
        contacts_list_1 = contacts_str_1.rstrip().split('\n\n')  
               
        for n, contact in enumerate(contacts_list_1, 1):
             if n == copy_str: 
                secondfile.write(f'{contact}\n\n')
                print(f'Строка {copy_str} скопирована в файл new_phonebook.txt')
                print()
                interface()
           
        if n!=copy_str:
            print('Такой строки для копирования нет') 
            print()
            interface() 

 
def interface():
    with open("phonebook.txt", 'a', encoding='utf-8'):
        pass

    var = 0
    while var != '5':
        print(
            'Возможные варианты:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Копирование контакта в файл\n'
            '5. Выход'
            )
        print()
        var = input('выберите вариант действия: ')
        while var not in ('1', '2', '3', '4', '5'):
            print('некорректный ввод!')
            var = input('выберите вариант действия: ')
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
                exit()
        print()        


if __name__ == '__main__':
    interface()

