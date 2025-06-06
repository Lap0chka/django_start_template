# 🧩 Django Starter Template

Этот репозиторий — шаблон (boilerplate) для быстрого старта проектов на Django.  
Он включает различные конфигурации: от базового Django до связок с Celery, Redis и Django REST Framework (DRF).

## 🗂 Ветки репозитория

- **`main`** — базовый Django-проект
- **`django-celery`** — Django + Celery + Redis
- **`drf`** — Django REST Framework (DRF)
- **`drf-celery`** — DRF + Celery + Redis

Каждая ветка содержит готовую структуру проекта, настроенные зависимости и базовые шаблоны для разработки.

## 🚀 Установка
1. Переименование папки `backend` (по желанию)**  
   Если необходимо, переименуйте папку `backend` на более удобное имя.  

2**🐍 Установка и активация виртуального окружения**
   1. Создайте виртуальное окружение:
      ```bash
      python3 -m venv venv
      ```
   2. Активируйте его:
      ```bash
      source venv/bin/activate
      ```
   3. Установите зависимости:
      ```bash
      pip install -r requirements.txt
      ```
   ⚠️ Убедитесь, в `.gitignore` указана папка `venv`.  
   Если вы переименуете окружение, не забудьте также изменить:
   - [.gitignore](.gitignore)`.gitignore`
   - настройки [linter.sh](linter.sh)
   - [pyproject.toml](pyproject.toml)`pyproject.toml`, если используется


3. **🔐 Создание `.env` файла**  
   Скопируйте шаблон переменных окружения:
   ```bash
   cp .env_sample .env
   
4. 🐳 Запуск Docker Compose
📌 Обратите внимание: используется порт базы данных 5412, а не стандартный 5432:

docker-compose up --build

5. 🔁 Смена удалённого репозитория Git
   1.	Удалите текущий origin:
        git remote remove origin
   2. Убедитесь, что удалённые репозитории удалены:
        git remote -v
   3. Добавьте новый origin
      git remote add origin <новый-url>

6. ⚙️ Запуск проекта
   1. cd проект
   2. ./manage.py runserver


### ⚙️ Pre-commit хуки

В проекте настроен [pre-commit](https://pre-commit.com/) 
— инструмент, который запускает линтеры и форматтеры автоматически при коммите.

#### 📦 Установка

```bash
pre-commit install
```

> После этого хуки будут автоматически запускаться при каждом `git commit`.

#### 🚀 Ручной запуск

```bash
pre-commit run --all-files
```


В проекте используются [django-extensions](https://django-extensions.readthedocs.io/) 
— набор полезных утилит для разработки.

#### 🔧 Полезные команды

| Команда           | Описание                                                  |
|------------------|-----------------------------------------------------------|
| `shell_plus`     | Улучшенная оболочка Python с автоимпортами моделей        |
| `runserver_plus` | Расширенный сервер с отладчиком Werkzeug                  |
| `show_urls`      | Список всех URL и их имён                                 |
| `graph_models`   | Визуализация моделей и связей в PNG/Graphviz              |

#### 🧪 Примеры

```bash
python manage.py shell_plus
python manage.py runserver_plus
python manage.py show_urls
python manage.py graph_models app_name -o graph.png
```

---

### 🐞 Django Debug Toolbar

[django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/) — 
мощный инструмент для профилирования и отладки запросов в Django-приложении.

### 🕓 Django Simple History

[django-simple-history](https://django-simple-history.readthedocs.io/) —
библиотека, которая сохраняет историю изменений моделей Django.

#### 🔍 Зачем нужно

- 🔒 **Аудит** — кто и когда изменил данные
- 🕵️ **Отладка** — легко понять, какие значения были раньше
- ⏪ **Откат** — можно восстановить предыдущую версию записи


#### 🧱 Пример модели

```python
from django.db import models
from simple_history.models import HistoricalRecords

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    history = HistoricalRecords()
```

#### 🛠 Миграции

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 🧪 Использование

```python
product = Product.objects.create(name="Phone", price=500)
product.price = 450
product.save()

for record in product.history.all():
    print(record.history_date, record.price)


#### 🖥 Поддержка в админке

```python
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Product

admin.site.register(Product, SimpleHistoryAdmin)
```
"""

### 🔐 Security Best Practices

#### 1. 🌐 django-cors-headers

Позволяет настраивать [CORS (Cross-Origin Resource Sharing)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS), 
чтобы ограничить доступ к API только определённым доменам.


📌 Используется для: защиты API от несанкционированного доступа с других доменов.

---

#### 2. 🧱 Secure Headers (Безопасные заголовки)

Django позволяет установить заголовки, которые защищают от XSS, MIME-sniffing и Clickjacking.

Рекомендуемые настройки в `settings.py`:

```python
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000  # включает HSTS для HTTPS
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

📌 Используется для: повышения защищённости сайта на уровне браузера и протоколов.

---

#### 3. 🔐 django-csp

[Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) — 

📌 Используется для: ограничения источников загрузки скриптов, стилей и другого контента.


### 🛠 Adminer в Docker

[Adminer](https://www.adminer.org/) — 
лёгкий веб-интерфейс для работы с базой данных (альтернатива phpMyAdmin).

#### 📦 Добавление в docker-compose


```bash
docker-compose up -d
```

Adminer будет доступен по адресу: [http://localhost:8080](http://localhost:8080)

#### 🔐 Подключение

- **System**: PostgreSQL или MySQL (в зависимости от вашего `db`)
- **Server**: имя сервиса из `docker-compose.yml` (например, `db`)
- **Username** / **Password**: те же, что в `DATABASES` в `settings.py`
- **Database**: имя вашей базы данных

📌 Используется для: быстрого доступа к базе данных из браузера для отладки и разработки.

### 🧪 Используемые инструменты качества кода

Проект использует следующие инструменты статического анализа и форматирования:

| Категория  | Инструмент | Назначение                                      |
|------------|------------|--------------------------------------------------|
| Форматирование | `black`     | Автоматическое форматирование кода |
| Типизация      | `mypy`      | Проверка типов Python по аннотациям           |
| Стиль          | `flake8`    | Проверка соблюдения стиля кода (PEP8)         |
| Анализ         | `pylint`    | Глубокий линтинг и анализ качества кода       |

Эти инструменты запускаются через линтер-скрипты и CI для обеспечения единообразного и качественного кода.
