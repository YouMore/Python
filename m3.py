class A:
    pass

class B(A):
    pass

class C(B): #не должно быть множественного наследования, В и так наследуется от А
    pass