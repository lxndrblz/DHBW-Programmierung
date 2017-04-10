class ToDoItem:
    def __init__(self,taskdate,taskname):
        self.__taskdate = taskdate
        self.__taskname = taskname

    def set_taskname(self, newtaskname):
        self.__taskname = newtaskname

    def set_taskdate(self, newtaskdate):
        self.__taskdate = newtaskdate

    def display(self):
        print(self.__taskdate + " "+self.__taskname)

    def export(self):
        return str(self.__taskdate) + ";" + str(self.__taskname) + "\n"