# 1) What will happen if a real number is divisible by zero?
# because  zeo is a undefined in mathmatics.
# This is because no number multiplied by zeo can give a result.
# in real situation, it is meaningless, for example, try to share apples among zeo people, which makes no logical sense.


# 2) In some country why appliances works in different frequency works?
# Different countries use different power frequencies, include 50Hz or 60Hz.There have three reasons to explain this situation: environment, cost and losses
# For example, most of Europe, Asia, and Australia use 50 Hz, while North America uses 60 Hz.
# Higher frequency result in increase losses and costs. Once these systems were established, switching became too expansive, so countries kept their original standards.


import math
# 3)Convert c=3+6i to polar coordinates and cartisian coordinates coordinates interpretation conversion and viceversa?
def verify_coordinates(x,y):
    r = math.sqrt(x ** 2 + y ** 2)
    theta_rad = math.atan2(y, x)
    angle = math.degrees(theta_rad)
    # verify
    x_verify = r * math.cos(theta_rad)
    y_verify = r * math.sin(theta_rad)
    return angle,x_verify,y_verify


if __name__ == '__main__':
    x = 3
    y = 6
    angle,x,y = verify_coordinates(3,6)
    print(f"angle = {angle}")
    print(f"x_verify = {x}")
    print(f"y_verify = {y}")