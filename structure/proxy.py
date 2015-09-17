#!/usr/bin/env python
# coding=utf-8

#Proxy Example

class Proxy:

    def __init__(self, cls=None):
        self._real = None
        if cls is not None:
            self._real = cls()

    def access_real_subject(self):
        #print('access real subject')
        if self._real is not None:
            self._real.access_subject()

class RealSubject:
    def access_subject(self):
        print("access REAL subject")    


class Client:
    def __init__(self):
        self._proxy = Proxy(RealSubject)

    def get_subject(self):
        self._proxy.access_real_subject()

if __name__ == '__main__':

    c = Client()
    c.get_subject()
