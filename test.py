import math

from core import Dual, sin, exp

x = Dual(1.0, 1.0)

def test_add():

    y = x ** 2 + x

    # y =1+1=2    y'=2*x+1 = 2*1+1=3
    assert  math.isclose(y.val,2.0)
    assert  math.isclose(y.der,3.0)

def test_sub():

    y = x**2-x

    # y =1-1=0   y'=2*x-1 = 2-1=1
    assert math.isclose(y.val, 0.0)
    assert math.isclose(y.der, 1.0)

def test_mul():

    y = (x**2+1)*(x**3)

    # y =2*1=2   y'=2*x*(x**3)+3*(x**2)*(x**2+1) = 2*1+3*2=8
    assert math.isclose(y.val, 2.0)
    assert math.isclose(y.der, 8.0)

def test_truediv():

    y = (x**2+1)/x

    # y =2/1=2   y'=(x**2-1)/((x**2) = (2-2)/1=0
    assert math.isclose(y.val, 2.0)
    assert math.isclose(y.der, 0.0)



def test_chain_rule():

    y = (x**2+2*x+1)**3

    # y =((1+2+1)**3=64   y'= 3*((x**2+2*x+1)**2)*(2*x+2)=3*(4**2)*4=192
    assert math.isclose(y.val, 64.0)
    assert math.isclose(y.der, 192.0)


if __name__ == "__main__":
    test_add()
    test_sub()
    test_mul()
    test_truediv()
    test_chain_rule()
