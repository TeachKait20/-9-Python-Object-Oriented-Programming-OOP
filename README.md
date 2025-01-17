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

## Пример

<img src="https://github.com/TeachKait20/NoneCode/blob/main/OOP+python/img5.gif?raw=true" width="400">

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

Конструктор для задания начальных параметров. Инициализирует новый поезд с его номером, моделью, временем отправления, номером пути и конечной станцией.
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

## Задания для самостоятельного выполнения

<img src="https://github.com/TeachKait20/NoneCode/blob/main/OOP+python/img4.gif?raw=true" width="400">

## Задание 1

Реализуйте класс Create_Personage, который будет представлять персонажа. Класс должен иметь следующие атрибуты:

* name_pers (строка) — имя персонажа.
* class_pers (строка) — класс персонажа (например, маг, воин, стрелок).
* hp_pers (целое число) — количество жизней у персонажа.
* damage_pers (целое число) — урон, который персонаж может наносить.

Добавьте в класс методы:

* print_info() — выводит информацию о персонаже в формате:
```
Имя: <имя персонажа>
Класс: <класс персонажа>
Жизни: <количество жизней>
Урон: <урон персонажа>
```
* go_on_a_trip() — выводит сообщение о том, что персонаж отправился в путешествие.
* go_back() — выводит сообщение о том, что персонаж возвращается назад.
* start_training() — выводит сообщение о начале тренировки. Тренировка увеличивает его параметры (например, урон или жизни).
* start_the_battle() — выводит сообщение о том, что персонаж готовится к сражению, и отображает его текущие характеристики.

Каждый метод должен выводить информацию.

Создайте объект персонажа с любыми атрибутами (имя, класс, жизни, урон). Например:
```python
pers_1 = Create_Personage("Игорь", "Боец", 99, 15)
```
Проведите тесты методов:
```python
pers_1 = Create_Personage("Игорь", "Боец", 99, 15)
pers_1.print_info()  # Выводим начальные показатели
pers_1.go_on_a_trip()  # Отправляем в путешествие
pers_1.go_back()  # Возвращаем назад
pers_1.start_training()  # Начинаем тренировку. Она даст +5 к урону и +3 к жизням
pers_1.print_info()  # Выводим показатели после тренировки
pers_1.start_the_battle()  # Начинаем битву
```
На выходе получим:
```
Имя: Игорь
Класс: Боец
Жизни: 99
Урон: 15

Персонаж Игорь отправился в путешествие и пока недоступен.

Персонаж Игорь возвращается назад.

Персонаж Игорь начал тренировку. Некоторое время он не будет доступен, однако станет сильнее!

Имя: Игорь
Класс: Боец
Жизни: 102
Урон: 20

Персонаж Игорь хочет начать сражаться!
Его показатели: Жизни: 102 и урон: 20
```
## Задание 2

Перед вами программа, моделирующая работу с классом `Room`, который представляет комнату с набором предметов. 

