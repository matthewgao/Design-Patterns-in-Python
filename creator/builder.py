#!/usr/bin/env python
# coding=utf-8

#Builder-Director example

class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct(self, builder_type):
        if builder_type in self._builder.keys():
            return self._builder[builder_type].create().who_i_am()
        return None


class Builder:pass

class BuilderA(Builder):
    def create(self):
        return ProductA()

class BuilderB(Builder):
    def create(self):
        return ProductB()


class Product:pass

class ProductA:
    def who_i_am(self):
        print('product A')

class ProductB:
    def who_i_am(self):
        print('product B')

if __name__ == '__main__':
    builder_dict = {}
    builder_dict['A'] = BuilderA()
    builder_dict['B'] = BuilderB()

    d = Director(builder_dict)

    d.construct('A')
    d.construct('B')
