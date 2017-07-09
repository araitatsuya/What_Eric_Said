import numpy as np
import numpy.matlib as M

max_r = 20
r = np.around(max_r * M.rand(10, 1))

key_num = 24
key_vec = key_num * M.ones(np.shape(r))

#### Potential Pair
r_pair = key_vec - r; 

#for i0 in range(r.shape[0]):
#    for i1 in range(r.shape[1]):
#        print(i0, i1, r[i0,i1])

prd_r = M.zeros(np.shape(r))
for i0 in range(r.shape[0]):
    for i1 in range(i0, r.shape[0]):
        if r_pair[i0] == r[i1]:
            prd_r[i0] = 1
            break

for i0 in range(r[np.nonzero(prd_r)[0]].shape[0]):
    print(i0, r[np.nonzero(prd_r)[0][i0]],r_pair[np.nonzero(prd_r)[0][i0]])
    

str_vect = "ahourhoutnoaunoturo"

for i_str, c in enumerate(str_vect):
    print(i_str, c)

edibles = ["ham", "spam","eggs","nuts"]
i1 = 0
for food in edibles:
    print(i1, food)
    i1 = i1 + 1

################################################






def ismember(a, b):
    bind = {}
    for i, elt in enumerate(b):
        if elt not in bind:
            bind[elt] = i
    return [bind.get(itm, None) for itm in a] 
