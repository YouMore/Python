class MyClass:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.__hidden__ = 3

    def do_something(self):
        pass


obj = MyClass()

for name in vars(obj):
    if not name.startswith("__"):
        print(name)
