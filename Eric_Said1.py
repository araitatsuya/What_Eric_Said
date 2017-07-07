import numpy as np
import numpy.matlib as M

max_r = 20
r = np.around(max_r * M.rand(10, 1))
print(r)
print('*---------*')

key_num = 24
key_vec = key_num * M.ones(np.shape(r))

#### Potential Pair
r_pair = key_vec - r; 

#for i0 in range(r.shape[0]):
#    for i1 in range(r.shape[1]):
#        print(i0, i1, r[i0,i1])

prd_r = M.zeros(np.shape(r))
for i0 in range(r.shape[0]):
    for i1 in range(r.shape[0]):
        if r_pair[i0] == r[i1]:
            prd_r[i0] = 1
            break

for i0 in range(r[np.nonzero(prd_r)[0]].shape[0]):
    print(np.nonzero(prd_r)[0][i0], r[np.nonzero(prd_r)[0][i0]],r_pair[np.nonzero(prd_r)[0][i0]])
    
