class Shape:
    def __init__(self, color, size, position):
        self.color = color
        self.size = size
        self.position = position

    def draw(self, turtle):
        pass

class Circle(Shape):
    def __init__(self, color, size, position):
        super().__init__(color, size, position)
    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.color(self.color)
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

class Square(Shape):
    def __init__(self, color, size, position):
        super().__init__(color, size, position)
    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.color(self.color)
        for _ in range(4):
            turtle.forward(self.size)
            turtle.right(90)
