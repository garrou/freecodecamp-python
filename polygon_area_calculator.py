class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width) -> None:
        self.width = width

    def set_height(self, height) -> None:
        self.height = height

    def get_area(self) -> float|int:
        return self.width * self.height

    def get_perimeter(self) -> float|int:
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> float|int:
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_amount_inside(self, shape) -> int:
        return int(self.get_area() / shape.get_area())
    
    def get_picture(self) -> str:
        picture = ""

        if self.width > 50 or self.height > 50:
            picture = "Too big for picture."
        else:
            for _ in range(self.height):
                for _ in range(self.width):
                    picture += "*"
                picture += "\n"
        
        return picture

class Square(Rectangle):
    def __init__(self, side) -> None:
        Rectangle.__init__(self, side, side)

    def __str__(self) -> str:
        return f"Square(side={self.width})"

    def set_side(self, side) -> None:
        self.width = side
        self.height = side

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

rect.set_width(3)
rect.set_height(10)
print(rect.get_diagonal())