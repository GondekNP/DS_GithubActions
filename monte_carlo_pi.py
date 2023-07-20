"""This module contains a function to estimate the value of pi using the Monte Carlo method."""
import random

def estimate_pi(n):
    """
    Estimate the value of pi using the Monte Carlo method.

    This function generates n random points in the unit square (0, 0) to (1,1)
    and determines the proportion that lies within the unit circle. It then
    multiplies this proportion by 4 to estimate pi.

    Args:
        n (int): The number of random points to generate.

    Returns:
        float: The estimated value of pi.
    """
    num_points_circle = 0
    num_points_total = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            num_points_circle += 1
        num_points_total += 1
    return 4 * num_points_circle / num_points_total

if __name__ == "__main__":
    print(estimate_pi(1000000))