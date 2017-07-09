import numpy as np
import numpy.matlib as M
import numpy.random as random

max_r = 20
r = np.around(max_r * random.rand(10, 1))

np.nonzero(np.dot(r,r.T)/r + r == 24)
loc1 = np.nonzero(np.dot(r,r.T)/r + r == 24)[0]
loc2 = np.nonzero(np.dot(r,r.T)/r + r == 24)[1]

for i0 in range(len(loc1)):
    print(loc1[i0], ':', r[int(loc1[i0])], loc2[i0], ':', r[int(loc2[i0])])
print(r)
