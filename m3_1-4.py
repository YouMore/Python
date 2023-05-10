class Num:
    def __init__(self, data) -> None:
        self.data = data


class Add:
    def __init__(self, l, r) -> None:
        self.l = l
        self.r = r

class Mul:
    def __init__(self, l, r) -> None:
        self.l = l
        self.r = r


class PrintVisitor:
    def visit(self, node):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name)
        return method(node)

    def visit_Num(self, node):
        return str(node.data)

    def visit_Add(self, node):
        return f"({self.visit(node.l)} + {self.visit(node.r)})"

    def visit_Mul(self, node):
        return f"({self.visit(node.l)} * {self.visit(node.r)})"


ast = Add(Num(100), Mul(Num(12), Num(12)))
pv = PrintVisitor()
print("3.2")
print(pv.visit(ast))


# 3.3
class CalcVisitor:
    def visit(self, node):
        method_name = f"v_{type(node).__name__}"
        method = getattr(self, method_name)
        return method(node)

    def v_Num(self, node):
        return node.data

    def v_Add(self, node):
        return self.visit(node.l) + self.visit(node.r)

    def v_Mul(self, node):
        return self.visit(node.l) * self.visit(node.r)


cv = CalcVisitor()
print("\n3.3")
print(cv.visit(ast))


# 3.4
class StackVisitor:
    def visit(self, node):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name)
        return method(node)

    def visit_Num(self, node):
        return f"PUSH {str(node.data)}\n"

    def visit_Add(self, node):
        return f"{self.visit(node.l)}{self.visit(node.r)}ADD\n"

    def visit_Mul(self, node):
        return f"{self.visit(node.l)}{self.visit(node.r)}MUL\n"


print("\n3.4")
sv = StackVisitor()
print(sv.visit(ast))