# A0192 - محاسبه کسینوس

import math

angle_degrees = float(input())
angle_radians = math.radians(angle_degrees)
cos_value = math.cos(angle_radians)

print(f"{cos_value:.4f}")
