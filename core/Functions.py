import math

def sin(x):
    """ f(x) = sin(x), f'(x) = cos(x) * x' """
    from .Dual import Dual
    if not isinstance(x, Dual):
        return math.sin(x)

    return Dual(sin(x.val), cos(x.val) * x.der)

def cos(x):
    """ f(x) = cos(x), f'(x) = -sin(x) * x' """
    from .Dual import Dual
    if not isinstance(x, Dual):
        return math.cos(x)

    return Dual(cos(x.val), -sin(x.val) * x.der)

def exp(x):
    """ f(x) = e^x, f'(x) = e^x * x' """
    from .Dual import Dual
    if not isinstance(x, Dual):
        return math.exp(x)

    val = exp(x.val)
    return Dual(val, val * x.der)

def log(x):
    """ f(x) = ln(x), f'(x) = (1/x) * x' """
    from .Dual import Dual
    if not isinstance(x, Dual):
        return math.log(x)

    return Dual(log(x.val), (1.0 / x.val) * x.der)

def sinh(x):
    """ f(x) = sinh(x), f'(x) = cosh(x) * x' """
    from .Dual import Dual
    if not isinstance(x, Dual):
        return math.sinh(x)

    return Dual(sinh(x.val), cosh(x.val) * x.der)

def cosh(x):
    """ f(x) = cosh(x), f'(x) = sinh(x) * x' """
    from .Dual import Dual
    if not isinstance(x, Dual):
        return math.cosh(x)

    return Dual(cosh(x.val), sinh(x.val) * x.der)

def ln(x):
    """ f(x) = ln x, f'(x) = (1/x) * x' """
    from .Dual import Dual
    if not isinstance(x, Dual):
        return math.log(x)

    return  Dual(ln(x.val),x.der/x.val)