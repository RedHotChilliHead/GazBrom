# GazBrom

GazBrom — это веб-приложение для управления информацией о сотрудниках компании. 
Приложение позволяет отображать сотрудников в иерархическом виде, просматривать их в табличном формате, 
выполнять операции CRUD (создание, чтение, обновление, удаление), а также осуществлять сортировку и фильтрацию данных.

## Основные возможности
- **Создание и управление сотрудниками**: возможность добавлять новых сотрудников с указанием их имени, фотографии, зарплаты, 
начальника и других параметров.
- **CRUD-операции**: поддержка всех CRUD-операций для работы с сотрудниками.
- **Иерархический просмотр**: отображение всех сотрудников в виде иерархической структуры.
- **Табличный вид**: представление данных о сотрудниках в табличном формате с поддержкой сортировки и фильтрации по различным полям.
- **Поиск и сортировка**: быстрый поиск по имени, должности и другим параметрам сотрудников. Поддержка сортировки данных по различным критериям.
- **Аутентификация и авторизация**: поддержка разных уровней доступа для пользователей, включая административные функции.
- **Команды управления**:
  - **create_employee**: команда для массового создания сотрудников (более 150 записей) с использованием случайных данных в соответствии с 
иерархией компании.
  - **delete_employees**: команда для удаления всех сотрудников из базы данных, что позволяет подготовить базу к новому набору данных.
- **Контейнеризация и управление данными**:
  - Использование PostgreSQL в качестве основной базы данных.
  - Деплоймент с использованием Docker и Docker Compose для удобства развертывания и управления приложением.
  - Инициализация базы данных тестовыми данными через скрипт dump.sql.

### Стартовая страница
Приложение доступно по адресу http://127.0.0.1:8000/GazBrom/
![start.png](assets%2Fstart.png)

## Установка и запуск

Для развертывания всей необходимой инфраструктуры используйте Docker и Docker Compose.

### Предварительные требования

- Убедитесь, что у вас установлены Docker и Docker Compose
- Версия Python: 3.11

### Шаги установки

1. Клонируйте репозиторий проекта:

```
git clone https://github.com/RedHotChilliHead/GazBrom.git
cd GazBrom
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
3. Соберите и запустите Docker-контейнеры:
```
docker compose up -d
docker compose run gazbromapp python manage.py migrate
```
Это создаст необходимые тома, соберет и запустит Docker-контейнеры в фоновом режиме и выполнит миграции.

4. Остановите сервисы при необходимости:
```
docker compose down
```
