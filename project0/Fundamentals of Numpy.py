# x = np.array([1,5])
# np.zeros([]) , np.ones([]) , np.random.random([])
# access the dimensions of Numpy array: .shape
# transpose: .transpose()
# elementwise multiplication: *
# matrix multiplication: np.matmul()
# np.exp() x^e
# np.sin(), np.cos(), np.tanh()
# .max(), .min()
# 产生一个随机数: np.random.random()
# norm(linear algebra): np.linalg.norm(x)

'''Write a function called randomization that takes as input a positive integer n, and returns A, a random n x 1 Numpy array.

Available Functions: You have access to the NumPy python library as np
'''

import numpy as np


def randomization(n):
    """
    Arg:
      n - an integer
    Returns:
      A - a randomly-generated nx1 Numpy array.
    """
    # Your code here
    return np.random.random([n, 1])

    raise NotImplementedError


print(randomization(5))

'''Write a function called operations that takes as input two positive integers h and w,
   makes two random matrices A and B, of size h x w, and returns A,B, and s, the sum of A and B.

Available Functions: You have access to the NumPy python library as np'''


def operations(h, w):
    """
    Takes two inputs, h and w, and makes two Numpy arrays A and B of size
    h x w, and returns A, B, and s, the sum of A and B.

    Arg:
      h - an integer describing the height of A and B
      w - an integer describing the width of A and B
    Returns (in this order):
      A - a randomly-generated h x w Numpy array.
      B - a randomly-generated h x w Numpy array.
      s - the sum of A and B.
    """
    # Your code here
    A = np.random.random([h, w])
    B = np.random.random([h, w])
    s = A + B

    return A, B, s
    raise NotImplementedError


'''Write a function called norm that takes as input two Numpy column arrays A and B, 
   adds them, and returns s, the L2 norm of their sum.

Available Functions: You have access to the NumPy python library as np'''


def norm(A, B):
    """
    Takes two Numpy column arrays, A and B, and returns the L2 norm of their
    sum.

    Arg:
      A - a Numpy array
      B - a Numpy array
    Returns:
      s - the L2 norm of A+B.
    """
    # Your code here
    s = A + B
    L2 = np.linalg.norm(s)

    return L2
    raise NotImplementedError
