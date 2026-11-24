import math
import csv

g = 9.81
c_d = 0.25
s = 0.2

burn_time_s = 30
dry_mass_kg = 200
propel_mass_kg = 300
thrust_N = 15000

dt = 0.1

def drag_N(velocity, rho):
    return c_d * rho * velocity * abs(velocity) * 0.5 * s

def acceleration(propel_mass_kg, velocity):
    return (thrust_N - drag_N(velocity))/(dry_mass_kg+propel_mass_kg) - g

t=0
h=0
v=0
times = []
altitudes = []
velocities = []

while t<1 or h>0:
    propel_mass_kg = max(0, 300 - 10 * t)
    thrust = thrust_N if t < burn_time_s else 0
    rho = 1.225 * math.exp(-h/8500)
    a = (thrust - drag_N(v,rho))/(dry_mass_kg+propel_mass_kg)-g
    v = v + a * dt
    h = h + v * dt
    t = t + dt
    times.append(round(t, 2))
    altitudes.append(round(h, 1))
    velocities.append(round(v, 2))



print(f"Max speed: {max(velocities):.0f} m/s")
apogee = max(altitudes)
print(f"Apogee: {apogee:.0f} m at t = {times[altitudes.index(apogee)]} s")
print(f"Flight time: {times[-1]} s")

with open("launch.csv", "w", newline="") as out:
    writer = csv.writer(out)
    writer.writerow(["time_s", "altitude_m", "velocity_ms"])
    for i in range(len(times)):
        writer.writerow([times[i], altitudes[i], velocities[i]])
