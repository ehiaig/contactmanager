"""
Create a class with static methods to do conversions:
cm <--> in: 1cm == 0.393701 in
mi <--> km: 1mile == 1.60934
farenheit <--> celsius: 32fh == 0c
gm <--> Pounds: 1gm == 0.00220462pds
litres <--> floz(fluid ounces): 1litres == 33.814fl
"""

class Conversion:
    @staticmethod
    def cm_to_in(cm):
        INCH = 0.393701
        cm = cm*INCH
        return format(cm, '4f')

    @staticmethod
    def in_to_cm(inc):
        CM = 0.393701
        inc = inc/CM
        return format(inc, '4f')

    @staticmethod
    def m_to_km(m):
        KM = 1.60934
        m = m * KM
        return format(m, '4f')

    @staticmethod
    def km_to_m(km):
        M = 1.60934
        km = km / M
        return format(km, '4f')

    @staticmethod
    def f_to_c(fa):
        cel = (fa-32)*(5/9)
        return format(cel, '4f')

    @staticmethod
    def c_to_f(cel):
        fa = (1.8 * cel) + 32
        return format(fa, '4f')

print("----cm to inch conversion----")
print(Conversion.cm_to_in(34))
print(Conversion.in_to_cm(13.385834000000001))
print("----m to km conversion----")
print( Conversion.m_to_km(300))
print(Conversion.km_to_m(345))
print("----Farenheit to celsius conversion----")
print(Conversion.f_to_c(56))
print(Conversion.c_to_f(56))
