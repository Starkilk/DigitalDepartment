#-Создайте класс Rectangle и Square с методом вычисления периметра, создайте экземпляры классов – объекты, вызовите созданный метод.
#-В классе Square определите метод для изменения размера на соответствующее значение
#-Создайте класс Shape, в котором определите метод, выводящий текст «Я фигура». Измените классы Rectangle и Square для наследования от Shape. Создайте объекты классов Rectangle и Square и вызовите созданный метод.
#-Добавьте переменную square_list в класс Square таким образом, чтобы при создании нового объекта данного класса, он добавлялся в список
#-Измените класс Square таким образом, чтобы при выводе объекта класса Square выводилась информация о всех сторонах квадрата, например, 15x15, 15x15
#-Напишите функцию, которая имеет два параметра, и возвращает True, если они являются одним и тем же объектом и False в противном случае.
#-Создайте классы Course и Student, используя композицию, смоделируйте запись студентов на курсы.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Метод для вычисления периметра
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


# Создаем класс Square, наследуемый от Rectangle
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    # Метод для изменения размера на соответствующее значение
    def change_size(self, new_side):
        self.width = new_side
        self.height = new_side


# Создаем класс Shape
class Shape:
    def print_shape(self):
        print("Я фигура")


# Изменяем классы Rectangle и Square для наследования от Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Square(Shape):
    def __init__(self, side):
        self.width = side
        self.height = side

    def calculate_perimeter(self):
        return 4 * self.width


# Создаем объекты классов Rectangle и Square и вызываем методы
rectangle = Rectangle(4, 5)
print(rectangle.calculate_perimeter())
square = Square(5)
print(square.calculate_perimeter())


# Изменяем класс Square для добавления переменной square_list
class Square(Shape):
    square_list = []

    def __init__(self, side):
        self.width = side
        self.height = side
        self.square_list.append(self)


# Создаем два объекта класса Square
square1 = Square(10)
square2 = Square(15)

# Выводим информацию о всех сторонах квадрата
for square in Square.square_list:
    print(f"{square.width}x{square.height}")


# Напишем функцию для сравнения объектов
def compare_objects(obj1, obj2):
    return obj1 is obj2


# Создаем объекты для сравнения
obj1 = object()
obj2 = obj1
obj3 = object()

print(compare_objects(obj1, obj2))
print(compare_objects(obj1, obj3))


# Создаем классы Course и Student с использованием композиции
class Course:
    def __init__(self, name, students):
        self.name = name
        self.students = students


class Student:
    def __init__(self, name):
        self.name = name


# Создаем объекты курсов и студентов и моделируем запись студентов на курсы
student1 = Student("John")
student2 = Student("Jane")
student3 = Student("Mike")

course1 = Course("Math", [student1, student2])
course2 = Course("Science", [student2, student3])