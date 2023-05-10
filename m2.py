class MyClass:
    def method1(self):
        print("Hello world")

obj = MyClass()

method = getattr(obj, "method1")
method()

