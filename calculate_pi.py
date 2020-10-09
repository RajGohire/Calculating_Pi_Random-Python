import random
import math

def calculate_pi(num):
    total_points_circle, total_points = 0, 0
    for i in range(num):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            total_points_circle += 1
        total_points += 1
    return 4 * total_points_circle / total_points

num = int(input("Enter number of points to generate: "))
print(calculate_pi(num))
