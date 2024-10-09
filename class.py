class Cupboard:
    def __init__(self, color, shelf_count, height) -> None:
        self.color = color
        self.shelf_count = shelf_count
        self.height = height


szekreny01 = Cupboard("kek", "3", "150")

print(szekreny01.color)
