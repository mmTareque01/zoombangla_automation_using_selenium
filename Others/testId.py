class TestId:
    def __init__(self):
        self.id = 0

    def get(self):
        self.id = self.id + 1
        return self.id
