# B_R_R
# M_S_A_W


class MyCustomError(TypeError):
    """
    This is our own custom error inherited from TypeError, not only shows error message,
    but also it displays error code too.
    """
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code=code
        self.message=message


#raise MyCustomError("Ouch. Hurts right? Think carefully then. :)",452)

var_1=MyCustomError("Ouch. Hurts right? Think carefully then. :)",452)
print(var_1.__doc__)
