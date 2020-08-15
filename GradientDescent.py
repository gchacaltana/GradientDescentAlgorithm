# -*- coding: utf-8 -*-
# Implementación del algoritmo de gradiente descendente.

import sympy as sy
import sys
import os
from matplotlib import pyplot as plt


class GradientDescent(object):

    def __init__(self, x, y, fx, options):
        self.x, self.y, self.fx = x, y, fx
        self.coord_x, self.coord_y = [], []
        self.options = options
        self.iteration_counter, self.max_iterations = 0, 4

    def set_options(self):
        self.rounding = self.options['rounding'] if self.options['rounding'] else 2
        self.x_ini = self.options['x_ini'] if self.options['x_ini'] else 0
        self.y_ini = self.options['y_ini'] if self.options['y_ini'] else 0

    def run(self):
        self.set_options()
        os.system('clear')
        print("\n------------------------------------------")
        print("Aplicando el Metodo del Gradiente Descendente")
        print("----------------------------------------------")
        print("\nDada la funcion f(x)")
        print("\nf(x) = {}".format(sy.simplify(self.fx)))
        self.x_i, self.y_i = self.x_ini, self.y_ini
        self.arrayPoints, self.arrayFx, self.arrayGrad, self.arrayAlpha = [], [], [], []
        while(self.iteration_counter < self.max_iterations):
            self.iteration_counter = self.iteration_counter+1
            self.calculate()
        self.show_table_result()

    def calculate(self):
        self.arrayPoints.append("({},{})".format(self.x_i, self.y_i))
        self.arrayFx.append(self.process_function())
        self.process_gradient()
        self.arrayGrad.append("({},{})".format(self.x_grad, self.y_grad))
        self.arrayAlpha.append(str(self.calculate_alpha())[0:6])
        self.x_i = self.x_i-self.x_grad*self.alpha
        self.y_i = self.y_i-self.y_grad*self.alpha

    def process_function(self):
        return round(float(self.fx.subs({self.x: self.x_i, self.y: self.y_i})), self.rounding)

    def process_gradient(self):
        """
        Obtener los valores de x,y de la Gradiente
        """
        dx, dy = self.df(self.x), self.df(self.y)
        self.x_grad = round(
            float(dx.subs({self.x: self.x_i, self.y: self.y_i})), self.rounding)
        self.y_grad = round(
            float(dy.subs({self.x: self.x_i, self.y: self.y_i})), self.rounding)

    def df(self, var):
        """
        Derivada de la funcion f(x) dado una variable
        """
        return sy.diff(self.fx, var)

    def calculate_fx_grad(self):
        x_g = self.x_i - self.x_grad
        y_g = self.y_i - self.y_grad
        return round(float(self.fx.subs({self.x: x_g, self.y: y_g})), self.rounding)

    def calculate_alpha(self):
        """
        g(a) = g(f(x,y)+G(x,y)*a)
        g(a) = g(x + x*a , y + y*a)
        Donde:
        a = alpha = ratio de aprendizaje
        f(x,y) = Valores "x" "y" de la funcion "f"
        G(x,y) = Valores "x" "y" de la Gradiente de "f"
        """
        a = sy.Symbol('a')
        x_g = self.x_i + self.x_grad*a
        y_g = self.y_i + self.y_grad*a
        print(x_g)
        print(y_g)
        gx = self.fx.subs({self.x: x_g, self.y: y_g})
        print(sy.diff(gx, a))
        sys.exit(0)
        r = sy.solve(self.fx.subs({self.x: x_g, self.y: y_g}))
        self.alpha = r[0]
        print(self.alpha)
        return self.alpha

    def show_table_result(self):
        print("\n")
        print("{} {} {} {} {}".format("".ljust(6, "-"), "".ljust(12, "-"),
                                      "".ljust(12, "-"), "".ljust(20, "-"), "".ljust(20, "-")))
        print("{} {} {} {} {}".format("K".center(6), "Punto (X)".center(12), "F(x)".center(
            12), "Vector Gradiente".center(20), "Ratio Aprendizaje (&)".center(20)))
        print("{} {} {} {} {}".format("".ljust(6, "-"), "".ljust(12, "-"),
                                      "".ljust(12, "-"), "".ljust(20, "-"), "".ljust(20, "-")))

        for k in range(len(self.arrayFx)):
            print("{} {} {} {} {}".format(
                str(k+1).center(6),
                str(self.arrayPoints[k]).center(12),
                str(self.arrayFx[k]).center(12),
                str(self.arrayGrad[k]).center(20),
                str(self.arrayAlpha[k]).center(12)))
