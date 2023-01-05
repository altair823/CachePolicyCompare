class Page:
    def __init__(self, num):
        self.num = num
        self.data = str(num)

    def __str__(self):
        return "Page" + str(self.num)

    def __repr__(self):
        return str(self)
