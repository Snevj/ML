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
    # pyplot.show()
    return pyplot

plotData(x, y)  

x = np.stack([np.ones(m), x], axis=1)

def computeCost(x, y, theta):
    m = len(y)  # number of training examples
    h = x.dot(theta)  # hypothesis
    # Compute the cost function J
    J=0
    J = (1 / (2 * m)) * np.sum(np.square(h - y))
    return J

J = computeCost(x, y, theta=np.array([0.0, 0.0]))
print('With theta = [0, 0] \nCost computed = %.2f' % J)
print('Expected cost value (approximately) 32.07\n')

# further testing of the cost function
J = computeCost(x, y, theta=np.array([-1, 2]))
print('With theta = [-1, 2]\nCost computed = %.2f' % J)
print('Expected cost value (approximately) 54.24')

def gradientDescent(x, y, theta, alpha, num_iters):
    m = len(y)  # number of training examples
    J_history = np.zeros(num_iters)  # to store cost in each iteration

    for i in range(num_iters):
        h = x.dot(theta)  # hypothesis
        theta = theta - (alpha / m) * (x.T.dot(h - y))  # update theta
        J_history[i] = computeCost(x, y, theta)  # save the cost

    return theta, J_history

def runGradientDescent(x, y, alpha=0.01, num_iters=1500):
    # Initialize theta
    theta = np.zeros(2)
    # Run gradient descent
    theta, J_history = gradientDescent(x, y, theta, alpha, num_iters)
    return theta, J_history