# A0191 - محاسبه سینوس

import math

angle_degrees = float(input())
angle_radians = math.radians(angle_degrees)
sin_value = math.sin(angle_radians)

print(f"{sin_value:.4f}")
