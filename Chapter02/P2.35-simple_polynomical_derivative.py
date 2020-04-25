class Term():
    """
    Creates a polyonomial term
    
    coefficient = coefficient of term (i.e. "4" in "4x^2")
    variable = variable of term (i.e. "x" in "4x^2")
    exponent = exponent value of term (i.e. "2" in "4x^2")
    """
    def __init__(self, coef=1, var='x', exp=0):
        """
        Creates Term object with defaul coefficient and exponent of 1 and
        variable of x
        """
        if isinstance(coef, (int, float)):
            self._coefficient = coef
        else:
            raise TypeError('coefficient must be numeric')
        if var.isalpha():
            if len(var) == 1:
                self._variable = var
            else:
                raise ValueError('must contain one variable')
        else:
            raise TypeError('variable must be a letter')
        if isinstance(exp, (int, float)):
            self._exponent = exp
        else:
            raise TypeError('exponent must be numeric')

    def get_coef(self):
        """Returns coefficient of Term"""
        return self._coefficient

    def get_var(self):
        """Returns variable of term"""
        return self._variable

    def get_exp(self):
        """Returns exponent of term"""
        return self._exponent
    
    def derivative(self):
        """Returns the derivative of the term"""
        if self._exponent == 0:
            return Term(coef=0, exp=0)
        else:
            return Term(self._coefficient * self._exponent, self._variable, self._exponent - 1)

    def str_term(self):
        """Returns the string form of the term"""
        temp_str = ''
        if self._coefficient != 1:
            temp_str += str(self._coefficient)
            if self._exponent == 1:
                temp_str += self._variable
            elif self._exponent != 0:
                temp_str += self._variable + '^' + str(self._exponent)
        else:
            if self._exponent == 1:
                temp_str += self._variable
            elif self._exponent != 0:
                temp_str += self._variable + '^' + str(self._exponent)
            else:
                temp_str += str(self._coefficient)
        
        return temp_str

def parse_polynomial(poly):
    """
    Given a string, splits each term in the polynomial and returns them as
    list terms

    Also returns a list of operators in the polynomials

    Example:
    >> parse_polynomial("x^2-3x-8")
    (["x^2", "3x", "8"], ["-", "-"])
    """
    pass

def combine_terms(terms, operators):
    """
    Given a list of terms and operators, combines all strings to form a
    new string
    """
    pass

if __name__ == "__main__":
    # Test Term class
    term1 = Term(-2.3, 'y', 3)
    print(term1.str_term())         # print -2.3y^3
    print("derivative: {}".format(term1.derivative().str_term()))

    term2 = Term(var='x', exp=1)
    print(term2.str_term())         # print x
    print("derivative: {}".format(term2.derivative().str_term()))

    term3 = Term(coef=5)
    print(term3.str_term())         # print 5
    print("derivative: {}".format(term3.derivative().str_term()))

    term4 = Term(coef=4, exp=1)
    print(term4.str_term())         # print 4x
    print("derivative: {}".format(term4.derivative().str_term()))

    term5 = Term(exp=-3)
    print(term5.str_term())         # print x^-3
    print("derivative: {}".format(term5.derivative().str_term()))

    term6 = Term(0)
    print(term6.str_term())         # print 0
    print("derivative: {}".format(term6.derivative().str_term()))


    # poly1 = "x^2-2x-8"
    # # print 2x-2
    # print("derivative of {}: {}".format(poly1, derivative(poly1)))

    # poly2 = "5"
    # # print 0
    # print("derivative of {}: {}".format(poly2, simple_derivative(poly1)))

    # poly3 = "-3z^-1"
    # # print 3z^-2
    # print("derivative of {}: {}".format(poly3, simple_derivative(poly1)))