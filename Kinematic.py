import math

PI_VALUE = 3.14159265359

FEMUR_LENGTH_VAL = 73
TIBIA_LENGTH_VAL = 17
THETA1_DEGREES_VAL = 40
THETA2_DEGREES_VAL = 30

theta1_radians_final = THETA1_DEGREES_VAL * (PI_VALUE / 180.0)
theta2_radians_final = THETA2_DEGREES_VAL * (PI_VALUE / 180.0)

x_final = (FEMUR_LENGTH_VAL * math.cos(theta1_radians_final) + 
           TIBIA_LENGTH_VAL * math.cos(theta1_radians_final + theta2_radians_final))
y_final = (FEMUR_LENGTH_VAL * math.sin(theta1_radians_final) + 
           TIBIA_LENGTH_VAL * math.sin(theta1_radians_final + theta2_radians_final))

print(f"Panjang Lengan: Femur={FEMUR_LENGTH_VAL}, Tibia={TIBIA_LENGTH_VAL}")
print(f"Rotasi Joint: θ1={THETA1_DEGREES_VAL}°, θ2={THETA2_DEGREES_VAL}°")
print(f"Koordinat Titik Akhir (x, y) : ({x_final:.4f}, {y_final:.4f})")