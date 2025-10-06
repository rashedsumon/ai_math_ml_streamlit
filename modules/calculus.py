import numpy as np

def derivative_example():
    # f(x) = x^2
    f = lambda x: x**2
    x = 5
    derivative = 2*x
    return derivative

def gradient_descent_example():
    # Simple gradient descent for f(x) = x^2
    x = 10
    lr = 0.1
    for i in range(10):
        grad = 2*x
        x = x - lr * grad
    return x
