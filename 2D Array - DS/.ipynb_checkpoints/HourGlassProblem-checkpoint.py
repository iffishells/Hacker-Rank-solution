
import numpy as np

def Split_in_3_by_3_Matrix(matrix):

    i = 0 
    j = 3
    three_by_three_matrix = []
    for row_index in range(0,len(matrix)):
        row = matrix[row_index]
        for z in range(4):
            mat = row[i:j]
            i +=1
            j +=1
            print(mat)
        break
        
    print("Three by three matrix \n",three_by_three_matrix)

    # return mat  #matrix

def SumhourGlass_3_X_3_Matrix(arr):
    '''This funtion take the 3 by 3 matrix return the Sumhourglass'''
    # Summing floor Array
    count = 0
    for outer in range(0,len(arr)):
        oneD = arr[outer]  # one Dim Array

        if outer==0:
            count += sum(oneD)
        if outer==1:
            count+= oneD[1]
        if outer==2:
            count+= sum(oneD)

        

        print(count) 
    # return arr


# Test Case for SumhourGlass_3_X_3_Matrix
# Array = np.arange(36).reshape(6,6) # general Array

# Array  = np.arange(9).reshape(3,3) # splitting problem in 3 by 3 matrix
# print("Input Array \n",Array)
# print(SumhourGlass_3_X_3_Matrix(Array))


# Test Case for General Matrix 
Array  = np.arange(36).reshape(6,6) # splitting problem in 3 by 3 matrix
print("Input Array \n",Array)
print(Split_in_3_by_3_Matrix(Array))
