
import numpy as np



def Split_in_3_by_3_Matrix(matrix):
    glass_sum = 0
    for i in range(0,4):

        for j in range(0,4):
            greater_sum = matrix[i][j] + matrix[i][j+1] +matrix[i][j+2]+matrix[i+1][j+1]+matrix[i+2][j] + matrix[i+2][j+1] +matrix[i+2][j+2]           

            print(matrix[i][j],",", matrix[i][j+1] ,",",matrix[i][j+2],",",matrix[i+1][j+1],",",matrix[i+2][j] , ",",matrix[i+2][j+1],",",matrix[i+2][j+2] )

            if greater_sum > glass_sum:
                glass_sum = greater_sum

    return glass_sum          

        
    # print("Three by three matrix \n",three_by_three_matrix)

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
# Array  = np.arange(36).reshape(6,6) # splitting problem in 3 by 3 matrix

# test Case
Array = [1, 1, 1, 0, 0, 0,0, 1, 0, 0, 0, 0,1, 1 ,1 ,0 ,0, 0,0, 0 ,2 ,4, 4, 0,0, 0 ,0 ,2 ,0 ,0,0 ,0 ,1 ,2 ,4 ,0]
Array = np.array(Array).reshape(6,6)
print("Input Array\n",Array)
print("\n\n\n")
print(Split_in_3_by_3_Matrix(Array))
