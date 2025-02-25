#https://lmcodequestacademy.com/problem/mars-vacation
# START TIME: 10:05
# END TIME: 10:21
# ELAPSED TIME: 16mins DNF

output_dict = {False: "WORKING HARD", True: "VACATION"}
SUN_POS = (0,0)
from math import sqrt, cos, sin, degrees, acos

def is_solar_conjunction(earth_x: float, earth_y: float, mars_x: float, mars_y: float) -> bool:
    a = sqrt(earth_x ** 2 + earth_y ** 2)
    b = abs(mars_x - earth_x)
    c = sqrt(mars_x ** 2 + mars_y ** 2)
    angle = acos((a**2 + b**2 - c**2)/(2 * a * b))
    print(angle)

cases = int(input())
for _ in range(cases):
    line = input()
    earth_x, earth_y, mars_x, mars_y = (float(val) for val in line.split(" "))
    is_solar_conjunction(earth_x, earth_y, mars_x, mars_y)
    # print()