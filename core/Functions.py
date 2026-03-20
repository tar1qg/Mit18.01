import math
from .Dual import Dual

def sin(x):
    """ f(x) = sin(x), f'(x) = cos(x) * x' """

    x = x if isinstance(x, Dual) else Dual(x)
    return Dual(math.sin(x.val), math.cos(x.val) * x.der)

def cos(x):
    """ f(x) = cos(x), f'(x) = -sin(x) * x' """

    x = x if isinstance(x, Dual) else Dual(x)
    return Dual(math.cos(x.val), -math.sin(x.val) * x.der)

def exp(x):
    """ f(x) = e^x, f'(x) = e^x * x' """

    x = x if isinstance(x, Dual) else Dual(x)
    val = math.exp(x.val)
    return Dual(val, val * x.der)

def log(x):
    """ f(x) = ln(x), f'(x) = (1/x) * x' """

    x = x if isinstance(x, Dual) else Dual(x)
    return Dual(math.log(x.val), (1.0 / x.val) * x.der)

def sinh(x):
    """ f(x) = sinh(x), f'(x) = cosh(x) * x' """

    x = x if isinstance(x, Dual) else Dual(x)
    return Dual(math.sinh(x.val), math.cosh(x.val) * x.der)

def cosh(x):
    """ f(x) = cosh(x), f'(x) = sinh(x) * x' """

    x = x if isinstance(x, Dual) else Dual(x)
    return Dual(math.cosh(x.val), math.sinh(x.val) * x.der)

def ln(x):
    """ f(x) = ln x, f'(x) = (1/x) * x' """

    x = x if isinstance(x, Dual) else Dual(x)
    return  Dual(math.log(x.val),x.der/x.val)