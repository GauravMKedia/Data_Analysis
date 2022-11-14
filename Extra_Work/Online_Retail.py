import csv

import pandas as pd
import numpy as np

csv_file = pd.read_csv('D:\Python_Codes\Solar\Online Retail Data.csv')
print(" CSV File is : ")
print(csv_file)

print("\nArray is :")
arr = np.array(csv_file)
print(arr)

target = np.array(csv_file)[:, 1]
print("The target is: ", target)


def unknown_find(arr, t,x):
    sum_alls = 0
    count = 0
    pos = 0
    for i, val in enumerate(t):
        if val != "Na":
            print(f"val is :{val}")
            count += 1
            sum_alls = sum_alls + int(val)
        else:
            pos = i
    arr[:,x][pos]=int(sum_alls/count)
    return arr

unknown_find(arr,arr[:,1],1)
unknown_find(arr,arr[:,2],2)
print("The final value is :", arr)
