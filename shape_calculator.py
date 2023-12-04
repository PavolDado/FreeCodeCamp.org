class shape_calculator:

    class Rectangle:

        def __init__(self, width, height):
            self.width = width
            self.height = height

        def __repr__(self):
            return f"Rectangle(width={self.width}, height={self.height})"

        def set_width(self, width):
            self.width = width
            return self.width

        def set_height(self, height):
            self.height = height
            return self.height

        def get_area(self):
            return (self.width * self.height)

        def get_perimeter(self):
            return (2 * self.width + 2 * self.height)

        def get_diagonal(self):
            return ((self.width**2 + self.height**2)**.5)

        def get_picture(self):
            if self.width < 51 or self.height < 51:
                line = "*" * self.width
                for _i in range(self.height):
                    print(line)
            else:
                print("Too big for picture.")

        def get_amount_inside(self, shape):
            return int(
                (self.width / shape.width) * (self.height / shape.height))

    class Square(Rectangle):

        def __init__(self, side):
            self.width = self.height = self.side = side

        def __repr__(self):
            return f"Square(side={self.side})"

        def set_side(self, side):
            self.width = self.height = self.side = side
            return self.side
