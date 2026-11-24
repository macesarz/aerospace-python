import math

altitudes = [0, 3, 6, 9, 11]

def isa_temperature(altitude_km):
    return 15 - 6.5 * altitude_km

def speed_of_sound(temp_c):
    temperature_k = temp_c + 273.15
    return math.sqrt(1.4 * 287.05 * temperature_k)

def mach_number(airspeed, temp_c):
    return (airspeed / speed_of_sound(temp_c))

print("For Aircraft traveling at 250m/s:")
for h in altitudes:
    temp_c = isa_temperature(h)
    mach = mach_number(250, temp_c)
    print(F"At h = {h}km Mach = {mach:.2f}")
    if mach > 0.8:
        print("  transonic warning")

# v_inf = float(input("Airspeed of the Aircraft in m/s: "))
# temperature_c = float(input("Air Temperature in ℃: "))
# temperature_k = temperature_c + 273.15
# speed = math.sqrt(gamma * R * temperature_k)
# speed_knots = speed * 1.94384
# speed_kph = speed * 3.6
# Mach = v_inf/speed
# print(F"Speed of Sound: {speed:.1f}, {speed_kph:.1f}, {speed_knots:.1f}")
# print(F"Mach number: {Mach:.2f}")
# temperature_c = 15 + 6.5
# Mach = 0.85
# print("Altitude[km]     Temperature[℃]     SoS[m/s]     TAS[m/s]")
# for altitude_km in range(0, 11, 1):
#     temperature_c = temperature_c - 6.5
#     temperature_k = temperature_c + 273.15
#     speed = math.sqrt(gamma * R * temperature_k)
#     tas = Mach * speed
#     print(F"{altitude_km:>12}{temperature_c:>18.1f}{speed:>14.1f}{tas:>12.1f}")
#     if altitude_km == 8:
#        print("This is crusing altitude")
    
# mach = 0.85

# if mach < 0.8:
#     regime = "subsonic"
# elif mach < 1.2:
#     regime = "transonic"
# else:
#     regime = "supersonic"

# print(f"Mach {mach}: {regime}")

# for altitude_km in range(0, 50, 10):
#     print(altitude_km, "km")

# fuel = 100.0  # kg
# time = 0

# while fuel > 0:
#     fuel = fuel - 12.5
#     time = time + 1

# print(f"Fuel ran out after {time} seconds")


# temperature_c = -56.5  # air temperature in degrees Celsius
# temperature_k = temperature_c + 273.15

# gamma = 1.4         # ratio of specific heats for air
# R = 287.05          # gas constant for air, J/(kg*K)

# speed = math.sqrt(gamma * R * temperature_k)
# speed_knots = speed * 1.94384  # convert m/s to knots
# v_inf = 250 # speed of the aircraft in m/s
# Mach = v_inf/speed

# print("Speed of sound:", round(speed, 1), "m/s")
# print("Speed of sound:", round(speed_knots, 1), "knots")
# print("Mach number:", round(Mach, 2))

# temperature_c = float(input("Air temperature in °C: "))
# altitude_m = float(input("Altitude in m: "))
# print(f"At {altitude_m} m, the speed of sound is {speed:.0f} m/s")

# print(F"something {1234567.89:,.0f}")