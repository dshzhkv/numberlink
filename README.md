# numberlink

## Описание
Консольное приложение, решающее головоломку Numberlink.

Автор: Жукова Дарья

## Требования
* Python 3.8

## Состав
* Интерфейс: `UI/`
* Приложение: `Application/`
* Примеры полей: `examples/`
* Тесты: `Tests/`
* Запуск: `main.py`

## Запуск: 

### Формат поля
Для запуска необзодим txt файл с полем. Данное приложение умеет решать прямоугольные (квадратные) и шестиугольные поля.

**Формат файла для прямоугольного поля:** </br>
В первой строке ширина j и высота i поля - целые положительные числа.</br>
В следующих i строках по j элементов поля через пробел.</br>
\# - пустая клетка.

**Формат файла для шестиугольного поля:**</br>
В первой строке высота поля i- целое положительное нечетное число.</br>
В следующих i строках элементы поля через пробел. Ширина строки увеличивается на 1 символ до серередины поля и после уменьшается на 1 символ. В первой и последней строках по 2 символа. </br>
\# - пустая клетка.

Примеры полей в папке `examples`
  
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
