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

## Пример 1

Рассмотрим программу, моделирующую работу железнодорожной станции. Она предоставляет функционал для управления поездами и станциями. Состоит из класса `Railway_Station`, который объединяет данные и методы, связанные с железнодорожными станциями и расписанием поездов.

```python
class Railway_Station():
    all_stations = ["Ближняя", "Малиновка", "Суетино", "Носово", "Внуково", "Путь-33", "Грачёво", "Дальняя",
                    "СНТ-15", "Зелёный лес", "Стулово", "Железняково", "Островки", "Майнино", "Акулово-1"]

    def __init__(self, number_train: int, model_train: str, departure_time: str, train_path: int, last_station: int):
        """
        Информация о новом поезде для экземпляров класса:

           number_train - (int) номер поезда. > 0
           model_train - (str) название поезда. 'Name'
           departure_time - (str) время отбытия. '12:34'
           train_path - (int) путь №. > 0
           last_station - (int) выбор из списка all_stations, отсчёт с 1. > 0 и < длины all_stations
        """

        self.number_train = number_train  # Номер поезда
        self.model_train = model_train  # Модель поезда
        self.departure_time = departure_time
        self.train_path = train_path  # Пусть уезда

        # Проверка на правильность ввода индекса (есть ли столько элементов в all_stations)
        try:
            self.last_station = self.all_stations[last_station - 1]  # Номер конечной станции из списка all_stations
        except IndexError:
            self.last_station = None  # Устанавливаем в None, если индекс некорректен

    def show_information_to_passengers(self):
        """Информация о поездах для пассажиров"""
        if self.last_station:  # Проверяем, есть ли корректная станция
            print(f"Поезд {self.model_train} №{self.number_train} отправляется в {self.departure_time} "
                  f"с {self.train_path} пути до станции {self.last_station}.\n")
        else:
            print(f"Информация о поезде {self.model_train} №{self.number_train} недоступна из-за ошибки выбора станции.\n")

    @classmethod
    def del_station(self):
        print("Все станции: ")
        for num, station in enumerate(self.all_stations):
            print(f"{num + 1}: {station}")
        print()
        print("Введите название станции, которую нужно удалить.")
        del_station = input('> ')
        if del_station in self.all_stations:
            self.all_stations.remove(del_station)
            for num, station in enumerate(self.all_stations):
                print(f"{num + 1}: {station}")
            print()
        else:
            print("Такой станции нет в списке.")

    @classmethod
    def add_station(self):
        print("Все станции: ")
        for num, station in enumerate(self.all_stations):
            print(f"{num+1}: {station}")
        print()
        print("Введите название станции, которую нужно добавить.")
        new_station = input('> ')
        if new_station not in self.all_stations:
            print(f"Введите какая по счёту должна быть станция {new_station}")
            num_station = input("> ")
            try:
                num_station = int(num_station) - 1
            except ValueError:
                print("Ошибка. Введено не число.")
            else:
                if num_station <= 0:
                    print("Станции начинаются с 1.")
                else:
                    self.all_stations.insert(num_station, new_station)
                    for num, station in enumerate(self.all_stations):
                        print(f"{num + 1}: {station}")
                    print()
        else:
            print("Станция уже есть в списке.")


train_1 = Railway_Station(703, 'Ласточка', '10:00', 11, 7)
train_1.show_information_to_passengers()

train_2 = Railway_Station(690, 'дальнего следования', '00:30', 3, 100)
train_2.show_information_to_passengers()

admin_1 = Railway_Station.add_station()
admin_2 = Railway_Station.del_station()
```
**Основные части программы**
**1.** Класс `Railway_Station` <br>
Класс содержит информацию о поездах, списке станций и предоставляет методы для работы с ними.

**2.** Атрибуты класса <br>
`all_stations` - список всех доступных станций. Это общий атрибут для всех экземпляров класса.

**3.** Методы класса и экземпляра <br>

* `__init__(...)`: <br>

Инициализирует новый поезд с его номером, моделью, временем отправления, номером пути и конечной станцией.
Если переданный индекс конечной станции некорректен, устанавливает её значение в `None`.

* `show_information_to_passengers()`: <br>

Показывает информацию для пассажиров о конкретном поезде: номер, модель, время отправления, путь и конечная станция. Если информация некорректна (например, неверно указана конечная станция), выводится предупреждение.
Методы класса:

* `add_station()`: <br>

Позволяет добавить новую станцию в общий список `all_stations`.
Просит пользователя указать:
Название новой станции.
Порядковый номер, под которым станция должна быть добавлена.
Обрабатывает ошибки (например, некорректный ввод номера или добавление уже существующей станции).
Выводит обновлённый список станций.

* `del_station()`: <br>

Позволяет удалить станцию из списка `all_stations`.
Показывает пользователю текущий список станций с порядковыми номерами.
Просит ввести название станции для удаления.
Если станция найдена, удаляет её и показывает обновлённый список. В противном случае выводит сообщение об ошибке.

**4.** Пример использования <br>

Создаются два экземпляра класса `Railway_Station`, которые представляют поезда: <br>
`train_1` — поезд с корректной информацией о конечной станции. <br>
`train_2` — поезд с некорректной конечной станцией (передан индекс вне диапазона). <br>
Информация о поездах выводится с помощью метода `show_information_to_passengers`. <br>
Методы класса `add_station` и `del_station` используются для добавления и удаления станций, соответственно. <br>
