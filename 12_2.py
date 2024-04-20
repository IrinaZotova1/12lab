import random
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Кухня: {self.cuisine_type}")

    def open_restaurant(self):
        res = random.randint(0, 1)
        if res == 1:
            res1 = "открыт"
        else:
            res1 = "закрыт"
        print(f"Ресторан {self.restaurant_name} {res1}")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, location, hours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        self.location = location
        self.hours = hours

    def display_flavors(self):
        print("Сорты мороженого:")
        for flavor in self.flavors:
            print(flavor)

    def add_flavor(self, flavor1):
        self.flavors.append(flavor1)
        print(f"{flavor1} сорт добавлен в меню")

    def remove_flavor(self, flavor2):
        if flavor2 in self.flavors:
            self.flavors.remove(flavor2)
            print(f"{flavor2} удалено из меню")
        else:
            print(f"{flavor2} нет в меню")

    def check_flavor(self, flavor3):
        if flavor3 in self.flavors:
            print(f"{flavor3} в наличии")
        else:
            print(f"{flavor3} нет в наличии")

    def add_ice_cream_type(self, ice_cream_type):
        print(f"{ice_cream_type} добавлено в меню")

    def remove_ice_cream_type(self, ice_cream_type):
        print(f"{ice_cream_type} удалено из меню")

    def update_hours(self, new_hours):
        self.hours = new_hours
        print(f"Часы работы: {self.hours}")


# Создаем экземпляр с именем newRestaurant
Restaurant1 = Restaurant("Метрополь", "русская")

# Вызываем оба метода
Restaurant1.describe_restaurant()
Restaurant1.open_restaurant()

# Создаем экземпляр IceCreamStand
icecream_stand = IceCreamStand("Сладкое королевство", "десерты", "Театральный проспект 2", "10-19")

# Добавляем и удаляем сорта мороженого
kolvo_sorts1=int(input("Cколько сортов мороженого вы хотите ввести? "))
for i in range(0, kolvo_sorts1):
    flavour1 = input("Введите новый сорт мороженого: ")
    icecream_stand.add_flavor(flavour1)
icecream_stand.display_flavors()

kolvo_sorts2=int(input("Сколько сортов мороженого вы хотите удалить? "))
for i in range(0, kolvo_sorts2):
    flavour2=input("Введите сорт мороженого, который хотите удалить: ")
    icecream_stand.remove_flavor(flavour2)
icecream_stand.display_flavors()


check=input("Хотите проверить наличие какого-то сорта мороженого?(да/нет) ")
if check=="да":

# Проверяем наличие определенного сорта мороженого
    flavour3=input("Введите сорт мороженого, наличие которого вы хотите проверить: ")
    icecream_stand.check_flavor(flavour3)


# Добавляем новый тип мороженого
kolvo_types=int(input("Сколько новый типов мороженого вы хотите добавить? "))
for i in range(0, kolvo_types):
    ice_cream_type=input("Введите новый тип мороженого: ")
    icecream_stand.add_ice_cream_type(ice_cream_type)

# Обновляем часы работы
new_hours=input("Введите новые часы работы: ")
icecream_stand.update_hours(new_hours)