
import sympy as sp
import numpy as np


class Solver():
    def __init__(self, func):
        self.setfunction(func)
    def setfunction(self,func: str):
        f_exp = sp.simplify(func)
        self.fe = f_exp
        self.func = sp.lambdify("x",f_exp,"numpy")
    def find_roots(self, a, b, eps = 1e-8):

        if self.fe == 0:
            return "Уравнение имеет бесконечное множество решений"
        roots = []
        n = 10000
        h = (b - a)/n
        for k in range(n):
            x1 = a + k * h
            x2 = x1 + h
            if self.func(x1) * self.func(x2) <= 0:
                root = self.bis(self.func, x1,x2, eps)
                if root is not None and not any(abs(root - r) < eps for r in roots):
                    roots.append(root)
        return roots
    def bis(self,func,a,b,eps):
        while (b - a) / 2 > eps:
            c = (a+b)/2
            if func(c) == 0:
                return c
            elif func(a) * func(c) < 0:
                b = c
            else:
                a = c
        return (a+b)/2
if __name__ == "__main__":
    func_str = "x-5"
    d = Solver(func_str)

    print(d.find_roots(-20,10))
