# class MyClass:
#     x = 5


# obj = MyClass()
# print(obj.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_name(self):
        print("name: ", self.name)


class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year = year

    def current_year(self):
        print(self.year)


p1 = Student("Bushra", 23, 2019)
p1.my_name()
p1.current_year()
