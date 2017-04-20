#!/usr/bin/env python3
# encoding=utf-8
from human import human
class women(human):
    def __init__(self, name, alter):
        super().__init__(name, alter)
    def go_shopping(self):
        print("Go Shopping")
