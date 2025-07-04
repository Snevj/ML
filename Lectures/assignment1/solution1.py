import numpy as np #used for working with matrices in python
import matplotlib.pyplot as pyplot #used with graphs 
import utils #contains helper function
import os
from mpl_toolkits.mplot3d import Axes3D  # needed to plot 3-D surfaces

# Warm-up exercise, this creates a 5x5 identity matrix and prints it.
def warmUpExercise():
    A = np.eye(5)
    print (A)
    return A

# Load the data from a text file
data = np.loadtxt(os.path.join('data', 'ex1data1.txt'), delimiter=',')
x = data[:, 0]  # first column
y = data[:, 1]  # second column
m = len(y)  # number of training examples

def plotData(x, y):
    # plt.figure(figsize=(8, 6))
    # plt.scatter(x, y, marker='o', color='r', label='Training data')
    # plt.xlabel('Population of City in 10,000s')
    # plt.ylabel('Profit in $10,000s')
    # plt.title('Profit vs Population')
    # plt.legend()
    # plt.grid(True)
    # plt.show()
    pyplot.plot(x, y, 'ro', ms=10, mec='k')
    pyplot.ylabel('Profit in $10,000')
    pyplot.xlabel('Population of City in 10,000s')
    fig = pyplot.figure()
    return pyplot
plotData(x, y)  
