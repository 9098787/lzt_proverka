import sqlite3

def add_note(title: str, text: str) -> None:
    """Функция добавления заметки в базу данных.

        Сначала создается подключение к базе данных,
        затем создается курсор для выполнения SQL-запросов,
        далее сам INSERT-запрос. В конце изменения сохраняются (commit)
        и подключение к бд закрывается
    """
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO main (title, text) VALUES (?, ?)', (title, text))
    connection.commit()
    connection.close()

def get_notes() -> list:
    """Функция получения всех заметок из базы данных.

        Сначала создается подключение к базе данных,
        затем создается курсор для выполнения SQL-запросов,
        далее сам SELECT-запрос. В конце результат запрос получается
        с помощью метода fetchall, подключение закрывается и результат возвращается.
    """
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM main')
    notes = cursor.fetchall()
    connection.close()
    return notes

def delete_note(note_id: int) -> None:
    """Функция удаления заметки из базы данных.

        Сначала создается подключение к базе данных,
        затем создается курсор для выполнения SQL-запросов,
        далее сам DELETE-запрос. В конце изменения сохраняются (commit)
        и подключение к бд закрывается
    """
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM main WHERE id = ?', (note_id, ))
    connection.commit()
    connection.close()