#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
import random
from random import randint
def hashthis(s):
    h = 0
    base = 1
    for char in s:
        h += ord(char)*base
        base *= 26
    return h

def bruteforcel(h):
    buchstaben = string.ascii_lowercase
    
    while True:
        password = ''
        #Zufaellige Länge
        for i in range(10):
            #Zufaellige Buchstaben
            for b in buchstaben:
                
                password = password + str(b)
                if(h == hashthis(password)):
                    break
    return password

def bruteforce(h):
    buchstaben = string.ascii_lowercase
    
    while True:
        password = ''
        #Zufaellige Länge
        for i in range(randint(0,10)):
            #Zufaellige Buchstaben
            
            c = random.choice(buchstaben)
            password = password + c  
        if(h == hashthis(password)):
            break
    return password
hashwert =hashthis(str(raw_input("Ihr Passwort: ")))
print "Hash Wert: " + str(hashwert)
print "Passwort war: " + bruteforcel(hashwert)


