class ToDoItem:
    def __init__(self,taskddate,taskname):
        self.__taskdate = taskddate
        self.__taskname = taskname

    def setTaskname(self,newtaskname):
        self.__taskname = newtaskname
    def setTaskdate(self,newtaskdate):
        self.__taskdate = newtaskdate
    def display(self):
        return str(self.__taskdate + " "+self.__taskname)
    def export(self):
        return str(self.__taskname) + ";" + str(self.__taskdate) + "\n"