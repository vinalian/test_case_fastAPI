Setup: \
Создать виртуальное окружение python 3.11 \
Если на вашем ПК не установлен poetry: Установите его отдельно в ваше виртуальное окружение (pip install poetry) \
Введите в консоль:                          poetry install  \
После установки всех зависимостей заполните .env файл (данные БД) \
Затем выполните комманду:                   alembic upgrade head \
После можно запусть сайт коммандой:         python3 app/start_api.py \
