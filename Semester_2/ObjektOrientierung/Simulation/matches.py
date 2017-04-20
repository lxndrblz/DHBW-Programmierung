import names
import random
from men import men
from women import women

class matches(men, women):
    def __init__(self, match_men, match_women):
        self.__men = match_men
        self.__women = match_women
        self.__kids = []

    #Ability to compare couples
    def __eq__(self, second):
        if self.__men == second.__men and self.__women == second.__women:
            return True
        else:
            return False


    def print(self):
        print("Couple: " + self.__men.get_name() +"+"+ self.__women.get_name())


    def print_kids(self):
        for kid in self.__kids:
            print ("\t" +  kid.get_name())


    def make_kids(self):
        if (len(self.__kids) < 3) and 18 < self.__men.get_age() < 50 and 18 < self.__women.get_age() < 50:
            for i in range(random.randint(1,4)):
                if random.randint(0,2) == 0:
                    self.__kids.append(men(names.get_first_name(gender='male'),0))

                else:
                    self.__kids.append(women(names.get_first_name(gender='female'),0))

    def get_kids(self):
            return self.__kids