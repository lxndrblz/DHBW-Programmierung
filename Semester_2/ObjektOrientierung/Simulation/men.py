#!/usr/bin/env python3
# encoding=utf-8
from human import human

class men(human):
    def __init__(self, name, alter):
        super().__init__(name, alter)

    def play_soccer(self):
        print("Soccer")