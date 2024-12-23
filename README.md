# -9-Python-Object-Oriented-Programming-OOP
## Python Объектно-ориентированное программирование (ООП)

<img src="https://github.com/TeachKait20/NoneCode/blob/main/OOP+python/img1.gif?raw=true" width="400">

**Объектно-ориентированное программирование** — это парадигма программирования, которая основывается на концепции объектов. <br><br>
**Объекты** — это экземпляры классов, которые объединяют данные (атрибуты) и методы (функции, работающие с данными).

## Парадигма ООП

<img src="https://github.com/TeachKait20/NoneCode/blob/main/OOP+python/img2.gif?raw=true" width="400">

Начнём с понятий. Объектно-ориентированное программирование выстраивается на объектно-ориентированной парадигме. <br><br>
**Парадигма** — это способ мышления или подход к решению задач, который определяет, как мы видим и структурируем проблему. <br><br>
В контексте программирования парадигма — это стиль или модель написания кода, которая задаёт правила и принципы для разработки. Например:
* **Императивное программирование** - описывает шаги, которые компьютер должен выполнить. Сюда относятся процедурное программирование и работа с циклами.
* **Функциональное программирование** - акцент на чистые функции и избегание изменения состояния.
* **Объектно-ориентированное программирование (ООП)** - организация кода вокруг объектов, которые содержат данные и методы для работы с этими данными.

## Пример объектно-ориентированной парадигмы и чем она полезна

<img src="https://github.com/TeachKait20/NoneCode/blob/main/OOP+python/main_street.png?raw=true">

Например, есть длинная улица, на которой стоят дома. Детально, в голове, вы сможете рассмотреть всего 1 - 3 дома. Но представить множества домов со всеми шероховатостями вы не сможете. Для этого, мы рассматриваем их по отдельности. Это и есть модель объектно-ориентированной парадигмы.

В примере:
* Каждый дом — это объект, который может быть частью множества объектов (набор домов).
* Мы не обязаны помнить все детали каждого дома, достаточно знать общую структуру (например, у всех домов есть стены, крыша и окна). Эта структура — это класс, а каждый отдельный дом — это экземпляр этого класса.
* Если нужно уточнить детали, мы обращаемся к атрибутам (например, цвет крыши, количество этажей) или к методам (например, "покрасить дом", "открыть дверь").

## Основные элементы ООП

<img src="https://github.com/TeachKait20/NoneCode/blob/main/OOP+python/img3.gif?raw=true" width="400">

### Классы

**Классы** — шаблоны, по которым создаются объекты. <br>
**Атрибуты** — переменные, которые хранят состояние объекта. <br>
**Методы** — функции, определенные внутри классов.

Заложим за основу класса улицу в городе и добавим ей описание:

```python
class Street():
    def __init__(self, street_name, num_houses):
        self.street_name = street_name  # Атрибуты класса
        self.num_houses = num_houses

    def get_info_street(self):  # Метод класса
        return f"Street name: {self.street_name}, Number of houses: {self.num_houses}"
```
В данном случае, в сам класс будут переданы аргументы для её названия и количества домов. <br><br>
Ключевое слово `self` используется в методах класса для ссылки на текущий экземпляр класса, через который вызывается метод. Оно служит для того, чтобы получать и устанавливать атрибуты объекта, а также вызывать другие методы этого же объекта. <br><br>
Чтобы управлять данной улицей ещё больше (а именно расширить функционал), можно добавить ещё методов.
```python
class Street():
    def __init__(self, street_name, num_houses):
        self.street_name = street_name  # Атрибуты класса
        self.num_houses = num_houses

    def get_info_street(self):  # Метод класса для получения информации
        return f"Street name: {self.street_name}, Number of houses: {self.num_houses}"

    def add_house(self, num=1):  # Метод класса для добавления домов
        self.num_houses += num

    def remove_house(self, num=1):  # Метод класса для удаления домов
        if self.num_houses - num >= 0:
            self.num_houses -= num
        else:
            print("Cannot have negative houses!")
```

### Объекты

**Объекты** — экземпляры классов.

```python
class Street():
    def __init__(self, street_name, num_houses):
        self.street_name = street_name  # Атрибуты класса
        self.num_houses = num_houses

    def get_info_street(self):  # Метод класса для получения информации
        return f"Street name: {self.street_name}, Number of houses: {self.num_houses}"

    def add_house(self, num=1):  # Метод класса для добавления домов
        self.num_houses += num

    def remove_house(self, num=1):  # Метод класса для удаления домов
        if self.num_houses - num >= 0:
            self.num_houses -= num
        else:
            print("Cannot have negative houses!")

main_street = Street("Main Street", 20)  # main_street - объект класса (как обычная переменная)
print(main_street.get_info_street())  # Вывод: Street name: Main Street, Number of houses: 20

main_street.add_house(5)
print(main_street.get_info_street())  # Вывод: Street name: Main Street, Number of houses: 25

main_street.remove_house(30)  # Вывод: Cannot have negative houses!
```
Обязательно просмотрите файл [street.py](https://github.com/TeachKait20/-9-Python-Object-Oriented-Programming-OOP/blob/main/street.py). В нём будет дополнительная информация. 
