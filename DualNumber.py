import math

class Dual:
    def __init__(self, val, der=0.0):
        self.val = val  # 函数值 f(x)
        self.der = der  # 导数值 f'(x)

    def __add__(self, other):
        # 法则：(u + v)' = u' + v'
        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.val + other.val, self.der + other.der)

    def __sub__(self, other):
        # 法则：(u - v)' = u' - v'
        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.val - other.val, self.der - other.der)

    def __mul__(self, other):
        # 18.01 核心：乘积法则 (uv)' = u'v + uv'
        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.val * other.val,
                    self.der * other.val + self.val * other.der)

    def __truediv__(self, other):
        # 18.01 核心：商法则 (u/v)' = (u'v - uv') / v^2
        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.val / other.val,
                    (self.der * other.val - self.val * other.der) / (other.val**2))

    def __pow__(self, n):
        # 18.01 核心：幂法则 [u(x)^n]' = n * u(x)^(n-1) * u'(x) (结合了链式法则)
        return Dual(self.val**n, n * (self.val**(n-1)) * self.der)

    def __repr__(self):
        return f"Dual(val={self.val:.4f}, der={self.der:.4f})"

# 针对三角函数等非运算符的封装
def sin(d):
    # 链式法则：sin(u(x))' = cos(u(x)) * u'(x)
    return Dual(math.sin(d.val), math.cos(d.val) * d.der)

def cos(d):
    # 链式法则：cos(u(x))' = -sin(u(x)) * u'(x)
    return Dual(math.cos(d.val), -math.sin(d.val) * d.der)