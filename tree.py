import random
ctr = 1
for i in range(5):
    for j in range(1):
        print(' ' * ((9 - ctr) // 2), "*" * ctr, end = "")
    ctr += 2
    print("\n", end = "")
# get tree
'''     *
    ***
   *****
  *******
 *********'''
