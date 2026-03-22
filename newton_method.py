import math
from core import Dual,cos,sin


def newton_method(function,guess,tolerance=1e-5,max_steps=50):

    x_val = guess

    for i in range(max_steps):

        x_dual = Dual(Dual(x_val, 1.0), Dual(1.0, 0.0))
        res = function(x_dual)

        f_x = res.val.val
        f_prime_x = res.val.der
        f_double_prime_x = res.der.der

        # f'(x) can't be too small
        if abs(f_prime_x) < tolerance:
            return None

        # f''(x) can't be too big
        if abs(f_double_prime_x) > 100:
            print()

        # check for convergence
        if abs(f_x)<tolerance:
            return x_val


        # newton method x_next = x - f(x) / f'(x)
        x_val = x_val-f_x/f_prime_x


    return x_val

# Basic Polynomials
def test_basic_polynomials():
    print(">>> Test 1: Basic Polynomials")
    # f(x) = x^2 - 2, Root ≈ 1.41421356
    f1 = lambda x: x**2 - 2
    res1 = newton_method(f1, guess=2.0)
    print(abs(math.sqrt(2)-res1))

    # f(x) = x^3 - 27, Root = 3.0
    f2 = lambda x: x**3 - 27
    res2 = newton_method(f2, guess=5.0)
    print(abs(3 - res2))

# Far Guess
def test_far_guess():
    print(">>> Test 2: Far Guess (Testing Robustness)")
    # from 1,000,000 to look for sqrt(2)
    f = lambda x: x**2 - 2
    res = newton_method(f, guess=1000000.0, max_steps=100)
    print(abs(math.sqrt(2) - res))

def test_failures():
    print(">>> Test 4: Failure Cases (Zero Derivative)")
    # f(x) = x^2 + 1
    # guess =  0，f'(0) = 0
    f = lambda x: x**2 + 1
    res = newton_method(f, guess=0.0)
    # return None : error
    print(res)

if __name__ == "__main__":
    test_basic_polynomials()
    test_far_guess()
    test_failures()
