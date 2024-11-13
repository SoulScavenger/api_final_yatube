# Проект API FINAL YATUBE
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

Проект представляет собой площадку для размещения публикаций, комментирования публикаций, возможность подписки на авторов публикации.

# Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/SoulScavenger/api_final_yatube.git
```

```
cd api_final_yatube
```

2. Создать и активировать виртуальное окружение:

```
python3 -m venv .venv
```

* Если у вас Linux/macOS

    ```
    source .venv/bin/activate
    ```

* Если у вас windows

    ```
    source .venv/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

3. Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

4. Выполнить миграции:

```
python manage.py migrate
```

5. Запустить проект:

```
python manage.py runserver
```

# Пример API запроса
<details><summary>
http://127.0.0.1:8000/api/v1/posts/ - GET запрос для получения всех публикаций</summary>

```
{

    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": 

[

        {
            "id": 0,
            "author": "string",
            "text": "string",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": "string",
            "group": 0
        }
    ]

}
```
</details>

### Подробную информацию об API запросах проекта можно найти в OpenAPI документации:
* ReDoc: http://127.0.0.1:8000/redoc/

### Автор: Максим Торгашин
