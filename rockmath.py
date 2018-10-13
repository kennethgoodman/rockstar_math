 #Pi constant
the_pi = 3.1415926535897932
the_e = 2.7182818284590452
the_tau = the_pi * 2
 #Convert degrees to radians
def DegToRad(the_degrees):
    return the_degrees * the_tau / 360
 #Convert radians to degrees
def RadToDeg(the_radian):
    return the_radian * 360 / the_tau
 #Factorial: n!
def Factorial(the_number):
    the_zero = 0
    if the_number == the_zero:
        return 1
    if the_number < the_zero:
        return -1
    the_iterator = 1
    the_answer = 1
    while the_iterator <= the_number:
        the_answer = the_iterator * the_answer
        the_iterator += 1
    return the_answer
 #Abs value
def Absolute_Value(the_number):
    if the_number < 0:
        the_number = the_number * -1
        return the_number
    return the_number
 #Mod: a % m
def Mod(the_number, the_modulo):
    if the_number > 0:
        while the_number >= the_modulo:
            the_number = the_number - the_modulo
        return the_number
    if the_number < 0:
        while the_number < 0:
            the_number = the_number + the_modulo
        return the_number
    return the_number
 #Gcd
def Gcd(the_x, the_y):
    if Mod(the_x, 1) != 0 or Mod(the_y, 1) != 0:
        return "Error: the input must be two integer numbers"
    the_x = Absolute_Value(the_x)
    the_y = Absolute_Value(the_y)
    if the_x == 0:
        return the_y
    if the_y == 0:
        return the_x
    while the_x != the_y:
        if the_x > the_y:
            the_x = the_x - the_y
        else:
            the_y = the_y - the_x
    return the_x
 #Floor
def Floor(the_number):
    the_number = the_number - Mod(the_number, 1)
    return the_number
 #Ceil
def Ceil(the_number):
    the_number = -1 * the_number
    the_number = -1 * Floor(the_number)
    return the_number
 #Power: a^x
def Power(the_base, the_exponent):
    if the_exponent < 0:
        the_newexponent = -1 * the_exponent
        return 1 / Power(the_base, the_newexponent)
     #If the base is 0 and  the exponent is 0
     #Give back "Error: indefinite"
     #
    if the_exponent == 0:
        return 1
    if the_base == 0:
        return 0
    if Mod(the_exponent, 1) == 0:
        return PowerIntegerExponent(the_base, the_exponent)
    else:
        return PowerRealExponent(the_base, the_exponent)
 #PowerIntegerExponent
def PowerIntegerExponent(the_base, the_exponent):
    the_iterator = 1
    the_answer = the_base
    while the_iterator < the_exponent: #Probably can also use divide and conquer exponentiation -> e^n + e^m + ....
        the_answer = the_base * the_answer
        the_iterator += 1
    return the_answer
 #PowerRealExponent
def PowerRealExponent(the_base, the_exponent):
    the_argument = the_exponent * LN(the_base)
    return Exp(the_argument)
 #Exp
def Exp(the_x):
    the_answer = 1
    the_iterator = 1
    while the_iterator < 50:
        the_numerator = Power(the_x, the_iterator)
        the_denominator = Factorial(the_iterator)
        the_term = the_numerator / the_denominator
        the_answer = the_answer + the_term
        the_iterator += 1
    return the_answer
 #Natural Logarithm, always base e
def LN(the_number):
    the_top = the_number - 1
    the_bottom = the_number + 1
    the_x = the_top / the_bottom
    the_iterator = 1
    the_approximation = 0
    while the_iterator < 10: #get reasonable starting point for Halley's method
        the_term = Power(the_x, the_iterator)
        the_term = the_term / the_iterator
        the_approximation = the_approximation + the_term
        the_iterator += 1
        the_iterator += 1
    the_approximation = the_approximation * 2 #end power expansion, start Halley's cubic convergence
    the_iterator = 0
    while the_iterator < 30:
        the_numerator = the_number - Exp(the_approximation)
        the_denominator = the_number + Exp(the_approximation)
        the_term = 2 * the_numerator / the_denominator
        the_approximation = the_approximation + the_term
        the_iterator += 1
    return the_approximation
 #Log with number and base
def LOG(the_number, the_base):
    the_top = LN(the_number)
    the_bottom = LN(the_base)
    return the_top / the_bottom
 #Square Root Function
