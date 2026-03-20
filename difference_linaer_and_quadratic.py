from core import Dual, ln
import math

#  f(x) = ln(x)   to calculate ln(e+Δx) at x=e

e = math.e
x_a = Dual(e,1)

f_a = ln(x_a).val
f_prime_a = ln(x_a).der
f_double_prime_a = -1/(e**2)


delta_x = 0.5
target_x = delta_x+e
true_value = math.log(target_x)


#  Linear Approximation f(x) = f(a) + f'(a) * Delta x
linear_prediction = f_a+f_prime_a*delta_x
abs_linear = abs(true_value-linear_prediction)

# Quadratic Approximation f(x) = f(a) + f'(a) * Delta x + (1/2) * f''(a) * Delta x^2
quadratic_prediction = f_a+f_prime_a*delta_x+f_double_prime_a*(delta_x**2)/2
abs_quadratic = abs(true_value-quadratic_prediction)

print(true_value,linear_prediction,abs_linear,quadratic_prediction,abs_quadratic)
