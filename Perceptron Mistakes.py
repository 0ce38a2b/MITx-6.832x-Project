import numpy as np
import math

theta = np.array([0,0])
x = [np.array([np.cos(math.pi),0]), np.array([0,np.cos(2*math.pi)])]
y = [1,1]

num = 0

for t in range(20):
  for i in range(len(y)):
    if( y[i]*np.dot(theta,x[i]) <= 0):
        theta = theta + y[i]*x[i]
        print(theta)
        num += 1
print(num)
