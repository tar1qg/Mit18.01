import math

class Dual:
    def __init__(self,val,der = 0.0):
        self.val = val
        self.der = der

    def __add__(self, other):
        # (u + v)' = u' + v'

        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.val+other.val,self.der+other.der)

    def __sub__(self, other):
        # (u - v)' = u' - v'

        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.val - other.val, self.der - other.der)

    def __rsub__(self, other):
        return Dual(other - self.val, -self.der)


    def __mul__(self, other):
        # (uv)' = u'v + uv'

        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.val * other.val,
                    self.der * other.val + self.val * other.der)

    def __truediv__(self, other):
        # (u/v)' = (u'v - uv') / v^2

        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.val / other.val,
                    (self.der * other.val - self.val * other.der) / (other.val**2))

    def __rtruediv__(self, other):
        return  Dual(other.val/self.val,
                     - (other * self.der) / (self.val ** 2))

    def __pow__(self, n):

        # [u(x)^n]' = n * u(x)^(n-1) * u'(x)
        n = n if isinstance(n, Dual) else Dual(n)

        return Dual(self.val**n.der, self.val ** n.val *
                    (n.der * math.log(self.val) + (n.val * self.der / self.val)))

    def __repr__(self):
        return f"Dual(val={self.val:.4f}, der={self.der:.4f})"