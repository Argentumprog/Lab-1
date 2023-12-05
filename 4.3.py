class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Отрисовка с использованием ручки {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Отрисовка с использованием карандаша {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Отрисовка с использованием маркера {self.title}")


some_station = Stationery("-")
pen_instance = Pen("синяя")
pencil_instance = Pencil("черный")
handle_instance = Handle("зеленый")

some_station.draw()
pen_instance.draw()
pencil_instance.draw()
handle_instance.draw()
