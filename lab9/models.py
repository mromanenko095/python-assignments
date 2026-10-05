# Описание структуры БД


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Модель для заметок
class Note(db.Model):  # класс-наследник от Model
    id = db.Column(db.Integer, primary_key=True)  # колонка id, первичный ключ
    text = db.Column(db.String(200), nullable=False)  # Текст заметки
    important = db.Column(db.String(100))  # Указатель важности
