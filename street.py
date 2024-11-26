class Street:
    city = "Unknown City"  # Общий атрибут класса

    def __init__(self, street_name, num_houses):
        self.street_name = street_name  # Уникальный атрибут экземпляра
        self.num_houses = num_houses

    def get_info_street(self):
        return f"City: {Street.city}, Street name: {self.street_name}, Number of houses: {self.num_houses}"

    def add_house(self, num=1):
        self.num_houses += num

    def remove_house(self, num=1):
        if self.num_houses - num >= 0:
            self.num_houses -= num
        else:
            print("Cannot have negative houses!")

    @classmethod
    def set_city(cls, new_city):  # Работа с общим атрибутом через cls
        cls.city = new_city

    @classmethod
    def get_city(cls):
        return cls.city

    @staticmethod
    def is_valid_house_number(num):  # Проверка без обращения к классу или экземпляру
        return num > 0


# Используем classmethod для управления общим атрибутом
Street.set_city("Springfield")
print(Street.get_city())  # Вывод: Springfield

# Создаём улицу
main_street = Street("Main Street", 20)

# Получаем информацию о городе и улице
print(main_street.get_info_street())
# Вывод: City: Springfield, Street name: Main Street, Number of houses: 20

# Используем staticmethod для проверки данных
print(Street.is_valid_house_number(10))  # Вывод: True
print(Street.is_valid_house_number(-5))  # Вывод: False

# Staticmethod можно использовать и внутри других методов
if Street.is_valid_house_number(-3):
    main_street.add_house(-3)
else:
    print("Invalid house number!")  # Вывод: Invalid house number!
