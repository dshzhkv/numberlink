# Zuma

## Описание
Данное приложение является реализацией компьютерной игры «Zuma Deluxe».

Автор: Жукова Дарья

## Требования
* Python 3.8
* pygame

## Состав
* Интерфейс: `UI/`
* Приложение: `Application/`
* Примеры полей в папке `examples`
* Тесты в папке `Tests`
* Запуск: `main.py`

## Запуск: 

### Формат поля
Для запуска необзодим txt файл с полем. Данно еприложение умеет решать прямоугольные (квадратные) и шестиугольные поля.

Пример файла для прямоугольного поля:
3 3 (ширина и высота поля - целые положительные числа)
2 1 #
# 2 1
3 # 3
(# - пустая клетка)

Пример файла для шестиугольного поля:
5 (высота поля - целое положительное нечетное число)
1 2
1 # #
3 # 3 2
4 # #
# 4

или

5
  1 2
 1 # #
3 # 3 2
 4 # #
  # 4
  
### Пример запуска

Для прямоугольного поля:
`python main.py examples/6.txt`

Для шестиугольного поля:
`python main.py -s examples/2_h.txt`

## Подробности реализации

* `Application/Instance.py` содержит класс `Instance` - сущность головоломки
* `Application/Solver.py` решает головоломку
*  В `Application/Structures.py`  вспомогательные классы

## Тестирование
`test_application.py` тестирует модуль `Application`. Покрытие строк - 100%
`test_ui.py` тестирует модуль `UI`. Покрытие строк - 83
