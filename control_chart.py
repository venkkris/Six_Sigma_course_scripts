"""
Author: Venkatesh Krishnamurthy, doctoral candidate,
Department of Materials Science and Engineering,
Carnegie Mellon University. Copyright 2021.

This script reads data from the csv file
(please click save as-> csv in the format when using Excel)
and plots the control charts (X_bar and R charts). 

Note: You have to specify the correct values for n, d2, D3 and D4.

Format for the csv file:
The csv file must have a header row. This is skipped when reading the data.
The first column must be the sample number.
The second column must be the X_bar value.
The third column must be the R value.
A sample csv file has been provided with the name 'control_chart_data.csv'.
"""

import csv
import numpy as np
import math as m
import matplotlib.pyplot as plt

###############################################################################
csv_filename = 'control_chart_data.csv'
n = 5 # Number of measurements in each sample i.e. denominator in X_bar (NOT X_bar_bar!)
L = 3 # Sigma level
d2 = 2.326

D3 = 0
D4 = 2.114
###############################################################################

# Internal variables
sample_no = []
X_bar = []
R = []


# Read data from csv file
with open(csv_filename, 'r') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    next(data)                                                  # Skip header
    for row in data:
        sample_no.append(int(row[0]))
        X_bar.append(float(row[1]))
        R.append(float(row[2]))

# Convert to numpy arrays
X_bar, R = np.array(X_bar), np.array(R)

# Compute centerlines
X_bar_bar = np.mean(X_bar)
R_bar = np.mean(R)

# Compute limits
LCL1_x = X_bar_bar - 1/3* L*R_bar/(m.sqrt(n)*d2)
LCL2_x = X_bar_bar - 2/3* L*R_bar/(m.sqrt(n)*d2)
LCL3_x = X_bar_bar - 3/3* L*R_bar/(m.sqrt(n)*d2)

UCL1_x = X_bar_bar + 1/3* L*R_bar/(m.sqrt(n)*d2)
UCL2_x = X_bar_bar + 2/3* L*R_bar/(m.sqrt(n)*d2)
UCL3_x = X_bar_bar + 3/3* L*R_bar/(m.sqrt(n)*d2)

LCL_r = D3*R_bar
UCL_r = D4*R_bar

# Plot control charts
fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Control Chart')

# X_bar chart
ax1.plot(sample_no, X_bar, 'b-*')
ax1.plot(sample_no, [X_bar_bar]*len(sample_no), color='black', linestyle='-' , linewidth=2, label='Centerline')

ax1.plot(sample_no, [LCL1_x]*len(sample_no), color='red', linestyle='--' , linewidth=1)
ax1.plot(sample_no, [LCL2_x]*len(sample_no), color='red', linestyle='--' , linewidth=1)
ax1.plot(sample_no, [LCL3_x]*len(sample_no), color='red', linestyle='--' , linewidth=2, label='LCL')

ax1.plot(sample_no, [UCL1_x]*len(sample_no), color='green', linestyle='--' , linewidth=1)
ax1.plot(sample_no, [UCL2_x]*len(sample_no), color='green', linestyle='--' , linewidth=1)
ax1.plot(sample_no, [UCL3_x]*len(sample_no), color='green', linestyle='--' , linewidth=2, label='UCL')

ax1.set(xlabel= 'Sample No.', ylabel=r'$\bar{x}$')
ax1.set_xlim([0.95, len(sample_no)+0.05])
ax1.set_title(r'$\bar{x}$ chart')
ax1.legend(loc="upper center", ncol=3)


# R chart
ax2.plot(sample_no, R, 'r-*')
ax2.plot(sample_no, [R_bar]*len(sample_no), color='black', linestyle='-' , linewidth=2, label='Centerline')
ax2.plot(sample_no, [LCL_r]*len(sample_no), color='red', linestyle='--' , linewidth=1, label='LCL')
ax2.plot(sample_no, [UCL_r]*len(sample_no), color='green', linestyle='--' , linewidth=1, label='UCL')
ax2.set(xlabel= 'Sample No.', ylabel='R')
ax2.set_title('R chart')
ax2.set_xlim([0.95, len(sample_no)+0.05])
ax2.legend(loc="upper center", ncol=3)


# Final adjustments and save chart
fig.subplots_adjust(hspace=0.7)
plt.savefig('control_chart.png')
