#!/usr/bin/env python
# coding=utf-8

# Prototype Example

import copy


class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class PrototypeA(Prototype):
    def who_i_am(self):
        print("Prototype A")


class PrototypeB(Prototype):
    def who_i_am(self):
        print("Prototype B")


class Client:
    def __init__(self, prototype_dict):
        self._prototype_dict = prototype_dict

    def register_new_prototype(self, type_name, type_object):
        self._prototype_dict[type_name] = type_object

    def get_prototype_of(self, prototype):
        if prototype in self._prototype_dict.keys():
            return self._prototype_dict[prototype].clone()
        return None


if __name__ == '__main__':

    pa = PrototypeA()
    pb = PrototypeB()
    print(pa)
    print(pb)
    p_dict = {}
    p_dict['A'] = pa
    #p_dict['B'] = pb

    c = Client(p_dict)
    
    c.register_new_prototype('B',pb)

    npa = c.get_prototype_of('A')
    npb = c.get_prototype_of('B')
    npa.who_i_am()
    npb.who_i_am()
    print(npa)
    print(npb)

