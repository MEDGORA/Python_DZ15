"""В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:

Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число) Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным положительным целым числом.

Ваша задача:

Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.

Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID). Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.

Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.

Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).

Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно при передаче неверных данных."""

#person = Person("", "John", "Doe", 30)
#print(person)

import datetime
import logging
import argparse


class Person:
    def __init__(self, second_name: str, name: str, last_name: str, age: int):

        MIN_AGE = 18
        MAX_AGE = 100

        self.second_name = second_name
        if type(self.second_name) is not str or self.second_name == "" :
            logging.error(f"{datetime.datetime.now()} {InvalidNameError(self.second_name)}")
            raise InvalidNameError(self.second_name)
        self.name = name
        if type(self.name) is not str or self.name == "" :
            logging.error(f"{datetime.datetime.now()} {InvalidNameError(self.name)}")
            raise InvalidNameError(self.name)
        self.last_name = last_name
        if type(self.last_name) is not str or self.last_name == "" :
            logging.error(f"{datetime.datetime.now()} {InvalidNameError(self.last_name)}")
            raise InvalidNameError(self.last_name)
        self.age = age
        if type(self.age) is not int or self.age < MIN_AGE or self.age > MAX_AGE:
            logging.error(f"{datetime.datetime.now()} {InvalidAgeError(self.age)}")
            raise InvalidAgeError(self.age)
        
        logging.info(f"{datetime.datetime.now()} Cоздали объект класса Person с параметрами: {self.second_name}, {self.name}, {self.last_name}, {self.age}")

    def __str__(self):
        logging.info(f"{datetime.datetime.now()} Вывели строковое представление объекта класса Person с параметрами: {self.second_name}, {self.name}, {self.last_name}, {self.age}")
        return f'ФИО : {self.second_name} {self.name} {self.last_name}. Возраст : {self.age}'
    
    def birthday(self) :
        logging.info(f"{datetime.datetime.now()} Применили метод birthday() к объекту класса Person с параметрами: {self.second_name}, {self.name}, {self.last_name}, {self.age}")
        self.age += 1
        return self.age
    
    def get_age(self):
        logging.info(f"{datetime.datetime.now()} Вернули возраст объекта класса Person с параметрами: {self.second_name}, {self.name}, {self.last_name}, {self.age}")
        return self.age
    
class Employee(Person):
    def __init__(self, second_name: str, name: str, last_name: str, age: int, ID : int):

        MIN_ID = 1
        MAX_ID = 999999999999
        MIN_AGE = 18
        MAX_AGE = 100

        self.second_name = second_name
        if type(self.second_name) is not str or self.second_name == "" :
            logging.error(f"{datetime.datetime.now()} {InvalidNameError(self.second_name)}")
            raise InvalidNameError(self.second_name)
        self.name = name
        if type(self.name) is not str or self.name == "" :
            logging.error(f"{datetime.datetime.now()} {InvalidNameError(self.name)}")
            raise InvalidNameError(self.name)
        self.last_name = last_name
        if type(self.last_name) is not str or self.last_name == "" :
            logging.error(f"{datetime.datetime.now()} {InvalidNameError(self.last_name)}")
            raise InvalidNameError(self.last_name)
        self.age = age
        if type(self.age) is not int or self.age < MIN_AGE or self.age > MAX_AGE:
            logging.error(f"{datetime.datetime.now()} {InvalidAgeError(self.age)}")
            raise InvalidAgeError(self.age)
        self.ID = ID
        if type(self.ID) is not int or self.ID < MIN_ID or self.ID > MAX_ID:
            logging.error(f"{datetime.datetime.now()} {InvalidError(self.ID)}")
            raise InvalidError(self.ID)
        
        logging.info(f"{datetime.datetime.now()} Cоздали объект класса Employee с параметрами: {self.second_name}, {self.name}, {self.last_name}, {self.age}, {self.ID}")
        

    def __str__(self):
        logging.info(f"{datetime.datetime.now()} Вывели строковое представление объекта класса Employee с параметрами: {self.second_name}, {self.name}, {self.last_name}, {self.age}")
        return f'ФИО : {self.second_name} {self.name} {self.last_name}. Возраст : {self.age}. ID : {self.ID}'
    
    def get_level(self) :
        sum = 0
        for i in range(len(str(self.ID))):
            sum += int(str(self.ID)[i])
        level = sum % 7
        logging.info(f"{datetime.datetime.now()} Вернули уровень объекта класса Employee с параметрами: {self.second_name}, {self.name}, {self.last_name}, {self.age}, {self.ID}")
        return level

    
class InvalidNameError(Exception) :
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Invalid name: {self.value}. Name should be a non-empty string."
    
class InvalidAgeError(Exception) :
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Invalid age: {self.value}. Age should be a positive integer."
    
class InvalidError(Exception) :
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Invalid number: {self.value}. Number should be a positive integer."
    


logging.basicConfig(
    filename="task_loggin",
    encoding="utf-8",
    level=logging.INFO
)


if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="Создаёт обект person класса Person(second_name: str, name: str, last_name: str, age: int)")
    parser.add_argument("second_name", metavar="second_name", type= str, help="Введите фамилию, тип str")
    parser.add_argument("name", metavar="name", type= str, help="Введите имя, тип str")
    parser.add_argument("last_name", metavar="last_name", type= str, help="Введите отчество, тип str")
    parser.add_argument("age", metavar="age", type= int, help="Введите возраст, тип int")
    args = parser.parse_args()
    person = Person(args.second_name, args.name, args.last_name, args.age)
    print(person)
    

