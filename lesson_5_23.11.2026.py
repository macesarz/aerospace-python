import csv
import math

def speed_of_sound(temp_c):
    temp_k = temp_c + 273.15
    return math.sqrt(1.4*287*temp_k)

def isa_temp(altitude):
    return 15 - 6.5 * altitude

def mach_number(air_speed, temp_isa):
    return air_speed/speed_of_sound(temp_isa)

altitudes_km = []
machs = []


with open("flight_log.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        altitude = float(row["altitude_m"])
        speed = float(row["speed_ms"])
        altitude_km = altitude / 1000  
        altitudes_km.append(altitude_km)
        temp_isa = isa_temp(altitude_km)
        mach = mach_number(speed, temp_isa) 
        machs.append(mach)
        
print(f"Maximum altitude: {max(altitudes_km):.1f} km")
print(f"Highest Mach number: {max(machs):.2f}")

with open("results.csv", "w", newline="") as out:
    writer = csv.writer(out)
    writer.writerow(["altitude_km", "mach"])
    for i in range(len(altitudes_km)):
        writer.writerow([altitudes_km[i], round(machs[i], 3)])
    # inside a loop: writer.writerow([a, m])