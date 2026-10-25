import numpy as np
arr1=np.array([[10,20],
              [78,90]])
arr2=np.array([[40,50],
               [45,23]])
new_arr=np.concatenate((arr1,arr2),axis=0)
print(new_arr)