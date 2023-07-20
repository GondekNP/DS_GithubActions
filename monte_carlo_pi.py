## function that uses the monte carlo method to estimate pi
import random


def random_point():
    """Generate a random point in the unit square (0,0) to (1,1)."""
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    return x, y


def in_circle(x, y):
    """Check whether the point (x, y) lies within the unit circle."""
    distance = x**2 + y**2
    return distance <= 1


def estimate_pi(n):
    """
    Estimate the value of pi using the Monte Carlo method.

    Args:
        n (int): The number of random points to generate.

    Returns:
        float: The estimated value of pi.
    """
    num_points_circle = 0
    num_points_total = 0
    for _ in range(n):
        x, y = random_point()
        if in_circle(x, y):
            num_points_circle += 1
        num_points_total += 1

    return 4 * num_points_circle / num_points_total

if __name__ == "__main__":
    print(estimate_pi(1000000))