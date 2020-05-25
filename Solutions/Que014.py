#The area of a circle is defined as r^2. Estimate \pi to 3 decimal places using a Monte Carlo method.
#Hint: The basic equation of a circle is x^2 + y^2 = r^2.

import random,math

def is_cirle(x,y):
    return x*x+y*y<=0.5*0.5

def area():
    num_of_tests = 10000000
    circle_points=0
    for i in range(num_of_tests):
        x=random.uniform(-0.5,0.5)
        y=random.uniform(-0.5,0.5)

        if (is_cirle(x,y)):
            circle_points+=1
    pi=4 *(circle_points/num_of_tests)
    print("%.3f" % pi)

area()