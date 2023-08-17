import os
import shutil
import pathlib
import platform

while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории (*необязательный пункт)')
    print('12. выход')

    choice = input('Выберите пункт меню')

    if choice == '1':
        folder = str(input('введите название папки:'))

        if os.path.isdir(folder) == False:
            os.mkdir(folder)

        print(os.path.isdir(folder) == True)
        pass
    elif choice == '2':
        folder = str(input('введите название папки:'))

        if os.path.isdir(folder) == True:
            os.rmdir(folder)

        print(os.path.isdir(folder) == False)
        pass
    elif choice == '3':
        folder = str(input('введите название папки:'))
        newfolder = str(input('введите новое название папки:'))

        if os.path.isdir(folder) == True:
            shutil.copytree(folder, newfolder)

        print(os.path.isdir(newfolder) == True)
        pass
    elif choice == '4':

        pass
    elif choice == '5':

        pass
    elif choice == '6':

        pass
    elif choice == '7':

        print(platform.platform() == 'Windows-10-10.0.19045-SP0')
        pass
    elif choice == '8':

        print('Дмитрий С.' == 'Дмитрий С.')
        pass
    elif choice == '9':

        pass
    elif choice == '10':

        pass
    elif choice == '11':
        folder = str(input('введите название рабочей директории:'))

        os.chdir(folder)

        print(os.getcwd() == folder)
        pass
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')