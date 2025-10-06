import numpy as np
from scipy.stats import norm

def gaussian_example():
    mu, sigma = 0, 1
    x = np.linspace(-3, 3, 100)
    pdf = norm.pdf(x, mu, sigma)
    return x, pdf

def expectation_variance(data):
    mean = np.mean(data)
    variance = np.var(data)
    return mean, variance
