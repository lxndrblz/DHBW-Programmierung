#!/usr/bin/env python3
# encoding=utf-8
import ToDoItem

'''

Implementierung einer einfachen ToDo Liste

'''
pathtonotes = "./data/todo.tasks"


# Datei auslesen
def read_data_from_file():
    f = open(pathtonotes)
    # Liste mit ToDoItems
    tasks = []
    for lines in f:
        t = lines.rstrip().split(";")
        tasks.append(ToDoItem.ToDoItem(t[0], t[1], t[2]))
    return tasks


# Datei schreiben
def write_data(path, tasks, append):
    # Zeilenweise schreiben
    if append == True:
        f = open(path, 'a')
    else:
        # ersetzen
        f = open(path, 'w')
    task = ""
    for t in tasks:
        task += t.export()
    f.write(task)
    f.close()


# Datenreihe löschen
def delete_task(id):
    list_index = 0
    for item in read_data_from_file():
        if(item.getUUID()==id):
            break
        list_index += 1
    data = read_data_from_file()
    data.remove(data[list_index])
    write_data(pathtonotes, data, False)

# Werte eines Eintrags anpassen
def edit_task(id, newtitle, newdate):
    data = read_data_from_file()
    for item in data:
        if(item.getUUID()==id):
            item.set_taskname(str(newtitle))
            item.set_taskdate(str(newdate))
    write_data(pathtonotes, data, False)


# Menüpunkt hinzufügen
def new_task(title, date, id):
    temp = ToDoItem.ToDoItem(title, date, id)
    write_data(pathtonotes, [temp], True)
