import numpy as np                                                #we are using numpy/scipy libraries
from scipy.optimize import minimize


    #1
#find minimum of first function
print(" №1 - minimum of function x1^2 + x2^2")
fcn_First = lambda x: x[0]**2 + x[1]**2                           # задаю функцию, минимум который ищу
constraintS =[{'type' : 'eq', 'fun' : lambda x: x[0] + x[1] - 4}, # constraintS - условия для переменных x[0], x[1] функции  
             {'type' : 'ineq', 'fun' : lambda x: x[0]},           # eq - равенство нулю выражения из условия 
             {'type' : 'ineq', 'fun' : lambda x: x[1]}]           # ineq - неравенство, выражение из условия больше||равно 0 
x0 = [1,3]
result = minimize(fcn_First, x0, method ='SLSQP', constraints = constraintS)

print(result)
print('')


    #2
# to find maximum of first function we multiply it by (-1)
print(" №2 - maximum of function x1^2 + x2^2")
fcn_Second = lambda x: (-1)*(x[0]**2 + x[1]**2)
constraintS =[{'type' : 'eq', 'fun' : lambda x: x[0] + x[1] - 4},
             {'type' : 'ineq', 'fun' : lambda x: x[0]},
             {'type' : 'ineq', 'fun' : lambda x: x[1]}]
x0 = [1,3]
result1 = minimize(fcn_Second, x0, method ='SLSQP', constraints = constraintS)

print(result1)
print('')



    #3
#find minimum of third function
print(" №3 - minimum of function cos(x1*x2)")
import math
fcn_Third = lambda x: math.cos(x[0]*x[1])
boundS =[(0, math.pi/4), (0, math.pi/3)]                          #задаю границы


x0 = [1,3]
result2 = minimize(fcn_Third, x0, method ='SLSQP', bounds = boundS)

print(result2)
