from rockmath import Factorial as rockfactorial, Power, LN as rockln, Square_Root as rocksqrt, Absolute_Value, the_e, the_pi, the_tau, DegToRad, RadToDeg, Mod, LOG as rocklog, Exp, Floor, Ceil, Sine, Cos, Tan, Arctan, Arcsin, Arccos, Sinh, Cosh, Tanh, Arcsinh, Arccosh, Arctanh
from math import factorial as pyfactorial, log as pyln, sqrt as pysqrt, floor, ceil, sin, pi, radians, degrees, cos, tan, atan, asin, acos, sinh, cosh, tanh, asinh, acosh, atanh
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
    assert_close(math.e, the_e, "Approximation of e")

def run_pi_test():
    assert_close(pi, the_pi, "Approximation of pi")
    assert_close(pi*2, the_tau, "Approximation of 2*pi")

def run_degtorad_test():
    for x in [0, 1, 5, 45, 90, 360, 777, -0, -0.1, -75, -360, -1080]:
        print("testing {}° -> radians".format(x))
        assert_close( radians(x), DegToRad(x), "Failed for deg_to_rad({})".format(x))

def run_radtodeg_test():
    for x in [0, 0.5, pi/2, pi, 2*pi, 4.88*pi, -0, -0.25*pi, -pi, -pi*5]:
        print("testing {} * 2*pi -> degrees".format(x))
        assert_close( degrees(x), RadToDeg(x), "Failed for rad_to_deg({})".format(x))

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

def run_arctan_test():
    for x in range(-9,10):
        x/=10
        print("Doing arctan({})".format(x))
        assert_close( atan(x), Arctan(x), "arctan({})".format(x))

def run_arcsin_test():
    for x in range(-9,10):
        x/=10
        print("Doing arcsin({})".format(x))
        assert_close( asin(x), Arcsin(x), "arcsin({})".format(x))

def run_arccos_test():
    for x in range(-9,10):
        x/=10
        print("Doing arccos({})".format(x))
        assert_close( acos(x), Arccos(x), "arccos({})".format(x))

def run_sinh_test():
    for x in [-10, -3, -1, -0.1, 0, 0.1, 1, 3, 10]:
        print("Doing sinh({})".format(x))
        assert_close( sinh(x), Sinh(x), "sinh({})".format(x))

def run_cosh_test():
    for x in [-10, -3, -1, -0.1, 0, 0.1, 1, 3, 10]:
        print("Doing cosh({})".format(x))
        assert_close( cosh(x), Cosh(x), "cosh({})".format(x))

def run_tanh_test():
    for x in [-10, -3, -1, -0.1, 0, 0.1, 1, 3, 10]:
        print("Doing tanh({})".format(x))
        assert_close( tanh(x), Tanh(x), "tanh({})".format(x))

def run_arcsinh_test():
    # for x in [-100000, -1000, -10, -1, 0, 1, 10, 1000, 1000000]:
    for x in [-100, -10, -1, 0, 1, 10, 100]:
        print("Doing arcsinh({})".format(x))
        assert_close( asinh(x), Arcsinh(x), "arcsinh({})".format(x))

def run_arccosh_test():
    # for x in [1.0001, 1.01, 2, 10, 100, 1000, 100000]:
    for x in [1.0001, 1.01, 2, 10, 100]:
        print("Doing arccosh({})".format(x))
        assert_close( acosh(x), Arccosh(x), "arccosh({})".format(x))

def run_arctanh_test():
    # for x in [-0.999, -0.99, -0.9, -0.5, 0, 0.5, 0.9, 0.99, 0.999]:
    for x in [-0.99, -0.9, -0.5, 0, 0.5, 0.9, 0.99]:
        print("Doing arctanh({})".format(x))
        assert_close( atanh(x), Arctanh(x), "arctanh({})".format(x))

def run_dec_to_bin_test():
    pass  # not using until we have integer division

def main():
    run_factorial_test()
    run_power_test()
    run_ln_test()
    run_sqrt_test()
    run_abs_test()
    run_e_test()
    run_pi_test()
    run_degtorad_test()
    run_radtodeg_test()
    run_log_test()
    run_floor_test()
    run_ceil_test()
    run_exponential_test()
    run_mod_test()
    run_sine_test()
    run_cos_test()
    run_tan_test()
    run_arcsin_test()
    run_arccos_test()
    run_arctan_test()
    run_sinh_test()
    run_cosh_test()
    run_tanh_test()
    run_arcsinh_test()
    run_arccosh_test()
    run_arctanh_test()
    run_dec_to_bin_test()

if __name__ == '__main__':
    main()
