# файл для описания структуры БД
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # создаем объект db, ерез который будем управлять базой данных

class Contact(db.Model):  # класс описывает таблицу в БД; db.Model - специальный базовый класс
    # создаем колонки
    id = db.Column(db.Integer, primary_key=True)  # id - первичный ключ
    name = db.Column(db.String(30), nullable=False)  # строка до 30 символов, не может быть пустой
    phone = db.Column(db.String(20), nullable=False)