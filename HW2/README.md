# Вторая домашняя работа п курсу "Базы Данных"

## Задача

Мы - мебельный магазин. К нам поступают претензии на изделия, нам надо передавать их производителям.

## Структура базы

**Manufacturer** - *Таблица с производителями*

* id integer PRIMARY KEY AUTO_INCREMENT
* Name nvarchar(100) NOT NULL
* Mail nvarchar(50)
* Address nvarchar(100) NOT NULL
* Сountry nvarchar(100) NOT NULL

**Product** - *Таблица с продукцией*

* id integer PRIMARY KEY AUTO_INCREMENT
* Denomination nvarchar(100) NOT NULL
* Code nvarchar(10) NOT NULL
* ManufacturerID integer NOT NULL
* Price integer NOT NULL

**Claim** - *Таблица с претензиями*

* id integer PRIMARY KEY AUTO_INCREMENT
* Text nvarchar(200) NOT NULL
* Code nvarchar(10) NOT NULL
* Declarant nvarchar(100) NOT NULL
* Status nvarchar(50) DEFAULT "Принята"

## Возможности

* Добавление новых производителей, товаров и претензий
* Просмотр таблицы с претензиями
* Удаление претензий с определенным статусом
* Изменение статуса претензии
* Join таблиц претензии и товара, с ограничением по стоимости.

## Запуск

В файле *config_info.py* хранится адрес базы данных, имя базы данных, имя пользователя и пароль.

Конфигуратор базы данных находится в файле Configurator.ipynb

1) Загрузить паки и файлы на свой компьютер на свой компьютер
2) Запустить файл main.py
```
python3 *path to main.py*
```
3) Перейти по [Ссылке](http://127.0.0.1:5000/)
