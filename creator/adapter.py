#!/usr/bin/env python
# coding=utf-8


class Target:
    i = 1
    def interface(self):
        print('Call interface ', self.i)
        self.i = self.i + 1

class Adapter(Target):
    def interface(self):
        Target.interface(self)
        self.special_interface()

    def special_interface(self):
        print('Call special interface ', self.i)

#Client is the guy who use this speical_interface(), but it can only call
#interface()
class Client:
    def __call__(self, adapter):
        adapter.interface()

if __name__ == '__main__':
    c = Client()
    a = Adapter()
    c(a)
    c(a)
    c(a)
