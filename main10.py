class MealyError(Exception):
   pass

class Mealy:
    def __init__(self) -> None:
        self.st = "A"

    def paste(self):
        if self.st == "A":
            self.st = "B"
            return 0
        elif self.st == "B":
            self.st = "C"
            return 2
        elif self.st == "D":
            self.st = "B"
            return 6
        elif self.st == "E":
            self.st = "H"
            return 8
        else:
            raise MealyError("paste")
    def fade(self):
        if self.st == "A":
            self.st = "E"
            return 1
        elif self.st == "E":
            self.st = "F"
            return 7
        elif self.st == "F":
            self.st = "G"
            return 10
        elif self.st == "G":
            self.st = "H"
            return 11
        else:
            raise MealyError("fade")
    def view(self):
        if self.st == "B":
            self.st = "H"
            return 3
        elif self.st == "C":
            self.st = "D"
            return 4
        elif self.st == "D":
            self.st = "E"
            return 5
        elif self.st == "E":
            self.st = "C"
            return 9
        else:
            raise MealyError("view")



def main():
    return Mealy()

def checkTest(obj: Mealy, method):
    try:
        if method == "paste":
            obj.paste()
        elif method == "fade":
            obj.fade()
        elif method == "view":
            obj.view()
    except MealyError as e:
        pass

def test():
    o = main()
    #A-B-H
    checkTest(o, "view")  # error in A
    checkTest(o, "paste") # B
    checkTest(o, "fade")  # error in B
    checkTest(o, "view")  # H
    checkTest(o, "view")  # error in H
    checkTest(o, "fade")  # error in H
    checkTest(o, "paste")  # error in H
    #A-B-C-D-B-H
    o = main()
    checkTest(o, "view")  # error in A
    checkTest(o, "paste")  # B
    checkTest(o, "fade")  # error in B
    checkTest(o, "paste") # C
    checkTest(o, "paste") # error in C
    checkTest(o, "fade")  # error in C
    checkTest(o, "view")  # D
    checkTest(o, "fade")  # error in D
    checkTest(o, "paste") # B
    checkTest(o, "fade")  # error in B
    checkTest(o, "view")  # H
    checkTest(o, "view")  # error in H
    checkTest(o, "fade")  # error in H
    checkTest(o, "paste")  # error in H

    #A-B-C-D-E-H
    o = main()
    checkTest(o, "view")  # error in A
    checkTest(o, "paste")  # B
    checkTest(o, "fade")  # error in B
    checkTest(o, "paste") # C
    checkTest(o, "paste") # error in C
    checkTest(o, "fade")  # error in C
    checkTest(o, "view")  # D
    checkTest(o, "fade")  # error in D
    checkTest(o, "view")  # E
    checkTest(o, "paste") # H
    checkTest(o, "view")  # error in H
    checkTest(o, "fade")  # error in H
    checkTest(o, "paste")  # error in H
    #A-B-C-D-E-C-D-B-H
    o = main()
    checkTest(o, "view")  # error in A
    checkTest(o, "paste")  # B
    checkTest(o, "fade")  # error in B
    checkTest(o, "paste")  # C
    checkTest(o, "paste")  # error in C
    checkTest(o, "fade")  # error in C
    checkTest(o, "view")  # D
    checkTest(o, "fade")  # error in D
    checkTest(o, "view")  # E
    checkTest(o, "view")  # C
    checkTest(o, "paste") # error in C
    checkTest(o, "fade")  # error in C
    checkTest(o, "view")  # D
    checkTest(o, "fade")  # error in D
    checkTest(o, "paste") # B
    checkTest(o, "fade")  # error in B
    checkTest(o, "view")  # H
    checkTest(o, "view")  # error in H
    checkTest(o, "fade")  # error in H
    checkTest(o, "paste")  # error in H
    #A-B-C-D-E-C-D-E-H
    o = main()
    checkTest(o, "view")  # error in A
    checkTest(o, "paste")  # B
    checkTest(o, "fade")  # error in B
    checkTest(o, "paste") # C
    checkTest(o, "paste") # error in C
    checkTest(o, "fade")  # error in C
    checkTest(o, "view")  # D
    checkTest(o, "fade")  # error in D
    checkTest(o, "view")  # E
    checkTest(o, "view")  # C
    checkTest(o, "paste") # error in C
    checkTest(o, "fade")  # error in C
    checkTest(o, "view")  # D
    checkTest(o, "fade")  # error in D
    checkTest(o, "view")  # E
    checkTest(o, "paste") # H
    checkTest(o, "view")  # error in H
    checkTest(o, "fade")  # error in H
    checkTest(o, "paste")  # error in H
    #A-B-C-D-E-F-G-H
    o = main()
    checkTest(o, "view")  # error in A
    checkTest(o, "paste")  # B
    checkTest(o, "fade")  # error in B
    checkTest(o, "paste") # C
    checkTest(o, "paste") # error in C
    checkTest(o, "fade")  # error in C
    checkTest(o, "view")  # D
    checkTest(o, "fade")  # error in D
    checkTest(o, "view")  # E
    checkTest(o, "fade")  # F
    checkTest(o, "paste") # error in F
    checkTest(o, "view")  # error in F
    checkTest(o, "fade")  # G
    checkTest(o, "paste") # error in G
    checkTest(o, "view")  # error in G
    checkTest(o, "fade")  # H
    checkTest(o, "view")  # error in H
    checkTest(o, "fade")  # error in H
    checkTest(o, "paste")  # error in H
    #A-E-H
    o = main()
    checkTest(o, "view")  # error in A
    checkTest(o, "fade")  # E
    checkTest(o, "paste") # H
    checkTest(o, "view")  # error in H
    checkTest(o, "fade")  # error in H
    checkTest(o, "paste") # error in H
    #A-E-C-D-B-H
    o = main()
    checkTest(o, "view")  # error in A
    checkTest(o, "fade")  # E
    checkTest(o, "view")  # C
    checkTest(o, "paste")  # error in C
    checkTest(o, "fade")  # error in C
    checkTest(o, "view")  # D
    checkTest(o, "fade")  # error in D
    checkTest(o, "paste")  # B
    checkTest(o, "fade")  # error in B
    checkTest(o, "view")  # H
    checkTest(o, "view")  # error in H
    checkTest(o, "fade")  # error in H
    checkTest(o, "paste")  # error in H
    #A-E-C-D-E-H
    o = main()
    checkTest(o, "view")  # error in A
    checkTest(o, "fade")  # E
    checkTest(o, "view")  # C
    checkTest(o, "paste")  # error in C
    checkTest(o, "fade")  # error in C
    checkTest(o, "view")  # D
    checkTest(o, "fade")  # error in D
    checkTest(o, "view")  # E
    checkTest(o, "paste")  # H
    checkTest(o, "view")  # error in H
    checkTest(o, "fade")  # error in H
    checkTest(o, "paste")  # error in H
    #A-E-F-G-H
    o = main()
    checkTest(o, "view")  # error in A
    checkTest(o, "fade")  # E
    checkTest(o, "fade")  # F
    checkTest(o, "paste")  # error in F
    checkTest(o, "view")  # error in F
    checkTest(o, "fade")  # G
    checkTest(o, "paste")  # error in G
    checkTest(o, "view")  # error in G
    checkTest(o, "fade")  # H
    checkTest(o, "view")  # error in H
    checkTest(o, "fade")  # error in H
    checkTest(o, "paste")  # error in H

test()