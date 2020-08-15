# -*- coding: utf-8 -*-

import sympy as sy
from sympy.parsing.latex import parse_latex
import os
import sys
from GradientDescent import GradientDescent


class Application(object):
    def __init__(self):
        self.x, self.y, self.config = sy.Symbol('x'), sy.Symbol('y'), {}
        self.x_ini, self.y_ini = 0,0

    def f(self, x, y):
        """
        Función f(x) que contiene la ecuación.
        """
        return ((x-2)**4)+(x-2*y)**2

    def run(self):
        self.input_values()
        self.setConfig()
        self.run_gradient()

    def input_values(self):
        os.system('clear')
        print("\n")
        print(" Aplicacion del metodo de la Gradiente Descendente")
        print("----------------------------------------------------")
        print("\nIngresar el Punto de Inicio")
        self.x_ini = float(input("x: "))
        self.y_ini = float(input("y: "))

    def setConfig(self):
        self.config['rounding'] = 3
        self.config['min_value_fx'] = 0.01
        self.config['x_ini'] = self.x_ini
        self.config['y_ini'] = self.y_ini

    def run_gradient(self):
        gd = GradientDescent(self.x, self.y, self.f(
            self.x, self.y), self.config)
        gd.run()


if __name__ == "__main__":
    try:
        app = Application()
        app.run()
    except (Exception, TypeError, IndexError) as err:
        print("Exception: ", err)
