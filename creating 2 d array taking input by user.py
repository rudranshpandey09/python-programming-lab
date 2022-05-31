import numpy as np
matrix=[]
row=int(input("enter no. of rows:"))
column=int(input("enter no. of colums:"))
for i in range(row):
    a=[]
    for j in range(column):
        
        val=int(input("enter number"))
        
        a.append(val)
        matrix.append(a)
        
        arr=np.array(matrix)
        
for i in range(row):
    
    for j in range(column):
        
        print(arr[i,j],end=" ")
print()
print(type(arr))
