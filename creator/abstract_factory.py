#!/usr/bin/env python
# coding=utf-8

#这是一种C++的实现思路，但是实际上在Python中，不是一个强类型的语言
#所以抽象工厂完全没有必要

class AbstractFactory:
    def create_product(self):
        pass

#变换一种思路，也可以这样
#class AbstractFactory:
#    def create_factory(self, factory_type):
#        if factory_type = 'A':
#            return FactoryA()
#        return None


class FactoryA(AbstractFactory):
    def create_product(self):
        return ProductA()

class Product:pass

class ProductA(Product):
    def who_i_am(self):
        print("product A")


if __name__ == '__main__':
    fc = FactoryA()

    pd = fc.create_product()
    pd.who_i_am()
