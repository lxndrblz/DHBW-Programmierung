#!/usr/bin/env python3
# encoding=utf-8
from human import human
class women(human):

    def __init__(self, name, alter , babys):
        super().__init__(name, alter)
        self.__babys = babys

    def increase_baby_counter(self):
        self.__babys += 1

    def get_kids(self):
        return self.__babys

    def go_shopping(self):
        print("Go Shopping")