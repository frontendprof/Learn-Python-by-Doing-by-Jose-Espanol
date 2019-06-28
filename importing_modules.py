# B_R_R
# M_S_A_W


"""
We import chunk of code from addition.py, class name Addition below:

class Addition:
    @classmethod
    def add(cls, num1, num2):
        return num1+num2
        
From this only add method we have to find multiply, subtract, divide and add 
operations in Calculator class.
"""


from addition import Addition


class Calculator:

    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)  # make use of add() from addition module

    @classmethod
    def subtract(cls, num1, num2):
        return cls.add(num1, -num2)

    @classmethod
    def multiply(cls, num1, num2):
        res = 0
        for x in range(0, num1):
            res = cls.add(res, num2)
        return res

    @classmethod
    def divide(cls, num1, num2):
        res = 0
        while num1 >= num2:
            num1 = cls.subtract(num1, num2)
            res = cls.add(res, 1)
        return res
