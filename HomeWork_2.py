# "Классная работа"

# class Animals:
#     def __init__(self, name):
#         self.name = name
#     def eat(self):
#         return f"{self.name} ест"
#     def sleep(self):
#         return f"{self.name} спит"
        
# class Walker:
#     def __init__(self, name, walk):
#         self.walk = walk
#         self.name = name
#     def walkk(self):
#         print(f"{self.name} {self.walk}")
        
# class Swimmer:
#     def __init__(self, name,swim):
#         self.swim = swim
#         self.name = name
#     def swi(self):
#         print(f"{self.name} {self.swim}")
        
# class Flyer:
#     def __init__(self, name, fly):
#         self.fly = fly 
#         self.name = name
#     def flye(self):
#         print(f"{self.name} {self.fly}")
        
# class Penguin(Animals, Walker, Swimmer):
#     def __init__(self, name, walk, swim):
#         self.name = name
#         self.walk = walk
#         self.swim = swim
#     def describe(self):
#         print(f"{self.name} {self.walk} и {self.swim}")
        
# class Duck(Animals,Walker,Swimmer,Flyer):
#     def __init__(self, name, walk, fly, swim):
#         self.name = name
#         self.walk = walk
#         self.swim = swim
#         self.fly = fly
#     def describe1(self):
#         print(f"{self.name} {self.walk}, {self.fly} и {self.swim}")

# class Bat(Animals,Flyer):
#     def __init__(self, name, fly):
#         self.name = name
#         self.fly = fly 
#     def describe2(self):
#         print(f"{self.name} {self.fly}")
        

# animal = Animals("Собака")
# animall = f"{animal.eat()}, {animal.sleep()}"
# print(animall)
# wal = Walker("Кошка","ходит")
# wal.walkk()
# swim = Swimmer("Акула","плавает")
# swim.swi()
# fly = Flyer("Голубь","летает")
# fly.flye()
# pen = Penguin("Пингвин","умеет ходить","плавать")
# pen.describe()
# duc = Duck("Утка", "умеет ходить", "летать", "плавать")
# duc.describe1()
# batt = Bat("Летучая мышь", "может летать")
# batt.describe2()

"Домашняя работа"

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
                
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount < 0 :
            print("Ошибка пополнение баланса, нельзя пополнить баланс отрицательной суммой")
            return
        self.__balance += amount
        
    def withdraw(self,amount):
        if amount > self.__balance :
            print("Недостаточно суммы на карте!")
            return
        self.__balance -= amount

user = input("Ведите имя: ")
account = BankAccount(12345678,0)
account.deposit(5000)
account.withdraw(5001)
# account.withdraw(500) #полностью работает

if user == 'Abdulloh':
    print("текущий баланс:", account.get_balance(),"$")
else:
    print("В баззе данных нету информации с таким именим", {user})

# try:
#     account.__balance == 1000 
# except AttributeError as e:
#     print("Ошибка:","Нелзя изменить баланс карты на примую: ", e)