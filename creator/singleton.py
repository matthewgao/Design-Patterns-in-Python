#!/usr/bin/env python
# coding=utf-8

def singleton(cls, *args, **kw):
    _instance = {}

    def wrapper():
        if cls not in _instance:
            _instance[cls] = cls(*args, **kw)
        return _instance[cls]

    return wrapper

@singleton
class AObject:
    def __init__(self):
        print("Created")


if __name__ == '__main__':
    print(AObject())
    print(AObject())
    print(AObject())
