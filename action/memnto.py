#!/usr/bin/env python
# coding=utf-8

#Memento Example, Memento is used to store the object states

class Originator:
    def __init__(self, init_state):
        self._memento = Memento(init_state)
        self._state = None

    def set_memento(self):
        self._state = self._memento.get_state()

    def check_state(self):
        print(self._state)

class Memento:
    def __init__(self, init_state):
        self._state = init_state

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

if __name__ == '__main__':
    c = Originator('state first')
    c.set_memento()
    c.check_state()
