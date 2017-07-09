##########################
# Palindrome
#
#
##########################
import numpy as np
import copy

S = "eabcdcbacbacbc"

for i0 in range(len(S)): ### From Head
    if i0 == 0:
        for i1 in range(len(S)): ### From Tail
            S_b = copy.copy(S[-1 - i1::-1])
            if i1 == 0:
                S_f = copy.copy(S)
            else:
                S_f = copy.copy(S[:-i1])
            #Print
            if S_f == S_b and len(S_f) >= 1:
                print(i0,len(S) - i1 - 1, S_f, S_b)
    else:
        for i1 in range(len(S)): ### From Tail
            S_b = copy.copy(S[-1 - i1:i0 - 1:-1])
            if i1 == 0:
                S_f = copy.copy(S[i0:])
            else:
                S_f = copy.copy(S[i0:-i1])
            #Print
            if S_f == S_b and len(S_f) >= 1:
                print(i0,len(S) - i1 - 1, S_f, S_b)

