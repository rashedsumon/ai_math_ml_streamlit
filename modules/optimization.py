import numpy as np

def gradient_descent(x_init=0, lr=0.1, iterations=50):
    x = x_init
    for _ in range(iterations):
        grad = 2*x
        x = x - lr*grad
    return x

def regularization_example(weights):
    l2_penalty = 0.01 * np.sum(weights**2)
    return l2_penalty
