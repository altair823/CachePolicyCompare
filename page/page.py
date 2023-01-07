class Page:
    def __init__(self, num: int):
        self.num = num
        self.data = "h" + chr(num)

    def __str__(self):
        return "Page" + str(self.num)

    def __repr__(self):
        return str(self)

