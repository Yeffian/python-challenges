import numpy as np

def sigmoid(x,deriv=False):
    if(deriv == True):
        return x * (1 - x)
    
    return 1 / (1 + np.exp(-x))
    
# datasets
X = np.array([[0,0,1], [0,1,1], [1,0,1], [1,1,1]])
y = np.array([[0,0,1,1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2 * np.random.random((3, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1

for i in range(10000):
    # layer one, input layer
    l0 = X
    # layer two, connected to layer one by synapse layer 1
    l1 = sigmoid(np.dot(l0, syn0))
    # layer three, connected to layer two by synapse layer 2
    l2 = sigmoid(np.dot(l1, syn1))

    # calculate how off it is
    l2_error = y - l2

    if i % 1000 == 0:
        print('Error:', str(np.mean(np.abs(l2_error))))

    # multiply how much we missed by the 
    # slope of the sigmoid at the values in l1
    l2_delta = l2_error * sigmoid(l2, True)

    # how much did the l1 value contribute to the error for l2
    l1_error = l2_delta.dot(syn1.T)

    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error * sigmoid(l1,deriv=True)

    # update weights
    syn0 += np.dot(l0.T,l1_delta)
    syn1 += np.dot(l1.T, l2_delta)

print("Output after training")
print(l1)