def Square_Root(the_number):
    the_approximation = 0.5 * the_number
    the_iterator = 1
    the_number = 1.0 * the_number
    while the_iterator < 50:
        the_term = the_number / the_approximation + the_approximation
        the_approximation = 0.5 * the_term
        the_iterator += 1
    return the_approximation
 #Sine
def Sine(the_radian):
    the_iterator = 1
    the_answer = 0
    the_sign = 1
    while the_iterator < 26:
        the_term = Power(the_radian, the_iterator) / Factorial(the_iterator)
        the_term = the_term * the_sign
        the_answer = the_answer + the_term
        the_iterator += 1
        the_iterator += 1
        the_sign = the_sign * -1
    return the_answer
 #Cos
def Cos(the_radian):
    the_iterator = 0
    the_answer = 0
    the_sign = 1
    while the_iterator < 26:
        the_term = Power(the_radian, the_iterator) / Factorial(the_iterator)
        the_term = the_term * the_sign
        the_answer = the_answer + the_term
        the_iterator += 1
        the_iterator += 1
        the_sign = the_sign * -1
    return the_answer
 #Tan
def Tan(the_radian):
    the_numerator = Sine(the_radian)
    the_denominator = Cos(the_radian)
    return the_numerator / the_denominator
 #Arctan
def Arctan(the_number):
    the_iterator = 1
    the_answer = 0
    the_sign = 1
    while the_iterator < 200:
        the_term = Power(the_number, the_iterator) / the_iterator
        the_term = the_term * the_sign
        the_answer = the_answer + the_term
        the_iterator += 1
        the_iterator += 1
        the_sign = the_sign * -1
    return the_answer
 #Arcsin
def Arcsin(the_number):
    the_iterator = 0
    the_answer = 0
    while the_iterator < 80:
        the_placeholder = 2 * the_iterator
        the_numerator = Factorial(the_placeholder)
        the_exponent = 2 * the_iterator + 1
        the_numerator = the_numerator * Power(the_number, the_exponent)
        the_firstdenominator = Power(4, the_iterator)
        the_placeholder = Factorial(the_iterator)
        the_seconddenominator = Power(the_placeholder, 2)
        the_thirddenominator = 2 * the_iterator + 1
        the_denominator = the_firstdenominator * the_seconddenominator * the_thirddenominator
        the_term = the_numerator / the_denominator
        the_answer = the_answer + the_term
        the_iterator += 1
    return the_answer
 #Arccos
def Arccos(the_number):
    the_answer = the_pi / 2
    the_answer = the_answer - Arcsin(the_number)
    return the_answer
 #Sinh
def Sinh(the_number):
    the_iterator = 1
    the_answer = 0
    while the_iterator < 50:
        the_term = Power(the_number, the_iterator) / Factorial(the_iterator)
        the_answer = the_answer + the_term
        the_iterator += 1
        the_iterator += 1
    return the_answer
 #Cosh
def Cosh(the_number):
    the_iterator = 0
    the_answer = 0
    while the_iterator < 50:
        the_term = Power(the_number, the_iterator) / Factorial(the_iterator)
        the_answer = the_answer + the_term
        the_iterator += 1
        the_iterator += 1
    return the_answer
 #Tanh
def Tanh(the_number):
    the_numerator = Sinh(the_number)
    the_denominator = Cosh(the_number)
    return the_numerator / the_denominator
 #Arcsinh
def Arcsinh(the_number):
    the_term = Power(the_number, 2)
    the_term = the_term + 1
    the_argument = the_number + Square_Root(the_term)
    return LN(the_argument)
 #Arccosh
def Arccosh(the_number):
    the_term = Power(the_number, 2)
    the_term = the_term - 1
    the_argument = the_number + Square_Root(the_term)
    return LN(the_argument)
 #Arctanh
def Arctanh(the_number):
    the_numerator = 1 + the_number
    the_denominator = 1 - the_number
    the_argument = the_numerator / the_denominator
    return LN(the_argument) / 2
 #Get binary from decimal
def DecToBin(the_number):
    if the_number <= 1:
        if the_number == 0:
            return "0"
        return "1"
    the_temp = Mod(the_number, 2)
    if the_temp == 0:
        the_temp = "0"
    else:
        the_temp = "1"
    the_number = the_number / 2
    return the_temp + DecToBin(the_number) #doesn't work until we have integer division
