class Bruch(object):

    def __init__(self,zaehler,nenner):
        self.__zaehler=zaehler
        self.__nenner=nenner
    def __add__(self, b2):
        if (self.__nenner == b2.__nenner):
            result = Bruch(1, 1)
            result.__nenner = self.__nenner
            result.__zaehler = self.__zaehler + b2.__zaehler
            return result
        else:
            result = Bruch(1, 1)
            result.__nenner = self.__nenner * b2.__nenner
            result.__zaehler = (self.__zaehler * b2.__nenner + b2.__zaehler * self.__nenner)

            result.__nenner = result.__nenner / self.euklid(result.__nenner, result.__zaehler)
            result.__zaehler = result.__zaehler / self.euklid(result.__nenner, result.__zaehler)
            return result

    def euklid(self,a, b):
        while b != 0:
            a, b = b, a % b
        return a
    def show(self):
        print(str(self.__zaehler) + "/" + str(self.__nenner))
    def quadrat(self):
        result = Bruch(1, 1)
        result.__zaehler = self.__zaehler * self.__zaehler
        result.__nenner = self.__nenner * self.__nenner
        return result
    def __mul__(self,b2):
        result = Bruch(1,1)
        result.__zaehler = self.__zaehler * b2.__zaehler
        result.__nenner = self.__nenner * b2.__nenner
        return result
    def kehrbruch(self):
        result = Bruch(self.__nenner, self.__zaehler)
        return result
    def string(self):
        return str(self.__zaehler) + "/" + str(self.__nenner)

if __name__ == '__main__':
    b1 = Bruch(2,4)
    b2 = Bruch(1,2)
    print("Multiply:")

    b4 = Bruch(1,12)
    b5 = Bruch(2,6)
    t = b4+b5
    b4.show()
    b5.show()
    t.show()

