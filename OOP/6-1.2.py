class Rectangle:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def area_of_the_figure(self):
        width = self.x2[0] - self.x1[0]
        height = self.x1[1] - self.x2[1]

        return width * height

    def info(self):
        print(self.area_of_the_figure(), self.x1, self.x2)


a = [2, 9]
b = [11, 5]

a1 = [2, 7]
b1 = [7, 5]

x = Rectangle(a, b)
y = Rectangle(a1, b1)

x.info()
y.info()

