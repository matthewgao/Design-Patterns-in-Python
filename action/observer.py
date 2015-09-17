#!/usr/bin/env python
# coding=utf-8

# Observer Example

class Subject:
    def __init__(self):
        self._observer_list = []
        self._state = None
    def notify(self):
        for itr in  self._observer_list:
            itr.update()

    def get_state(self):
        return self._state

    def set_state(self, in_state):
        self._state = in_state
    
    def register(self, observer):
        if observer is not None:
            observer.set_subject(self)
            self._observer_list.append(observer)

class Observer:
    def __init__(self):
        self._state = 'init'
        self._subject = None

    def set_subject(self, subject):
        self._subject = subject

    def update(self):
        self._state = self._subject.get_state()
        print(self._state)

class ObserverA(Observer):pass
class ObserverB(Observer):pass

if __name__ == '__main__':
    s = Subject()
    a = ObserverA()
    b = ObserverB()
    s.register(a)
    s.register(b)

    s.notify()
    s.set_state('set 2')
    s.notify()
