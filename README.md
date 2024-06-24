# Проект обработки изображений на Django и Celery

Этот проект демонстрирует обработку изображений с использованием Django и Celery с Docker.

## Настройка

### Предварительные требования

- Docker
- Docker Compose

### Установка

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/ваш_пользователь/myproject.git
    cd myproject
    ```

2. Соберите и запустите контейнеры Docker:

    ```sh
    docker-compose up --build
    ```

3. Примените миграции базы данных:

    ```sh
    docker-compose exec web python manage.py migrate
    ```

4. Создайте суперпользователя для доступа к админке Django:

    ```sh
    docker-compose exec web python manage.py createsuperuser
    ```

5. Откройте ваш браузер и перейдите по адресу `http://localhost:8000/admin`.

## Использование

- Загрузите изображение через админку Django.
- Изображение будет обработано Celery и изменено до различных размеров.
- Обработанные изображения будут сохранены по указанным путям.

## Участие

1. Сделайте форк репозитория.
2. Создайте новую ветку (`git checkout -b feature-branch`).
3. Внесите ваши изменения и закоммитьте их (`git commit -am 'Add new feature'`).
4. Отправьте изменения в ветку (`git push origin feature-branch`).
5. Создайте новый Pull Request.

## Лицензия

Этот проект лицензирован под лицензией MIT - смотрите файл [LICENSE](LICENSE) для деталей.
