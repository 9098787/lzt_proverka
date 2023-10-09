import db

def add_note() -> None: # Функция добавления заметки
    title = input('Введите загловок заметки: ')
    text = input('Введите текст заметки: ')
    db.add_note(title, text) # Взаимодействие с бд
    print('\nЗаметка успешно добавлена!\n')

def get_notes() -> None: # Функция получения заметок
    notes = db.get_notes() # Взаимодействие с бд
    for note in notes:
        print(f'ID: {note[0]} Заголовок: {note[1]} Текст: {note[2]}\n')
    print('Все заметки показаны!\n')

def search_notes() -> None: # Функция поиска заметок
    key = input('Введите ключевое слово/фразу: ')
    notes = db.get_notes() # Взаимодействие с бд
    for note in notes:
        if key in note[1] or key in note[2]: # Проверка есть ли ключевая фраза, в заголовке/тексте заметки
            print(f'ID: {note[0]} Заголовок: {note[1]} Текст: {note[2]}\n')
    print('Все заметки показаны!\n')

def delete_note() -> None: # Функция удаления заметок
    note_id = input('Введите ID заметки: ')
    # Строки 26 - 32: Обработка исключений
    if note_id.isnumeric():
        note_id = int(note_id)
        notes = db.get_notes() # Взаимодействие с бд
        note_ids = list()
        for note in notes:
            note_ids.append(note[0])
        if note_id in note_ids:
            db.delete_note(note_id) # Взаимодействие с бд
            print('Заметка удалена!\n')
        else:
            print('Заметка с таким ID отсутсвует в базе данных!\n')
    else:
        print('Неверное значение!\n')

while True: # Цикл для получения режимов работы
    work_type = input('Выберите режим работы:\n1 - Добавление заметки\n2 - Посмотреть все заметки\n3 - Поиск заметки\n4 - Удаление заметки\n0 - Выход из программы\n')
    if work_type == '1':
        add_note()
    elif work_type == '2':
        get_notes()
    elif work_type == '3':
        search_notes()
    elif work_type == '4':
        delete_note()
    elif work_type == '0':
        print('Работа программы завершена!')
        break
    else:
        print('Данные введены неверно!\n')