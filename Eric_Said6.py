import numpy as np
import copy

S1 = "aaaaa"
S2 = "zzzzz"

slen1 = len(S1)
slen2 = len(S2)

## The string length of the final product
wrd_len = len(S1) + len(S2)
wrd_indx = list(range(wrd_len))
Jumps = -1 * np.ones([wrd_len, wrd_len])

#######################################
# Level Order Traversal: Breadth-first-search
# Jumps
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

###################
Tree_a_select = copy.copy(Tree_a[np.nonzero((Tree_a[:,int(len(S1)) - 1] !=  - 1) &(Tree_a[:,int(len(S1))] ==  - 1))[0],:])

intrlv_str_list = [];
for i0 in range(int(Tree_a_select.shape[0])):
    sindx1 = 0
    sindx2 = 0
    intrlv_str_temp = ""
    for i1 in range(wrd_len):
        if (Tree_a_select[i0,:] == i1).any() == True:
            intrlv_str_temp = intrlv_str_temp + S1[sindx1]
            sindx1 = sindx1 + 1
        else:
            intrlv_str_temp = intrlv_str_temp + S2[sindx2]
            sindx2 = sindx2 + 1           
    intrlv_str_list.append(intrlv_str_temp)

#####################

S3 = input("input S3: ")
#S3 = raw_input("input S3")
if S3 in intrlv_str_list:
    print(1)
else:
    print(0)



        
