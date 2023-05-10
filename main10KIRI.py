class Mealy:
    def __init__(self) -> None:
        self.condition = "A"

    def reset(self):
        # try:
        if self.condition == "A":
            self.condition = "B"
            return int(0)
        elif self.condition == "B":
            self.condition = "C"
            return int(1)
        elif self.condition == "C":
            self.condition = "D"
            return int(2)
        elif self.condition == "D":
            self.condition = "E"
            return int(3)
        elif self.condition == "E":
            self.condition = "E"
            return int(6)
        elif self.condition == "F":
            self.condition = "F"
            return int(7)
        else:
            raise MealyError("reset")
        # except MealyError as e:
        #     return e

    def mute(self):
        # try:
        if self.condition == "D":
            self.condition = "A"
            return int(4)
        elif self.condition == "E":
            self.condition = "F"
            return int(5)
        elif self.condition == "F":
            self.condition = "B"
            return int(8)
        else:
            raise MealyError("mute")
        # except MealyError as e:
        #     return eeturn e


class MealyError(Exception):
    pass


def main():
    return Mealy()


def checkTest(obj: Mealy, method):
    try:
        if method == "reset":
            obj.reset()
        elif method == "mute":
            obj.mute()
    except MealyError as e:
        pass


def test():
    o = main()
    #A-B-C-D-A-B
    checkTest(o, "mute")  #ошибка в А
    checkTest(o, "reset") #B
    checkTest(o, "mute")  # ошибка в B
    checkTest(o, "reset")  # C
    checkTest(o, "mute")  # ошибка в C
    checkTest(o, "reset")  # D
    checkTest(o, "mute")  # A
    checkTest(o, "mute")  # ошибка в А
    checkTest(o, "reset")  # B
    #B-C-D-E-F-B-C-D-A-B
    checkTest(o, "mute")  # ошибка в B
    checkTest(o, "reset")  # C
    checkTest(o, "mute")  # ошибка в C
    checkTest(o, "reset")  # D
    checkTest(o, "reset") # E
    checkTest(o, "mute")  # F
    checkTest(o, "mute")  # B
    checkTest(o, "mute")  # ошибка в B
    checkTest(o, "reset")  # C
    checkTest(o, "mute")  # ошибка в C
    checkTest(o, "reset")  # D
    checkTest(o, "mute")  # A
    checkTest(o, "mute")  # ошибка в А
    checkTest(o, "reset")  # B
    #B-C-D-E-E-F-B-C-D-A-B
    checkTest(o, "mute")  # ошибка в B
    checkTest(o, "reset")  # C
    checkTest(o, "mute")  # ошибка в C
    checkTest(o, "reset")  # D
    checkTest(o, "reset")  # E
    checkTest(o, "reset")  # E
    checkTest(o, "mute")  # F
    checkTest(o, "mute")  # B
    checkTest(o, "mute")  # ошибка в B
    checkTest(o, "reset")  # C
    checkTest(o, "mute")  # ошибка в C
    checkTest(o, "reset")  # D
    checkTest(o, "mute")  # A
    checkTest(o, "mute")  # ошибка в А
    checkTest(o, "reset")  # B
    #B-C-D-E-F-F-B-C-D-A-B
    checkTest(o, "mute")  # ошибка в B
    checkTest(o, "reset")  # C
    checkTest(o, "mute")  # ошибка в C
    checkTest(o, "reset")  # D
    checkTest(o, "reset")  # E
    checkTest(o, "mute")  # F
    checkTest(o, "reset")  # F
    checkTest(o, "mute")  # B
    checkTest(o, "mute")  # ошибка в B
    checkTest(o, "reset")  # C
    checkTest(o, "mute")  # ошибка в C
    checkTest(o, "reset")  # D
    checkTest(o, "mute")  # A
    checkTest(o, "mute")  # ошибка в А
    checkTest(o, "reset")  # B
    #B-C-D-E-E-F-F-B-C-D-A-B
    checkTest(o, "mute")  # ошибка в B
    checkTest(o, "reset")  # C
    checkTest(o, "mute")  # ошибка в C
    checkTest(o, "reset")  # D
    checkTest(o, "reset")  # E
    checkTest(o, "reset")  # E
    checkTest(o, "mute")  # F
    checkTest(o, "reset")  # F
    checkTest(o, "mute")  # B
    checkTest(o, "mute")  # ошибка в B
    checkTest(o, "reset")  # C
    checkTest(o, "mute")  # ошибка в C
    checkTest(o, "reset")  # D
    checkTest(o, "mute")  # A
    checkTest(o, "mute")  # ошибка в А
    checkTest(o, "reset")  # B
    #B-C-D-E-F-B
    checkTest(o, "mute")  # ошибка в B
    checkTest(o, "reset")  # C
    checkTest(o, "mute")  # ошибка в C
    checkTest(o, "reset")  # D
    checkTest(o, "reset") # E
    checkTest(o, "mute")  # F
    checkTest(o, "mute")  # B
    checkTest(o, "mute")  # ошибка в B
    #B-C-D-E-E-F-B
    checkTest(o, "mute")  # ошибка в B
    checkTest(o, "reset")  # C
    checkTest(o, "mute")  # ошибка в C
    checkTest(o, "reset")  # D
    checkTest(o, "reset")  # E
    checkTest(o, "reset")  # E
    checkTest(o, "mute")  # F
    checkTest(o, "mute")  # B
    #B-C-D-E-F-F-B
    checkTest(o, "mute")  # ошибка в B
    checkTest(o, "reset")  # C
    checkTest(o, "mute")  # ошибка в C
    checkTest(o, "reset")  # D
    checkTest(o, "reset")  # E
    checkTest(o, "mute")  # F
    checkTest(o, "reset")  # F
    checkTest(o, "mute")  # B
    #B-C-D-E-E-F-F-B
    checkTest(o, "mute")  # ошибка в B
    checkTest(o, "reset")  # C
    checkTest(o, "mute")  # ошибка в C
    checkTest(o, "reset")  # D
    checkTest(o, "reset")  # E
    checkTest(o, "reset")  # E
    checkTest(o, "mute")  # F
    checkTest(o, "reset")  # F
    checkTest(o, "mute")  # B

test()
