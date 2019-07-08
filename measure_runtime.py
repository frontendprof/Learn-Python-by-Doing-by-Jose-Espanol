# B_R_R
# M_S_A_W



"""
Coding Problem on time module:
Measuring time lapse between execution of code
First class function is passed in higher order function
Using lambda can help us to pass in paramater in function
"""

import time

def measure_runtime(func):
    start=time.time()
    func()
    end=time.time()
    print(end-start)

def powers(limit):
    return [x**2 for x in range(limit)]

measure_runtime(lambda:powers(50000)) # Using lambda can help us to pass in paramater in function
