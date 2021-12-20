"""
Author: Venkatesh Krishnamurthy, doctoral candidate, 
Department of Materials Science and Engineering,
Carnegie Mellon University. Copyright 2021.

This script generates the OC curves for different values of n and c
And also calculates the probability of accepting a batch given the sampling parameters
Sampling parameters: n (number of trials), c (acceptance number), 
p (probability of defect/defect fraction in the lot being sampled).
"""

# Import modules
import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

###############################################################################
# This function plots the OC curve for a given set of three number of trials and acceptance numbers
def plot_OC_curve(x, n1, c1, n2, c2, n3, c3, filename):
    y1 = binom.cdf(c1, n1, x)
    y2 = binom.cdf(c2, n2, x)
    y3 = binom.cdf(c3, n3, x)

    plt.plot(x, y1, label='n = '+str(n1)+', c = '+str(c1), color='red', linewidth=2)
    plt.plot(x, y2, label='n = '+str(n2)+', c = '+str(c2), color='green', linewidth=2)
    plt.plot(x, y3, label='n = '+str(n3)+', c = '+str(c3), color='blue', linewidth=2)

    plt.xlabel('Probability defective')
    plt.ylabel('Probability of acceptance')
    plt.legend()
    plt.xlim(0, 0.1)
    plt.title('OC Curve')
    #plt.show()
    plt.savefig(filename)
    plt.close()
###############################################################################

# Main
c = 12
n = 598
p_good = 0.01
print('Probability of accepting a lot with a sample size {n}, acceptance number {c} and probability {p_good}: {:.4%}'.format(binom.cdf(c, n, p_good), c=c, n=n, p_good=p_good))


# Plot OC curve
# The first two arguments for the linspace are the limits of the x-axis 
# i.e. the lower and upper limits of p for which the x axis of the OC curve is to be plotted.
x = np.linspace(1e-6, 0.1, 100)
n1 = 90 # Number of trials
n2 = 90
n3 = 90
c1 = 0 # Acceptance number
c2 = 1
c3 = 2
plot_OC_curve(x, n1, c1, n2, c2, n3, c3, 'OC_curve.png')
