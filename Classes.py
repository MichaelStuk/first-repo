# class Dog:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         return(f'{self.name} is barking')
#     def all_data(self):
#         return(self.name, self.age)

# my_dog = Dog('Teo', 3)
# print(my_dog.age)
# print(my_dog.name)
# my_second_dog = Dog('Elsa', 6)
# print(my_second_dog.age)
# print(my_second_dog.name)
# print(my_dog.bark())
# print(list(my_dog.all_data()))

# class Car:
#     def __init__(self,brand,color,year):
#         self.brand = brand
#         self.color = color
#         self.year = year
#     def drive(self):
#         return(f'{self.color} {self.brand} is driving!')
        
# car1 = Car('Tesla','Red',2024)
# print(car1.drive())

# class Students:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#     def study(self):
#         return(f'Student {self.name} is studying for grade {self.grade}')
    
# student1 = Students('Michael', 8)
# print(student1.study())

# class BankAccount:
#     def __init__(self, owner):
#         self.owner = owner
#         self.balance = 0
#     def deposit(self,amount):
#         self.balance += amount
#         print(f'Deposited: {amount}. New balance: {self.balance}')
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print(f'Substructed {amount} from savings!')
#         else:
#             print('Not enough money!')
#     def check_balance(self):
#         print(f'Current balance is: {self.balance}')

# account1 = BankAccount('Michael')
# account1.deposit(100)
# account1.withdraw(30)
# account1.check_balance()
# print()
# account2 = BankAccount('Jordan')
# account2.deposit(200)
# account2.withdraw(84)
# account2.check_balance()


class Character:
    def __init__(self,name,power):
        self.name = name
        self.health = 100
        self.power = power
    def attack(self, other_character):
        other_character.health -= self.power
        print(f'{self.name} attacks {other_character.name} for {self.power} damage!')
    def is_alive(self):
        if self.health >= 0:
            return True
        else:
            return False
    def status(self):
        print(f'{self.name} has {self.health} health left.')

hero = Character('Michael',20)
villian = Character('Noa', 15)
hero.attack(villian)
villian.attack(hero)
hero.status()
villian.status()
#end
