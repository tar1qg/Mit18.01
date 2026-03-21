import math

class Dual:
    def __init__(self,val,der = 0.0):
        self.val = val
        self.der = der

    def __add__(self, other):
        # (u + v)' = u' + v'

        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.val+other.val,self.der+other.der)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        # (u - v)' = u' - v'

        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.val - other.val, self.der - other.der)

    def __rsub__(self, other):
        other = other if isinstance(other, Dual) else Dual(other)
        return other - self


    def __mul__(self, other):
        # (uv)' = u'v + uv'

        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.val * other.val,
                    self.der * other.val + self.val * other.der)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        # (u/v)' = (u'v - uv') / v^2

        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.val / other.val,
                    (self.der * other.val - self.val * other.der) / (other.val**2))

    def __rtruediv__(self, other):
        other = other if isinstance(other, Dual) else Dual(other)
        return  other/self


    def __pow__(self, n):
        from core.Functions import ln

        # [u(x)^n]' = n * u(x)^(n-1) * u'(x)
        n = n if isinstance(n, Dual) else Dual(n)

        res_val = self.val ** n.val
        ln_self = ln(self.val)

        res_der = res_val * (n.der * ln_self + (n.val * self.der / self.val))
        return Dual(res_val, res_der)

    def __repr__(self):
        return f"Dual(val={self.val:.4f}, der={self.der:.4f})"