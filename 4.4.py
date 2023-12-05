class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def info():
        print("Точки имеют координаты x y")

    @classmethod
    def fourfour(cls):
        return cls(4,4)

    def show_coor(self):
        print(f"Координата х: {self.x} \nКоордината у: {self.y} ")


a = Point(2, 3)
a.info()
b = a.fourfour()

a.show_coor()
print()
b.show_coor()