# encoding: utf-8

class A:
    def __init__(self):
        self.value = 0
        self._hvalue = 1
        self.__pvalue = 2
    def spam(self):
        print('A.spam')

class B(A):
    def __init__(self):
        self.value =1
        super(B,self).__init__()

    def bar(self):
        print('B.bar')

b = B()
# b.spam()
b._hvalue

b.value