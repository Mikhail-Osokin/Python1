import file_io
import Note

def create_note():
    name = input('Введите название: ')
    content = input('Введите текст заметки: ')
    return Note.Note(name=name, content=content)
def add():
    note = create_note()
    array = file_io.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_io.write_file(array, 'a')
    print('Заметка успешно добавлена')
def show(text):
    flag = True
    array = file_io.read_file()
    for notes in array:
        if text == 'all':
            flag = False
            print(Note.Note.info(notes))
        elif text == 'id':
            flag = False
            print('ID: ' + Note.Note.get_id(notes) + '; Название: ' + Note.Note.get_name(notes) + '.')
        elif text == 'date':
            flag = False
            print('Дата создания: ' + Note.Note.get_date(notes) + '; Название: ' + Note.Note.get_name(notes) + '.')
    if flag:
        print('Создайте новую заметку!')
def id_rewrite():
    id = input(
        'Выберете идентификатор заметки, которую требуется перезаписать: ')
    array = file_io.read_file()
    flag = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            note = create_note()
            Note.Note.set_name(notes, note.get_name())
            Note.Note.set_content(notes, note.get_content())
            Note.Note.set_date(notes)
            print('Изменения в заметке успешно сохранены')
    if flag:
        print('Заметка не найдена. Проверьте введенный идентификатор!')
    file_io.write_file(array, 'a')
def id_delete():
    id = input('Введите идентификатор заметки, которую требуется удалить: ')
    array = file_io.read_file()
    flag = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            flag = False
            prov = input('Подтвердите удаление (y или n): ').strip().lower()
            if prov == 'y':
                array.remove(notes)
                print('Заметка успешно удалена')
            elif prov == 'n':
                print('Операция удаления отменена')
    if flag:
        print('Указанная заметка не найдена. Проверьте идентификатор!')
    file_io.write_file(array, 'a')
def id_show():
    id = input('Введите ID необходимой заметки: ')
    array = file_io.read_file()
    flag = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            flag = False
            print(Note.Note.info(notes))
    if flag:
        print('Указанная заметка не найдена. Проверьте правильность внесенного ID!')
    file_io.write_file(array, 'a')
def date_show():
    date = input('Введите дату и время последнего редактирования: ')
    array = file_io.read_file()
    flag = True
    for notes in array:
        if date == Note.Note.get_date(notes):
            flag = False
            print(Note.Note.info(notes))
    if flag:
        print('Указанная заметка не найдена. Проверьте правильность внесенного идентификатора!')
    file_io.write_file(array, 'a')
    