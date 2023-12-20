import operation
import interface


def run():
    command = ''
    while command != '0':
        interface.menu()
        command = input().strip()
        if command == '6':
            operation.show('all')
        elif command == '1':
            operation.add()
        elif command == '2':
            operation.show('id')
            operation.id_delete()
        elif command == '3':
            operation.show('id')
            operation.id_rewrite()
        elif command == '4':
            operation.show('date')
            operation.date_show()
        elif command == '5':
            operation.show('id')
            operation.id_show()
        elif command == '0':
            print ('Вы завершили работу с приложением')
            break
        else:
            print('Команды в списке нет!')

