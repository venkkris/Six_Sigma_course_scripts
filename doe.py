"""
Author: Venkatesh Krishnamurthy, doctoral candidate,
Department of Materials Science and Engineering,
Carnegie Mellon University. Copyright 2021.

This script uses yield data from DOE results to fit a linear model
and prints the model parameters (intercept: b0 term in class).
In this script, I've also identified the significant factors 
affecting yield and fitted a simpler model to the data (model2).
This script also plots parity plot for the simpler model
as well as histogram of the residuals, and plots of the residuals
against the input variables x1, x2 and x3. The plots are all 
for the simpler model.
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

x = [[-1,-1,-1,+1,+1,+1,-1],
     [+1,-1,-1,-1,-1,+1,+1],
     [-1,+1,-1,-1,+1,-1,+1],
     [+1,+1,-1,+1,-1,-1,-1],
     [-1,-1,+1,+1,-1,-1,+1],
     [+1,-1,+1,-1,+1,-1,-1],
     [-1,+1,+1,-1,-1,+1,-1],
     [+1,+1,+1,+1,+1,+1,+1]]

y = [99,94,88,85,98,92,90,91]
x, y= np.array(x), np.array(y)

model = LinearRegression().fit(x, y)
print('Coefficient of determination: %.2f' % model.score(x, y))
print('Intercept, coefficients: ', model.intercept_, model.coef_)

x_new = [[-1,-1,1],
        [+1,-1,-1],
        [-1,+1,-1],
        [+1,+1,+1],
        [-1,-1,+1],
        [+1,-1,-1],
        [-1,+1,-1],
        [+1,+1,+1]]
x_new = np.array(x_new)

model2 = LinearRegression().fit(x_new, y)
print('Coefficient of determination: %.2f' % model2.score(x_new, y))
print('Intercept, coefficients: ', model2.intercept_, model2.coef_)


# Predict values for x_new using 2nd model, plot parity plot
y_predict = model2.predict(x_new)
plt.plot(y, y_predict, 'o')
xlim_min = min(min(y), min(y_predict))
x_lim_max = max(max(y), max(y_predict))
plt.xlim([0.95*xlim_min, 1.05*x_lim_max])
plt.ylim([0.95*xlim_min, 1.05*x_lim_max])
plt.plot(np.arange(0.95*xlim_min, 1.05*x_lim_max, 0.1), np.arange(0.95*xlim_min, 1.05*x_lim_max, 0.1), 'k-')
plt.xlabel('True Values')
plt.ylabel('Predicted')
plt.savefig('parity_plot.png')
plt.close()


# Plot residuals histogram
# plt.hist(y_predict-y, bins=5)
# plt.xlabel('Residuals')
# plt.ylabel('Frequency')
# plt.savefig('residuals_histogram.png')
# plt.close()

# Plot residuals histogram with prob. dist. function overlaid
sns.displot(y_predict-y, bins=5, kde=True)
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.savefig('residuals_histogram_new.png')
plt.close()

# Plot residuals against model predicted values
plt.plot(y_predict, y_predict-y, 'o')
plt.xlabel('Predicted')
plt.ylabel('Residuals')
plt.savefig('residuals_vs_predicted.png')
plt.close()

# Plot residuals against x1
plt.plot(x[:,0], y_predict-y, 'o')
plt.xlabel('x1')
plt.ylabel('Residuals')
plt.savefig('residuals_vs_x1.png')
plt.close()

# Plot residuals against x2
plt.plot(x[:,1], y_predict-y, 'o')
plt.xlabel('x2')
plt.ylabel('Residuals')
plt.savefig('residuals_vs_x2.png')
plt.close()

# Plot residuals against x3
plt.plot(x[:,2], y_predict-y, 'o')
plt.xlabel('x3')
plt.ylabel('Residuals')
plt.savefig('residuals_vs_x3.png')
plt.close()
