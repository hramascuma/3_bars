# Ближайшие бары

Скрипт bars обрабатывает базу данных московских баров и рассчитывает:
1. самый большой бар;
2. самый маленький бар;
3. самый близкий бар (текущие gps-координаты пользователь введет с клавиатуры).

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py # # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы

# в процессе выполнения скрипта, вас попросят ввести данные геолокации и выбор из трех предложенных вариантов, после чего на экран выведет всю информацию по данному бару. 
Пример вывода:

{
    "geometry": {
        "coordinates": [
            37.638228500803905,
            55.70111462924677
        ],
        "type": "Point"
    },
    "properties": {
        "Attributes": {
            "Address": "Автозаводская улица, дом 23, строение 1",
            "AdmArea": "Южный административный округ",
            "District": "Даниловский район",
            "IsNetObject": "нет",
            "Name": "Спорт бар «Красная машина»",
            "OperatingCompany": null,
            "PublicPhone": [
                {
                    "PublicPhone": "(905) 795-15-84"
                }
            ],
            "SeatsCount": 450,
            "SocialPrivileges": "нет",
            "global_id": 637548020
        },
        "DatasetId": 1796,
        "ReleaseNumber": 3,
        "RowId": "1324c45d-8e2a-4f48-8276-22aa5d539175",
        "VersionNumber": 2
    },
    "type": "Feature"
}
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
