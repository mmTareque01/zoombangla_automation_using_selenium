from configuration.configuration import SeleniumConfiguration


class AVC:
    def __init__(self):
        self.a = 0

    def get(self):
        self.a = self.a + 1
        return self.a


if __name__ == '__main__':
    # configObj = SeleniumConfiguration()

    print("hellow")
