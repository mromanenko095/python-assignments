# главный код веб приложения
from flask import Flask, render_template, request, redirect, url_for
'''
Flask - главный класс приложения
render_template - для показа html-страницы
request - для получения данных из формы
redirect, url_for - ля перенаправления на другую страницу
'''

# из файла models.py импортируем модель БД и объект db
from models import db, Contact

# создаем экзмепляр Flask-приложения
app = Flask(__name__)  # __name__ - специальная переменная, которая содержит имя текущего файла

# настройка подключения к БД
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///db.phonebook.db'

# отключаем отслеживание изменений объектов (чтобы не потреблять лишнюю память)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



