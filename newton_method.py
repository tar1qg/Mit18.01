import math
from core import Dual


def newton_method(function,guess,steps=5):

    x_val = guess

    for i in range(steps):

        x_dual = Dual(x_val,1.0)
        res = function(x_dual)

        f_x = res.val
        f_prime_x = res.der

        # x_next = x - f(x) / f'(x)
        x_val = x_val-f_x/f_prime_x


    return x_val


def my_function(x):
    return x**2-2

root = newton_method(my_function,2.0)
true_root= math.sqrt(2)

print(abs(true_root-root))

