import json
import logging


logging.basicConfig(
    filename="shelter.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


class Animal:

    def _init_(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.__health = 100

    def speak(self):
        return "Животное издает звук"

    def eat(self, food):
        logging.info(f"{self.name} ест {food}")
        return f"{self.name} ест {food}"

    def info(self):
        return f"Имя: {self.name}, возраст: {self.age}, вес: {self.weight}"

    def _str_(self):
        return f"{self.name} ({self.age} лет)"


class Dog(Animal):

    def speak(self):
        return "Гав!"

    def fetch(self):
        return f"{self.name} принес палку"


class Cat(Animal):

    def speak(self):
        return "Мяу!"

    def purr(self):
        return f"{self.name} мурчит"


class Parrot(Animal):

    def speak(self):
        return "Привет!"

    def repeat(self, phrase):
        return f"{self.name} повторяет: {phrase}"


class Shelter:

    def _init_(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        logging.info(f"Добавлено животное {animal.name}, возраст {animal.age}")

    def remove_animal(self, name):

        for animal in self.animals:
            if animal.name == name:
                self.animals.remove(animal)
                logging.info(f"Удалено животное {name}")
                return

        print("Животное не найдено")
        logging.error("Животное не найдено")

    def find_by_name(self, name):

        for animal in self.animals:
            if animal.name == name:
                logging.info(f"Найдено животное {name}")
                return animal

        logging.error("Животное не найдено")
        return None

    def show_all(self):

        if not self.animals:
            print("Приют пуст")

        for animal in self.animals:
            print(animal)

    def save_to_file(self):

        data = []

        for animal in self.animals:
            data.append({
                "type": animal._class.name_,
                "name": animal.name,
                "age": animal.age,
                "weight": animal.weight
            })

        with open("shelter.json", "w", encoding="utf8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        logging.info("Данные сохранены")

    def load_from_file(self):

        try:
            with open("shelter.json", "r", encoding="utf8") as f:
                data = json.load(f)

            self.animals = []

            for item in data:

                if item["type"] == "Dog":
                    animal = Dog(item["name"], item["age"], item["weight"])

                elif item["type"] == "Cat":
                    animal = Cat(item["name"], item["age"], item["weight"])

                elif item["type"] == "Parrot":
                    animal = Parrot(item["name"], item["age"], item["weight"])

                self.animals.append(animal)

            logging.info("Данные загружены")

        except FileNotFoundError:
            logging.error("Файл не найден")


shelter = Shelter()


while True:

    print("\n--- ВИРТУАЛЬНЫЙ ПРИЮТ ---")
    print("1 Добавить животное")
    print("2 Показать всех")
    print("3 Найти животное")
    print("4 Удалить животное")
    print("5 Сохранить")
    print("6 Загрузить")
    print("0 Выход")

    choice = input("Выберите действие: ")

    if choice == "1":

        t = input("Тип животного (dog/cat/parrot): ")
        name = input("Имя: ")

        try:
            age = int(input("Возраст: "))
            weight = float(input("Вес: "))
        except:
            print("Ошибка ввода")
            continue

        if t == "dog":
            animal = Dog(name, age, weight)

        elif t == "cat":
            animal = Cat(name, age, weight)

        elif t == "parrot":
            animal = Parrot(name, age, weight)

        else:
            print("Неизвестный тип")
            continue

        shelter.add_animal(animal)

    elif choice == "2":
        shelter.show_all()

    elif choice == "3":

        name = input("Введите имя: ")
        animal = shelter.find_by_name(name)

        if animal:
            print(animal.info())
        else:
            print("Не найдено")

    elif choice == "4":

        name = input("Введите имя: ")
        shelter.remove_animal(name)

    elif choice == "5":
        shelter.save_to_file()

    elif choice == "6":
        shelter.load_from_file()

    elif choice == "0":
        print("Программа завершена")
        break
