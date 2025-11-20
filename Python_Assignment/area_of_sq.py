import math

radius = 42
angle_deg = 60
angle_rad = math.radians(angle_deg)
wire_length = radius * angle_rad
side = wire_length / 4
area = side * side

print(area)
