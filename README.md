# Проект API приложения Yatube 
Автор: Коржов Дмитрий
## Назначение
Проект предназначен для использования в качестве API для реализации соц сети yatube


## Используемые технологии
Python 3.7.9, Django 3.2.16

## Установка

1. Склонировать репозиторий 
```
git clone https://github.com/kvot32/api_final_yatube
```

2. Создать виртуальное окружение:
```
python -m venv venv
```

3. Установить зависимости:
```
pip install -r requirements.txt
```

4. Создать и применить миграции:
```
python manage.py makemigrations
python manage.py migrate
```

5. Запустить сервер: 
```
python manage.py runserver
```