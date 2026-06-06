# # about class

# class Person:
#     def __init__(self, name, person_age, gender, passport_number, phone_number):
#         self.name = name
#         self.age = person_age
#         self.gender = gender
#         self.__passport_number = passport_number
#         self.phone_number = phone_number
        
    
#     def get_name(self):
#         return self.name
    
#     def set_age(self, new_age):
#         self.age = new_age

#     def get_age(self):
#         return self.age

#     def get_gender(self):
#         return self.gender

#     def get_passport_number(self):
#         return self.__passport_number

#     def get_phone_number(self):
#         return self.phone_number
    
#     def __str__(self):
#         return f"Name: {self.name}"
    
    
    
# class Student(Person):
#     def __init__(self, name, person_age, gender, passport_number, phone_number, student_id, course, card_number):
#         super().__init__(name, person_age, gender, passport_number, phone_number)
#         self.student_id = student_id
#         self.course = course
#         self.__card_number = card_number # private attribute, faqat class ichida ishlatiladi
        
        
#     def get_card_number(self):
#         return self.__card_number
#     def get_name(self):
#         return f"Student name: {self.name}"

#     def get_student_id(self):
#         return self.student_id
    
    
#     def set_course(self, new_course):
#         self.course = new_course

#     def get_course(self):
#         return self.course
    
#     def __str__(self):
#         return f"Name: {self.name}, Student ID: {self.student_id}"
    
    
# student1 = Student("Ali", 20, "male", "AB1234567", "+998901234567", "S12345", "Computer Science", "1234-5678-9012-3456")
# print(student1.get_name())
# print(student1.get_student_id())
# print(student1.get_course()) 

# print(student1.get_age()) 


# print(student1.get_passport_number())  

























# class Dog:
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age
        
#     def get_name(self):
#         return self.name
    
#     def get_breed(self):
#         return self.breed
    
#     def get_age(self):
#         return self.age
    
#     def __str__(self):
#         return f"Name: {self.name}, Breed: {self.breed}, Age: {self.age}"



# class Cat(Dog):
#     def __init__(self, name, breed, age, color):
#         super().__init__(name, breed, age)
#         self.color = color
        
#     def get_color(self):
#         return self.color       
    
#     def __str__(self):
#         return f"Name: {self.name}, Breed: {self.breed}, Age: {self.age}, Color: {self.color}"

# dog1 = Dog("Buddy", "Golden Retriever", 3)
# cat1 = Cat("Whiskers", "Persian", 2, "Gray")

# print(dog1)
# print(cat1)

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self._salary = salary  # protected

#     def display_salary(self):
#         print(f"Salary: {self._salary}")


# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self._department = department

#     def show_info(self):
#         print(f"Manager: {self.name}")
#         print(f"Department: {self._department}")
#         print(f"Salary: {self._salary}")  # protected atributdan foydalanish


# m = Manager("John", 5000, "HR")
# m.show_info()