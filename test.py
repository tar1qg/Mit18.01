import math

from core import Dual, sin, exp



def test_add():
    x = Dual(1.0, 1.0)
    y = x ** 2 + x

    # y =1+1=2    y'=2*x+1 = 2*1+1=3
    assert  math.isclose(y.val,2.0)
    assert  math.isclose(y.der,3.0)

def test_sub():
    x = Dual(1.0, 1.0)
    y = x**2-x

    # y =1-1=0   y'=2*x-1 = 2-1=1
    assert math.isclose(y.val, 0.0)
    assert math.isclose(y.der, 1.0)

def test_mul():
    x = Dual(1.0, 1.0)
    y = (x**2+1)*(x**3)

    # y =2*1=2   y'=2*x*(x**3)+3*(x**2)*(x**2+1) = 2*1+3*2=8
    assert math.isclose(y.val, 2.0)
    assert math.isclose(y.der, 8.0)

def test_truediv():
    x = Dual(1.0, 1.0)
    y = (x**2+1)/x

    # y =2/1=2   y'=(x**2-1)/((x**2) = (2-2)/1=0
    assert math.isclose(y.val, 2.0)
    assert math.isclose(y.der, 0.0)



def test_chain_rule():
    x = Dual(1.0, 1.0)
    y = (x**2+2*x+1)**3

    # y =((1+2+1)**3=64   y'= 3*((x**2+2*x+1)**2)*(2*x+2)=3*(4**2)*4=192
    assert math.isclose(y.val, 64.0)
    assert math.isclose(y.der, 192.0)


def test_exp():
    x = Dual(1.0, 1.0)
    y = exp(x) * x

    # y = e^x * x -> y(1) = e^1 * 1 = e
    # y' = e^x * x + e^x -> y'(1) = e + e = 2e
    assert math.isclose(y.val, math.e)
    assert math.isclose(y.der, 2 * math.e)


def test_sin():

    x = Dual(math.pi / 4, 1.0)
    y = sin(x) ** 2

    # y = sin^2(x) -> y(pi/4) = (sqrt(2)/2)^2 = 0.5
    # y' = 2 * sin(x) * cos(x) = sin(2x) -> y'(pi/4) = sin(pi/2) = 1.0
    assert math.isclose(y.val, 0.5)
    assert math.isclose(y.der, 1.0)


if __name__ == "__main__":
    test_add()
    test_sub()
    test_mul()
    test_truediv()
    test_chain_rule()
    test_exp()
    test_sin()
