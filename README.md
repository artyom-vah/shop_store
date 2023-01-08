# store
### Описание

# **store**
### **Описание**
Интернет-магазин **Учебный проект**.

Интернет-магазин с авторизацией, регистрацией, корзиной.

### **Стек**
![python version](https://img.shields.io/badge/Python-3.10.2-green)
![asgiref version](https://img.shields.io/badge/asgiref-3.6.0-green)
![asttokens version](https://img.shields.io/badge/asttokens-2.2.1-green)
![backcall version](https://img.shields.io/badge/backcall-0.2.0-green)
![colorama version](https://img.shields.io/badge/colorama-0.4.6-green)
![decorator version](https://img.shields.io/badge/decorator-5.1.1-green)
![django version](https://img.shields.io/badge/Django-4.1.5-green)
![django-debug-toolbar version](https://img.shields.io/badge/asgiref-3.2.4-green)
![executing version](https://img.shields.io/badge/executing-1.2.0-green)
![jedi version](https://img.shields.io/badge/jedi-0.18.2-green)
![pillow version](https://img.shields.io/badge/Pillow-9.3.0-green)
см. requirements.txt

### **Запуск проекта в dev-режиме**
Инструкция ориентирована на операционную систему windows и утилиту git bash.<br/>
Для прочих инструментов используйте аналоги команд для вашего окружения.

1. Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone https://github.com/artyom-vah/shop_store.git
```

```
cd store
```

2. Установите и активируйте виртуальное окружение
```
python -m venv venv
``` 
```
source venv/Scripts/activate
```

3. Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

4. В папке с файлом manage.py выполните миграции:
```
python manage.py migrate
```

5. В папке с файлом manage.py запустите сервер, выполнив команду:
```
python manage.py runserver
```

### *Что могут делать пользователи*:

**Авторизованные** пользователи могут:
1. Просматривать, страницу со всеми товарами;
2. Просматривать, страницу с отдельной категорией товаров;
3. Заходить в свой профиль *(редактировать свои данные)*;
4. Добавлять и удалять товары **свои** из корзины;
***Примечание***: Доступ ко всем операциям доступны только после аутентификации и авторизации.

**Неавторизованные :alien:** пользователи могут:
1. Просматривать, страницу со всеми товарами;
2. Просматривать, страницу с отдельной категорией товаров;
3. Авторизовываться;
4. Регистрироваться;


### **Набор доступных эндпоинтов** :point_down:_:
* ```users/login/``` - Вводим логи и пароль (_авторизация_);
* ```users/register/``` - регистрируемся (_регистрация_);
* ```users/profile/``` - заходим в профиль (_профиль авторизованного пользователя и корзина_);
* ```users/logout/``` - выход;
* ```/``` - Отображение основной страницы (_начать покупки и выбор каталога товаров_);
* ```products/``` - Отображение каталога товаров (_цен, описания, добавления в корзину_);
* ```products/{id}``` - Получение, определенного товара из категории (_одежда, рюкзаки, головные уборы и тд_);
* ```products/page/{id}```- Получение, определенного товара из категории (_пагинация_);

