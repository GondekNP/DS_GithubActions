import pytest
from monte_carlo_pi import random_point, in_circle, estimate_pi


def test_random_point():
    x, y = random_point()
    assert 0 <= x <= 1
    assert 0 <= y <= 1


def test_in_circle():
    assert in_circle(0, 0)
    assert in_circle(0.5, 0.5)
    assert not in_circle(1, 1)
    assert not in_circle(1.5, 1.5)


def test_estimate_pi():
    pi = estimate_pi(10000)
    assert 3 < pi < 4


def test_estimate_pi_regression():
    pi = estimate_pi(10000000)
    assert 3.141 < pi < 3.142
