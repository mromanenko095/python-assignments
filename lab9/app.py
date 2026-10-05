# Главный код веб-приложения


from flask import Flask, render_template, request, redirect
from models import db, Note

app = Flask(__name__)  # Создадим приложение

# БД
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'  # используем SQLite, храня данные в файле notes.db
db.init_app(app)  # привязали объект db к приложению

# Главная страница приложения
@app.route('/')  # когда пользователь открывает приложение, вызвать ф. index
def index():
    notes = Note.query.all()  # Получаем все заметки
    return render_template('index.html', notes=notes)

# Добавление новой заметки
@app.route('/add', methods=['POST'])  # отправка формы
def add():
    text_data = request.form['text']  # Читаем заметку из отправленной формы
    important_data = request.form['important']  # Считываем флаг важности заметки
    
    # Сохранение в БД
    new_note = Note(text=text_data, important=important_data)  # Создание заметки как объекта
    db.session.add(new_note)  # добавление сессии
    db.session.commit()  # сохранение
    return redirect('/')  # возвращаемся на главную страницу

# Удаление всех заметок
@app.route('/clear', methods=['POST'])
def clear():
    db.session.query(Note).delete()  # удаление
    db.session.commit()  # сохранение
    return redirect('/')  # возврат на главную страницу

# Запуск локального сервера
if __name__ == '__main__':
    with app.app_context():  # Входим в контекст приложения
        db.create_all()  # Создание таблиц (если еще нет их)
    app.run(debug=True)
