class ToDoItem:
    def __init__(self, taskdate, taskname, id, foreign):
        self.__taskdate = taskdate
        self.__taskname = taskname
        self.__id = id
        self.__foreign = foreign

    def set_taskname(self, newtaskname):
        self.__taskname = newtaskname

    def set_taskdate(self, newtaskdate):
        self.__taskdate = newtaskdate

    def display(self):
        print(self.__taskdate + " " + self.__taskname)

    def getTitle(self):
        return self.__taskname

    def getUUID(self):
        return self.__id

    def getDate(self):
        return self.__taskdate

    def isForeign(self):
        return self.__foreign

    def export(self):
        return str(self.__taskdate) + ";" + str(self.__taskname) + ";" + str(self.__id) + "\n"