![image](https://github.com/user-attachments/assets/117d0d0c-8c6e-4d1b-a39c-fe40b6e7a082)

Создадим экземпляр класса, применим методы и протестируем:
```python
room1 = Room("Кухня")
room1.add_item("Холодильник", "Стул", "Стол")
room1.print_items()
room1.del_item("Стул")
```
На выходе получим:
```
Все предметы в комнате Кухня: Холодильник, Стул, Стол
Все предметы в комнате: Холодильник, Стол
```
Ваша задача переписать и расширить эту программу, добавив новые возможности и протестировав работу с несколькими комнатами. <br><br>
Вариантов методов, которые можно добавить в класс `Room`, чтобы расширить его функциональность (названия могут быть любыми). <br><br>
**Выберете один из вариантов:**
1. Методы взаимодействия с предметами:
- find_item(item) — проверить, находится ли указанный предмет в комнате.
- count_items() — вернуть количество предметов в комнате.
- clear_items() — удалить все предметы из комнаты.
- replace_item(old_item, new_item) — заменить один предмет другим.
- move_item_to(item, another_room) — перенести предмет в другую комнату.
2. Методы для взаимодействия с комнатой:
- rename_room(new_name) — переименовать комнату.
- describe_room() — вывести описание комнаты с её именем и списком предметов.
- merge_rooms(another_room) — объединить содержимое двух комнат.
- is_empty() — проверить, пустая ли комната.
- get_room_size() — вернуть площадь комнаты (можно задавать площадь как дополнительный атрибут).
3. Методы управления доступом:
- lock_room() — закрыть комнату (запретить добавление/удаление предметов).
- unlock_room() — открыть комнату для изменений.
- is_locked() — проверить, закрыта ли комната.
4. Методы с фильтрацией:
- filter_items_by_keyword(keyword) — вернуть список предметов, содержащих указанный ключ (например, "стол").
- get_items_starting_with(letter) — вернуть все предметы, которые начинаются на определённую букву.
5. Методы с подсчётами:
- count_specific_item(item) — подсчитать, сколько раз определённый предмет встречается в комнате.
- list_items_by_type(item_type) — разделить предметы по типам (например, мебель, техника и т. д.).
6. Методы декора:
- add_decor(item) — добавить декоративный элемент (например, картину, ковёр).
- set_theme(theme) — установить тематику комнаты (например, "современная", "классическая").
- show_theme() — вывести текущую тематику комнаты.

## Задание 3

Создайте класс, который должен содержать: 
* Конструктор для задания начальных параметров.
* Минимум 3-4 метода, в каждом должна быть проверка.
* Использование атрибутов экземпляра класса.
* Пример работы программы с 2-3 объектами вашего класса.

**Варианты классов:**

**1. Книга** <br>

Атрибуты: название, автор, количество страниц, год издания. <br>
Методы: показать информацию о книге, обновить количество страниц, проверить, является ли книга старше заданного года. <br>

**2. Студент** <br>

Атрибуты: имя, курс, средний балл. <br>
Методы: повысить курс, добавить балл, проверить, может ли студент быть стипендиатом. <br>

**3. Автомобиль** <br>

Атрибуты: марка, модель, пробег, год выпуска. <br>
Методы: показать информацию, обновить пробег, проверить, является ли автомобиль новым (пробег < 10 000). <br>

**4. Игровой персонаж** <br>

Атрибуты: имя, уровень, здоровье, атака. <br>
Методы: нанести урон, восстановить здоровье, проверить, жив ли персонаж. <br>

**5. Телефон** <br>

Атрибуты: бренд, модель, ёмкость аккумулятора, заряд. <br>
Методы: зарядить телефон, потратить заряд, проверить, разрядился ли телефон. <br>

**6. Фильм** <br>

Атрибуты: название, режиссёр, рейтинг, год выхода. <br>
Методы: показать информацию, изменить рейтинг, проверить, популярный ли фильм (рейтинг > 8). <br>

**7. Продукт** <br>

Атрибуты: название, цена, количество. <br>
Методы: изменить цену, обновить количество, проверить, доступен ли товар на складе. <br>

**8. Ресторан** <br>

Атрибуты: название, тип кухни, рейтинг, количество столиков. <br>
Методы: забронировать столик, изменить рейтинг, проверить, есть ли свободные столики. <br>

**9. Пользователь** <br>

Атрибуты: имя, возраст, email. <br>
Методы: обновить email, проверить возраст. <br>

**10. Счёт в банке** <br>

Атрибуты: владелец, баланс, валюта. <br>
Методы: пополнить счёт, снять деньги, проверить остаток. <br>

**11. Футбольная команда** <br>

Атрибуты: название, город, количество игроков, победы. <br>
Методы: добавить игрока, увеличить число побед, показать статистику. <br>

**12. Домашнее животное** <br>

Атрибуты: кличка, вид, возраст. <br>
Методы: изменить возраст, показать информацию, проверить, нуждается ли животное в ветеринаре. <br>

**13. Компьютер** <br>

Атрибуты: процессор, оперативная память, объём накопителя. <br>
Методы: добавить оперативную память, изменить объём накопителя, показать конфигурацию. <br>

**14. Товар в интернет-магазине** <br>

Атрибуты: название, категория, цена, рейтинг. <br>
Методы: обновить цену, изменить рейтинг, проверить, доступен ли товар для покупки. <br>

**15. Почтовая посылка** <br>

Атрибуты: трек-номер, отправитель, получатель, статус. <br>
Методы: изменить статус, показать данные, проверить, доставлена ли посылка. <br>

**16. Фигуры на плоскости** <br>

Атрибуты: тип фигуры (круг, квадрат), координаты центра, размер. <br>
Методы: изменить координаты, изменить размер, вычислить площадь фигуры. <br>

**17. Чат-комната** <br>

Атрибуты: название, список участников, количество сообщений. <br>
Методы: добавить участника, отправить сообщение, показать статистику чата. <br>

**18. Космический корабль** <br>

Атрибуты: название, экипаж, запас топлива, дальность полёта. <br>
Методы: пополнить топливо, отправиться в полёт, проверить, достиг ли корабль цели. <br>

**19. Музыкальный альбом** <br>

Атрибуты: название, исполнитель, количество треков, год выпуска. <br>
Методы: добавить трек, показать информацию об альбоме, проверить, является ли альбом современным (выпущен за последние 5 лет). <br>

**20. Станция метро** <br>

Атрибуты: название станции, номер линии, количество пассажиров в день. <br>
Методы: изменить количество пассажиров, показать информацию о станции, проверить, является ли станция загруженной (> 100 000 пассажиров в день). <br>
