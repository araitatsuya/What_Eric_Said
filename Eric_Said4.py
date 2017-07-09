import numpy as np
import copy

#######################################
S = "rkrabbjtbbit"
T = "rabbit"

wrd_len = len(S)
t_wrd_len = len(T)

wrd_indx = list(range(wrd_len))
Jumps = -1 * np.ones([wrd_len, wrd_len])

#######################################
#Jumps
#   Row & Value: Original Index 
#   Column: Next Possible Destination
#######################################
for i0 in range(wrd_len):
    jumps_temp = -1 * np.ones([1, wrd_len])
    for i1 in range(int(wrd_len - i0 - 1)):
        jumps_temp[0][int(i0 + i1) + 1] = i0
    Jumps[i0][:] = jumps_temp[0][:]

#######################################
# Initialization
### One letter word
Tree_a = np.hstack([np.array([wrd_indx]).T, -1 * np.ones([wrd_len, wrd_len - 1])])
branch_check = np.zeros([1,wrd_len])
### More than one letter word
i0 = 0
while True:
    if branch_check[0][i0] == 0:
        ### Checking a tip of branch one by one
        tree_a_temp = Tree_a[i0][:]
        jumps_temp = Jumps[int(np.max(tree_a_temp))][:]
        nz_next_indx_v = np.nonzero(jumps_temp == np.max(tree_a_temp))
        for i1 in range(nz_next_indx_v[0].shape[0]):
            tree_a_temp2 = copy.copy(tree_a_temp)
            ### Minimum index number with a value of -1: Next Step
            tree_a_temp2[int(np.min(np.nonzero(tree_a_temp == -1)))] = nz_next_indx_v[0][i1]
            Tree_a = np.vstack([Tree_a, tree_a_temp2])
        ### This branch is checked. 
        branch_check[0][i0] = 1;
        branch_check = np.hstack([branch_check, np.zeros([1, nz_next_indx_v[0].shape[0]])])
    if i0 + 1 >= Tree_a.shape[0]:
        break
    i0 = i0 + 1

#### One letter words
#Tree_a[np.nonzero((Tree_a[:,1 - 1] !=  - 1) &(Tree_a[:,1] ==  - 1))[0],:]
#### Two letter words
#Tree_a[np.nonzero((Tree_a[:,2 - 1] !=  - 1) &(Tree_a[:,2] ==  - 1))[0],:] 

Tree_a_select = copy.copy(Tree_a[np.nonzero((Tree_a[:,t_wrd_len - 1] !=  - 1) &(Tree_a[:,t_wrd_len] ==  - 1))[0],:])

for i0 in range(Tree_a_select.shape[0]):
    tree_a_select = copy.copy(Tree_a_select[i0,:])
    T_cmp = ""
    for i1 in range(tree_a_select.shape[0]):
        if tree_a_select[i1] == -1:
            break
        T_cmp = T_cmp + S[int(tree_a_select[i1])]
    if T_cmp == T:
        S_cmp = ""
        for i2 in range(tree_a_select.shape[0]):
            if np.nonzero(tree_a_select == i2)[0].shape[0] == 1:
                S_cmp = S_cmp + S[i2]
            else:
                S_cmp = S_cmp + "_"
        print(S_cmp)
        

    

