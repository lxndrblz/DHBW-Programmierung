import random
class human(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def do(self):
        print(self.__name + " does something")
    def die(self):
        if self.__age > (100 - random.randint(0, 60)):
            #print(self.__name + " died at the age of " + str(self.__age))
            return True
        else:
            return False
    def show(self):
        print("Alter "+str(self.__age) + " Name "+ str(self.__name))
    def get_age(self):
        return self.__age
    def make_older(self):
        self.__age += 1
    def get_name(self):
        return str(self.__name)