import math

lcm = lambda a, b : (a*b)//math.gcd(a, b)
result = 1
for i in range(1, 21):
    result = lcm(result, i)

print("The smallest positive number is", result)