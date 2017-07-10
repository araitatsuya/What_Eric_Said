##########################################
# Assigning A Prime Number to Each Alphabet
#
#
#
########################################
import numpy as np

count = 1
pm_count = 0
str_alphbt ="abcdefghijklmnopqrstuvwxyz"
dict_alphabet_pm = {}
while True:
    isprime = True
    for x in range(2, int(np.sqrt(count) + 1)):
        if count % x == 0: 
            isprime = False
            break
    if isprime:
        print(pm_count, count)
        dict_alphabet_pm[str_alphbt[pm_count]] = count
        pm_count += 1 
    count += 1
    if pm_count > len(str_alphbt) - 1:
        break

#dict_alphabet_pm['a']
