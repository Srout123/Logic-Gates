# Logic-Gates
A perceptron is the basic part of a neural network.
Logic gates namely AND, OR,XOR are some of the building blocks of every technological breakthrough for the past decade specially for hardware.
I’ve created a perceptron using numpy that implements this Logic Gates with the dataset acting as the input to the perceptron.




import numpy as np


def AND(x1, x2):
    x = np.array([1, x1, x2])
    w = np.array([-1.5, 1, 1])
    y = np.sum(w*x)
    if y <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([1, x1, x2])
    w = np.array([-0.5, 1, 1])
    y = np.sum(w*x)
    if y <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    x = np.array([1, x1, x2])
    w = np.array([])
    y = np.sum(w*x)
    if y <= 0:
        return 0
    else:
        return 1


if __name__ == '__main__':
    input = [(0, 0), (1, 0), (0, 1), (1, 1)]

    print("AND")
    for x in input:
        y = AND(x[0], x[1])
        print(str(x) + " -> " + str(y))

    print("OR")
    for x in input:
        y = OR(x[0], x[1])
        print(str(x) + " -> " + str(y))

    print("XOR")
    for x in input:
        y = XOR(x[0], x[1])
        print(str(x) + " -> " + str(y))
