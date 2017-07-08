import numpy as np
import numpy.matlib as M

max_r = 20
r = np.around(max_r * M.rand(10, 1))

np.nonzero(np.dot(r,r.T)/r + r == 24)

