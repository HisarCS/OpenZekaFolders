import numpy as np
from scipy.optimize import fsolve



def quadraticSolver(array, value):
    # print("printing the quadratic things \n")
    # print(array[0] * (value ** 2))
    # print(array[1] * value)
    # print(array[2])
    return array[0] * (value ** 2) + array[1] * value + array[2]

def integralSquareFinder(equation, lowRange, highRange):
    if lowRange < 0:
        return (quadraticSolver(equation, highRange) + quadraticSolver(equation, lowRange)) ** 2
    else:
        return (quadraticSolver(equation, highRange) - quadraticSolver(equation, lowRange)) ** 2

def linearIntegralFinder(equation, c=0):
    integral = list()
    integral.append(equation[0] / 2.0)
    integral.append(equation[1])
    integral.append(c)

    return integral

def diffBetweenEqs(equation1, equation2):
    resultantEq = list()
    resultantEq.append(equation1[0] - equation2[0])
    resultantEq.append(equation1[1] - equation2[1])
    return resultantEq

def polyFit(xAxis, yAxis, degree):
    equation = list()
    if degree is 1:
        equation.append(np.polyfit(xAxis, yAxis, 1)[0])
        equation.append(np.polyfit(xAxis, yAxis, 1)[1])
    else:
        equation = []
    return equation

def findIntersection(eq1,eq2,x0):
    fun1 = np.poly1d(eq1)
    fun2 = np.poly1d(eq2)

    return fsolve(lambda x : fun1(x) - fun2(x),x0)

x1 = 0.0
x2 = 1.0

y1 = 1.0
y2 = 1.0

eq1 = polyFit((x1, x2), (y1, y2), 1)
# print(eq1)


x1 = 0
x2 = 1

y1 = 0
y2 = 3

eq2 = polyFit((x1, x2), (y1, y2), 1)
# print(eq2)


diffEq = diffBetweenEqs(eq1, eq2)

integral = linearIntegralFinder(diffEq)

intersectionPoint = findIntersection(eq1, eq2, 0.0)

# print(intersectionPoint[0] - 5.0)

area = integralSquareFinder(integral,  2,  5.0)


print(intersectionPoint)

print(area)

