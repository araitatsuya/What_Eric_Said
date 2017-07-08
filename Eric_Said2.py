import numpy as np
import numpy.matlib as M
import numpy.random as random
import matplotlib.pyplot as plt
import copy

### Initial Matrix
m = 4
n = 6

#A = np.around(M.rand(m,n))
A = np.around(ramdom.rand(m,n))

#m_max = np.sum(A, axis = 0).max(axis = 1).item(0) # In case of MATRIX
#n_max = np.sum(A, axis = 1).max(axis = 0).item(0) # In case of MATRIX
m_max = np.sum(A, axis = 0).max(axis = 0)
n_max = np.sum(A, axis = 1).max(axis = 0)

p_rec_max = np.sum(A)
a_vec = A.reshape([m*n, 1])

i_mask_stack = 0
for i0 in range(int(m_max)):
    for i1 in range(int(n_max)):
        #Mask = M.zeros([m,n]) # Matrix
        Mask = np.zeros([m,n])
        Mask[0:i0 + 1, 0:i1 + 1] = 1
        if (np.sum(Mask) > p_rec_max) or (np.sum(Mask) > m_max * n_max):
            break
        else:
            mask = Mask.reshape([m*n, 1])
            if i_mask_stack == 0:
                mask_stack = copy.copy(mask[:])
                #mask_stack = np.hstack((M.zeros(mask.shape), mask))
                i_mask_stack = i_mask_stack + 1
            else:
                mask_stack = np.hstack((mask_stack, mask))
                i_mask_stack = i_mask_stack + 1
            mask_shift = copy.copy(mask[:])
            for i2 in range(n * m):
                mask_shift[1:] = mask_shift[:-1]
                mask_shift[0] = 0
                #if (m % (i2 + 1)) + i0 <= m:
                mask_stack = np.hstack((mask_stack, mask_shift))
                i_mask_stack = i_mask_stack + 1
                if mask_shift[-1] == 1:
                    break
         
imgplot = plt.imshow(mask_stack)
plt.show()

rect_eval1 = np.dot(a_vec.T, mask_stack)
loc1 = np.nonzero(rect_eval1 == np.sum(mask_stack, axis = 0))
rect_eval2 = rect_eval1[loc1]
#loc2 = loc1[1][np.nonzero(rect_eval2 == np.max(rect_eval2, axis = 1))[1]] # When the rect2 is MATRIX
loc2 = loc1[1][np.nonzero(rect_eval2 == np.max(rect_eval2, axis = 0))]

#loc2 = np.zeros(np.nonzero(rect_eval2 == np.max(rect_eval2, axis = 1))[1].shape)
#for i0 in range(np.nonzero(rect_eval2 == np.max(rect_eval2, axis = 1))[1].shape[0]):
#    loc2[i0] = loc1[1][np.nonzero(rect_eval2 == np.max(rect_eval2, axis = 1))[1][i0]]

#loc2 = np.zeros(np.nonzero(rect_eval2 == 3)[1].shape)
#for i0 in range(np.nonzero(rect_eval2 == 3)[1].shape[0]):
#    loc2[i0] = np.nonzero(rect_eval2 == 3)[1][i0]                

Mask_2 = np.zeros(np.shape(A))
for i0 in range(len(loc2)):
    mask_2 = mask_stack[:,int(loc2[i0])]
    Mask_2_temp = mask_2.reshape([m, n])

# Two subplots sharing both x/y axes
plt.subplot(1, 2, 1)
plt.imshow(A)
plt.subplot(1, 2, 2)
plt.imshow(Mask_2_temp)

plt.show()


            
                
                
