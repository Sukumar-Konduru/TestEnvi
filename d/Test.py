from a.a1 import A1
from b.b1 import B1
from c.c1 import C1


class d1:
    def __init__(self,A,B,C):
        print("d1 object is called")
        self.a=A
        self.b=B
        self.c=C
    def test(self):
        self.a=10
        b=20
        c=30
        a1ref=A1()
        a1ref.a1Method()
        b1ref = B1()
        b1ref.b1Method()
        c1ref = C1()
        c1ref.c1Method()
        print(self.a,b,c)
if __name__ == '__main__':
    d=d1(1,2,3)
    d.test()
