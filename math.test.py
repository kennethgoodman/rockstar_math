from rockmath import Factorial as rockfactorial, Power, LN as rockln, Square_Root as rocksqrt, Absolute_Value, the_e, the_pi, Mod, LOG as rocklog, Exp, Sine, Cos, Tan
from math import factorial as pyfactorial, log as pyln, sqrt as pysqrt, floor, ceil, sin, pi, cos, tan

import math

def run_factorial_test():
    for i in range(25):
        print("testing factorial({})".format(i))
        assert rockfactorial(i) == pyfactorial(i)
    assert rockfactorial(-1) == -1

def close(x,y):
    return abs(x - y) < 1e-10 

def assert_close(x, y, m=""):
    if close(x,y):
        assert True
    else:
        assert False, "py({}) is not close to rock({})-{}".format(x,y,m)

def run_power_test():
    for x in range(10):
        for n in range(10):
            print("testing {}**{}".format(x,n))
            assert_close(x**n, Power(x,n), "Failed for {}**{}".format(x,n))

def run_sqrt_test():
    for x in range(1, 100):
        print("testing sqrt({})".format(x))
        assert_close(pysqrt(x), rocksqrt(x), "Failed for sqrt({})".format(x))

def run_ln_test():
    for x in range(1, 50):
        print("testing ln({})".format(x))
        assert_close(pyln(x), rockln(x), "Failed for ln({})".format(x)) 

def run_abs_test():
    for x in [-1, -40, -3.3, 0, 3, 32, 2]:
        print("testing abs({})".format(x))
        assert_close(abs(x), Absolute_Value(x), "Failed for abs({})".format(x))

def run_e_test():
    assert_closer(math.e, the_e, "Approximation of e")

def run_pi_test():
    assert_close(pi, the_pi, "Approximation of pi")
    assert_close(pi/2, the_pi/2, "Approximation of half pi")

def run_log_test():
    for x in range(1, 10):
        for b in range(2, 5):
            print("testing log_{}({})".format(b,x))
            assert_close(pyln(x,b), rocklog(x, b),"Failed for log_{}({})".format(b,x))

def run_floor_test():
    for x in [-2.99, -2.5, -1, 0, -0.0, 2, 4.001, 4.999]:
        print("testing floor({})".format(x))
        assert_close(floor(x), Floor(x), "Failed for floor({})".format(x))

def run_ceil_test():
    for x in [-2.99, -2.5, -1, 0, -0.0, 2, 4.001, 4.999]:
        print("testing ceil({})".format(x))
        assert_close(ceil(x), Ceil(x), "Failed for ceil({})".format(x))

def run_exponential_test():
    for x in range(10):
        print("testing e ^ {}".format(x))
        assert_close( math.e ** x, Exp(x), "Failed for e ^ {}".format(x))

def run_mod_test():
    for x in range(-25, 25):
        for m in range(1, 10):
            print("testing {} % {}".format(x,m))
            assert_close(x % m, Mod(x,m), "Failed for {} % {}".format(x,m))

def run_sine_test():
    for x in range(8):
        print("Doing sin({} * pi / 8)".format(x))
        x *= pi / 8
        assert_close( sin(x), Sine(x), "Sin({})".format(x))

def run_cos_test():
    for x in range(-8,9):    
        print("Doing cos({} * pi / 8)".format(x))
        x *= pi / 8
        assert_close( cos(x), Cos(x), "cos({})".format(x))

def run_tan_test():
    for x in range(-7, 7):
        print("Doing tan({} * pi / 2)".format(x))
        x *= pi / 16
        assert_close( tan(x), Tan(x), "tan({})".format(x))

def run_dec_to_bin_test():
    pass  # not using until we have integer division

def main():
    run_factorial_test()
    run_power_test()
    run_ln_test()
    run_sqrt_test()
    run_abs_test()
    run_pi_test()
    run_log_test()
    run_floor_test()
    run_ceil_test()
    run_exponential_test()
    run_mod_test()
    run_sine_test()
    run_cos_test()
    run_tan_test()
    run_dec_to_bin_test()

if __name__ == '__main__':
    main()
