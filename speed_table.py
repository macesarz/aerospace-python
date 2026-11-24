import math

altitudes = [0, 3, 6, 9, 11]

def speed_of_sound(temp_c):
    temp_k = temp_c + 273.15
    return math.sqrt(1.4*287*temp_k)

def isa_temp(altitude):
    return 15 - 6.5 * altitude

def mach_number(air_speed, temp_isa):
    return air_speed/speed_of_sound(temp_isa)

air_speed = float(input("Aircraft airspeed [m/s] : "))

for h in altitudes:
    temp = isa_temp(h)
    mach = mach_number(air_speed, temp)
    print(F"At altitude {h}km the Mach number is {mach:.2f}")
    if mach > 0.8:
        print("Transonic warning")
    