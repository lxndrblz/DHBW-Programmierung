# encoding=utf-8
from collections import OrderedDict

path_to_file = "./data/train.csv"


def read_data_from_file(file_path):
    data = []

    f = open(file_path)
    for line in f:

        data.append(make_row(line.rstrip().split(";")))

    return data


def make_row(list):
    data = OrderedDict()

    keys = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin',
            'Embarked']

    # Werte zuordnen
    for l in range(len(keys)):
        data[keys[l]] = list[l]
    return data


def filter_value(dataset, param, value):
    alle=[]
    for d in dataset:
        if d[param] > 0:
            if d[param] == value:
                alle.append(d)
    return alle


def filter_invalid(dataset, param):
    alle = []
    for d in dataset:
        if len(d[param]) > 0:
            alle.append(d)
    return alle


def sum_value(dataset, param):
    sum = 0.0
    for d in dataset:
        sum += float(d[param])
    return sum


def count(dataset):
    return len(dataset)


def age_survived(l):
    alle = []
    for p in l:
        if len(p["Age"]) > 0:
            alle.append(p)

    sum_survived = 0.0
    count_survived = 0
    sum_dead = 0.0
    count_dead = 0

    for pers in alle:
        if pers['Survived'] == '1':
            count_survived += 1
            sum_survived += float(pers['Age'])

        else:
            count_dead += 1
            sum_dead += float(pers['Age'])
    print("Mean Age survived %d" % (sum_survived / count_survived))
    print("Mead Age dead %d" % (sum_dead / count_dead))

#age_survived(read_data_from_file(path_to_file))


alle=read_data_from_file(path_to_file)


survived = filter_value(alle,"Survived","1")
dead = filter_value(alle,"Survived","0")

#Invalide Daten ausfiltern
survived = filter_invalid(survived, "Age")
dead = filter_invalid(dead,"Age")

sum_age_survived = sum_value(survived,"Age")
sum_age_dead = sum_value(dead,"Age")

count_survived = count(survived)
count_dead = count(dead)

print("Mean Age survived %d" %(sum_age_survived/count_survived))
print("Mead Age dead %d" %(sum_age_dead/count_dead))