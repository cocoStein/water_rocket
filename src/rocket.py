class Rocket:
    def __init__(self, x, y, m):
        self.x = x
        self.y = y
        self.m = m

if __name__ == "__main__":
    r = Rocket(12, 10, 10)
    print(r)