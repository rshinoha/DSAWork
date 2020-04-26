OPERATORS = ['+', '-', '*', '/']
EXPONENT = '^'

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
                temp_str += self._variable + EXPONENT + str(self._exponent)
        else:
            if self._exponent == 1:
                temp_str += self._variable
            elif self._exponent != 0:
                temp_str += self._variable + EXPONENT + str(self._exponent)
            else:
                temp_str += str(self._coefficient)
        
        return temp_str

def get_num(str_input):
	"""
	Given a string, str_input, returns a valid number. All invalid
	characters and extra decimals will be ignored.
	"""
	numeric_symbols = ['-', '.']
	# stores temp string
	num_str = ''
	for i in range(len(str_input)):
		if str_input[i].isnumeric() or str_input[i] in numeric_symbols:
			num_str += str_input[i]
		if str_input[i] == '-' or len(num_str) > 0:
			numeric_symbols[0] = ''
		if str_input[i] == '.':
			numeric_symbols[1] = ''
	if len(num_str) == 0:
		return 0
	if '.' in num_str:
		return float(num_str)
	else:
		return int(num_str)

def parse_polynomial(str_input):
    """
    Given a string, splits each term in the polynomial and returns them as
    list terms

    Also returns a list of operators in the polynomials

    Example:
    >> parse_polynomial("x^2-3x-8")
    (["x^2", "3x", "8"], ["-", "-"])
    """
    poly = ''.join(str_input.split())
    term_list = []
    operator_list = []
    coef = ''
    var = ''
    exp = ''
    i = 0
    while i < len(poly):
        if not poly[i].isalpha():
            while i < len(poly) and not poly[i].isalpha():
                coef += poly[i]
                i += 1
        if i < len(poly) and poly[i].isalpha():
            var = poly[i]
            i += 1
        if i < len(poly) and poly[i] == EXPONENT:
            i += 1
            if poly[i] == '-':
                exp += poly[i]
                i += 1
            while i < len(poly) and not poly[i] in OPERATORS:
                exp += poly[i]
                i += 1
        term_list.append([coef, var, exp])
        if i < len(poly) and poly[i] in OPERATORS:
            operator_list.append(poly[i])
            i += 1
        coef = ''
        var = ''
        exp = ''
    return term_list, operator_list

def list_to_term(poly_list):
    """
    Given a list of lists containing coefficients, variables, and
    exponents, returns a list of Terms
    """
    i = 0
    term_list = []
    # First variable found in list of potential Term objects
    var_in_list = ''
    # Looks for any explicity declared variables in list
    while i < len(poly_list) and var_in_list == '':
        var_in_list = poly_list[i][1]
        i += 1
    if var_in_list == '':
        var_in_list = 'x'
    i = 0
    while i < len(poly_list):
        if poly_list[i][0] != '':
            coef = get_num(poly_list[i][0])
        else:
            coef = 1
        if poly_list[i][2] == '':
            if poly_list[i][1] == '':
                var = var_in_list
                exp = 0
            else:
                var = poly_list[i][1]
                exp = 1    
        else:
            if poly_list[i][1] != '':
                var = poly_list[i][1]
            else:
                var = var_in_list
            exp = get_num(poly_list[i][2])
        term_list.append(Term(coef, var, exp))
        i += 1
    return term_list

def combine_terms(terms, operators):
    """
    Given a list of terms and operators, combines all strings to form a
    new string
    """
    if len(operators) == 0:
        return (terms[0].str_term())
    else:
        i = 0
        poly_str = term[i].str_term()
        while i < len(operators):
            if operators[i] == '-' and terms[i+1].get_coef() < 0:
                poly_str += '+' + terms[i+1].str_term()[1:]
            else:
                poly_str += operators[i] + terms[i+1].str_term()
    return poly_str

if __name__ == "__main__":
    # Test Term class
    # term1 = Term(-2.3, 'y', 3)
    # print(term1.str_term())         # print -2.3y^3
    # print("derivative: {}".format(term1.derivative().str_term()))

    # term2 = Term(var='x', exp=1)
    # print(term2.str_term())         # print x
    # print("derivative: {}".format(term2.derivative().str_term()))

    # term3 = Term(coef=5)
    # print(term3.str_term())         # print 5
    # print("derivative: {}".format(term3.derivative().str_term()))

    # term4 = Term(coef=4, exp=1)
    # print(term4.str_term())         # print 4x
    # print("derivative: {}".format(term4.derivative().str_term()))

    # term5 = Term(exp=-3)
    # print(term5.str_term())         # print x^-3
    # print("derivative: {}".format(term5.derivative().str_term()))

    # term6 = Term(0)
    # print(term6.str_term())         # print 0
    # print("derivative: {}".format(term6.derivative().str_term()))

    poly1 = "2x+2"
    poly2 = "x^2+3.5x-2"
    poly3 = "-1.2x - 2"
    poly4 = "3"

    t1, o1 = parse_polynomial(poly1)
    term_list1 = list_to_term(t1)


    # t2, o2 = parse_polynomial(poly2)
    # term_list2 = list_to_term(t2)

    # t3, o3 = parse_polynomial(poly3)
    # term_list3 = list_to_term(t3)

    # t4, o4 = parse_polynomial(poly4)
    # term_list4 = list_to_term(t4)