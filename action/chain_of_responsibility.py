#!/usr/bin/env python
# coding=utf-8

class Processor:
    def __init__(self):
        self._next = None

    def register_next_processor(self, processor):
        if isinstance(processor, Processor):
            self._next = processor
    def do(self):
        self.process()

class ProcessorA(Processor):
    def process(self):
        print('ProcessorA')
        if self._next is not None:
            self._next.process()

class ProcessorB(Processor):
    def process(self):
        print('ProcessorB')
        if self._next is not None:
            self._next.process()

class ProcessorC(Processor):
    def process(self):
        print('ProcessorC')
        if self._next is not None:
            self._next.process()


if __name__ == '__main__':
    a = ProcessorA()
    b = ProcessorB()
    c = ProcessorC()

    a.register_next_processor(b)
    b.register_next_processor(c)
    a.do()
