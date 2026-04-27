# The line imports the pyplot module from the matplotlib library to create plots and visualizations.
import matplotlib.pyplot as plt
# Numpy is a powerful library for numerical computing in Python, providing support for arrays, operations, and functions.
import numpy as np


class Calc():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = np.linspace(-10, 10, 100)  # Range of x values for plotting

# Determines which function activates based on user input
    def activeFunction(self):
        userIn = input(
            "What type of graph are you trying to solve? Enter 1 for vertical asymptote with discontinuity, or 2 for vertical and horizontal asymptote with discontinuity: ")

        if userIn == '1':
            self.verDisco()
        elif userIn == '2':
            self.vertHorDisc()
        else:
            print('Equations not found')

    def multiplyBinomial(self):
        if self.a != '' and self.b != '':
            eqCoefOne = 1
            eqcoefTwo = (int(self.a) * -1) + (int(self.b) * -1)
            eqconst = (int(self.a) * -1) * (int(self.b) * -1)

            quadraticStr = ("The resulting quadratic is: " + str(eqCoefOne) +
                            "x² + " + str(eqcoefTwo) + "x + " + str(eqconst))

            return lambda x: eqCoefOne*x**2 + eqcoefTwo*x + eqconst
        else:
            print('Invalid inputs')
            return None

# Does math for rational equation with only a vertical symptote with a discontinuity
    def verDisco(self):
        a = input("What is the value of a? ")
        c = input("What is the value of d? ")

        if a != '' and c != '':
            eq2CoefOne = 1
            eqCoefTwo = (int(a) * -1) + (int(c) * -1)
            eq2Const = (int(a) * -1) * (int(c) * -1)

            def equation(x): return self.multiplyBinomial()(x) / \
                (eq2CoefOne * x**2 + eqCoefTwo * x + eq2Const)
                

            self.plotEquation(equation)
        else:
            print('Invalid inputs')

# Does math for rational equation with only a vertical and horizontal symptote with a discontinuity
    def vertHorDisc(self):
        v = input("What is the vertical asymptote: ")
        d = input("What is the discontinuity: ")
        xInter = input("What is the x-intercept: ")

        if v != '' and d != '' and xInter != '':
            vert = int(v) * -1
            disc = int(d) * -1
            xInter = int(xInter) * -1
            def equation(x): return (x - disc) * (x - xInter) / \
                ((x - disc) * (x - vert))

            self.plotEquation(equation)
        else:
            print('Not valid input')

    def plotEquation(self, equation):
        # Generate y values for the given equation using the x values
        y = equation(self.x)

        # Plot the equation
        plt.plot(self.x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Graph')
        plt.grid(True)
        plt.show()
        # Save the plot as an image file
        plt.savefig('graph.png')


# Needed to run properly
# a = int(input("This is a test type 1: "))
a = 0
# b = int(input("This is another test type 2: "))
b = 0
calc_instance = Calc(a, b)
calc_instance.activeFunction()
