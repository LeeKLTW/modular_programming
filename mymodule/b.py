# encoding: utf-8
from .a import A


class B(A):
    def bar(self):
        print('B.bar')
