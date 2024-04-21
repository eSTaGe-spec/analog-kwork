## Использованиe
1. Клонирование репозитория(Windows)
    ```
   git clone https://github.com/eSTaGe-spec/analog-kwork.git
    ```
3. Создание виртуального окружения
    ```
   python -m venv venv
    ```
5. Активация виртуального окружения
    ```
   venv\Scripts\activate
    ```
7. Переход в папку app
    ```
   cd app
    ```
9. Установка зависимостей
    ```
   pip install -r requirements.txt
    ```
11. Создание новых миграций
    ```
    python manage.py makemigrations
    ```
13. Применение миграций
    ```
    python manage.py migrate
    ```
15. Создание суперпользователя
    ```
    python manage.py createsuperuser
    ```
17. Запуск сервера
    ```
    python manage.py runserver
    ```
