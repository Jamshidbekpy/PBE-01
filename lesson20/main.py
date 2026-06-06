# from abc import ABC, abstractmethod

# class Avto(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass
#     @abstractmethod
#     def stop_engine(self):
#         pass
#     @abstractmethod
#     def move(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
    
    
    
    

    
    
# class Car(Avto):
#     def start_engine(self):
#         print("Car engine started.")
#     def stop_engine(self):
#         print("Car engine stopped.")
#     def move(self):
#         print("Car is moving.")
#     def stop(self):
#         print("Car has stopped.")
       
       
       
# car1 = Car()
# car1.stop_engine()
# car1.move()
# car1.stop() 
        
# class Motorcycle(Avto):
#     def start_engine(self):
#         print("Motorcycle engine started.")
#     def stop_engine(self):
#         print("Motorcycle engine stopped.")
#     def move(self):
#         print("Motorcycle is moving.")
#     def stop(self):
#         print("Motorcycle has stopped.")


# Parent class
# class Animal:
#     def __init__(self, name):
#         self.name = name  # 👉 Parent class attributi

#     def speak(self):
#         print(f"{self.name} is making a sound.")

# # Child class
# class Dog(Animal):  # Animal klassidan meros olyapti
    
#     def bark(self):
#         print(f"{self.name} is barking!")

# # Obyekt yaratamiz
# dog1 = Dog("Bobik")

# dog1.speak()  # 👉 Parent class metodidan foydalanish
# dog1.bark()   # 👉 Child class metodidan foydalanish


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary  # protected

#     def display_salary(self):
#         print(f"Salary: {self.salary}")
        
        
# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self._department = department  # protected

#     def salaryt(self):
#         return super().display_salary()
    
    
# m = Manager("John", 5000, "HR")
# m.display_salary()
# m.salaryt()
        
    
        
# a = [1, 2, 3, 4, 5]
# b = a
# c = b

# a.append(6)



# # import copy

# # class Student:
# #     def __init__(self, name, scores):
# #         self.name = name
# #         self.scores = scores  # ichki ro'yxat

# # student1 = Student("Ali", [90, 80])    
# # student2 = copy.deepcopy(student1)  # student2 = copy(student1)

# # student2.scores.append(70)
# # print(student1.scores)  # 👉 [90, 80, 70] — asl obyekt ham o‘zgardi

# # print(student2.scores)  # 👉 [90, 80, 70] — yangi obyektning ro'yxati ham o'zgardi


# class Person:
#     people = []

#     def __init__(self, name):
#         self.name = name
#         Person.people.append(self)

#     @classmethod
#     def total_people(cls):  # cls = classning o‘zi
#         return len(cls.people)
    
#     @property   
#     def get_name(self):
#         return self.name
    
#     @staticmethod
#     def greet():
#         return "Hello! Welcome to the Person class."
    

# p1 = Person("Ali")
# p2 = Person("Vali")
# p3 = Person("Guli")
# print(Person.total_people())  # 👉 3

# print(p1.get_name)  # 👉 Ali


# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b

# s = Math()
# print(s.add(3, 5))  # 👉 8
# print(Math.add(3, 5))  # 👉 8



# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.age = 20

#     def __str__(self):
#         return f"Person({self.name}, {self.age})"
    
#     # def __del__(self):
#     #     print(f"{self.name} yo'q qilindi.")
    
#     def __repr__(self):
#         return f"Person({self.name}, {self.age})"
    
        
# class MyList:
#     def __init__(self, items):
#         self.items = items

#     def __len__(self):
#         return len(self.items)

# my_list = MyList([1, 2, 3])
# print(len(my_list))  # 3


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
    
#     def __sub__(self, other):
#         return Point(self.x - other.x, self.y - other.y)

# p1 = Point(2, 3)
# p2 = Point(4, 5)
# result = p1 + p2
# print(result.x, result.y)  # 6 8

# result2 = p1 - p2
# print(result2.x, result2.y)  # -2 -2

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
    
#     def __lt__(self, other):
#         return (self.x + self.y) < (other.x + other.y)

# p1 = Point(2, 3)
# p2 = Point(2, 3)
# p3 = Point(4, 5)
# print(p1 == p2)  # True
# print(p1 == p3)  # False
# print(p1 < p3)   # True
# print(p3 < p1)   # False


class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

my_list = MyList([1, 2, 3])
print(my_list[1])  # 2







    

   