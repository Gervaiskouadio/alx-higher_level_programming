class Rectangle:
    def __init__(self, width, height, x=0, y=0, id=None):
        self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def area(self):
        return self.width * self.height

    def display(self):
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}
