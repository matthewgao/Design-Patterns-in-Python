#!/usr/bin/env python
# coding=utf-8

# Assuming the Target is the class which come from other Lib or package,
# so you don't have the ability to change it, but the interface which Target
# given is insufficent for you, so you need a wrapper(adapter)
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
