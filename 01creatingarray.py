import numpy as np

# Create a NumPy ndarray Object---
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

arr1=np.array((1,2,3,4))
print(arr1)
print(type(arr1))


#Dimensions in Arrays-------------------

# 0-D Arrays
arr = np.array(42)
print("0-D array: ",arr)

# 1-D Arrays
arr =np.array([1,2,3,4,5])
print("1-D array: ",arr)

# 2-D Arrays
arr = np.array([[1,2,3,],[1,2,3]])
print("2-D array: ",arr)

# 3-D Arrays
arr = np.array([[[1,2,3],[1,2,3]],[[2,3,4],[7,8,9]]])
print(arr)


# Check Number of Dimensions? ------------------------

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Creating Array ------------------------

zero = np.zeros((3,4)) #if you want to make matrix of 3 row and 4 column filled with zero
print(zero)

ones = np.ones((2,3)) #if you want to make matrix of 2 row and 3 column filled with one
print(ones)

full = np.full((2,2),7) #if you want to make matrix of 2 row and 2 column filled with cusomized ones 7
print(full)

random = np.random.random((2,3)) #if you want to make matrix of 2 row and 3 column filled with random no.
print(random)

sequence = np.arange(0,19,2) # Result [ 0  2  4  6  8 10 12 14 16 18] start from 0 end with 18by skiping 2
print(sequence)


# Array Propieties -------------------------

arr = np.array([[2,3,4],
                [5,6,7]])

print("Shape: ", arr.shape)
print("Dimension: ", arr.ndim)
print("Size: ",arr.size)
print("DType: ", arr.dtype)

# Array Reshaping

arr = np.arange(12) # 1d
print("Original Array: ",arr)

reshape = arr.reshape((3,4)) # to chage into dimention
print("Reshaped arr: ", reshape)

flatten = reshape.flatten()
print("Flatten array: ",flatten) # to change in flat list

raveled = reshape.ravel() #return view insted of copy  
print("Raveled array: ",raveled )

# Transpose ------------------

transpose = reshape.T
print(transpose)

# Numpy Arry Operation ----------------

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print("Basic Slicing: ",arr[2:7]) #basic slicing using index
print("With Step: ", arr[2:6:2]) # skip the steps
print("Negative Slicing: ", arr[-3]) # Negative slicing from back


arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Specific Element: ", arr_2d[1,2])
print("Entire row: ", arr_2d[1]) # target row
print("Entire Column: ", arr_2d[:,2]) #target column


#Storting ---------------------------

unsorted = np.array([3,1,5,1,9,10,7])
print("Sorted Array: ", np.sort(unsorted))

arr_2d_unsorted = np.array([[1,5,3],[4,10,6],[7,1,9]])
print("Sorted 2d array by column", np.sort(arr_2d_unsorted, axis=0))
print("Sorted 2d array by row", np.sort(arr_2d_unsorted, axis=1))

#Filtering ------------------

numbers = np.array([1,2,3,4,5,6,7,8,9,10])
even = numbers[numbers % 2 == 0]
print("Even no.= ",even)

# Filter with mask ---------------

mask = numbers > 5
print("number greater than 5: ", numbers[mask])

#Fancy indexing vs np.where()

numbers = np.array([1,2,3,4,5,6,7,8])
indices = [0,2,3]
print("number: ", numbers[indices])

where_result = np.where(numbers > 5)
print(where_result)
print("NP Where: ", numbers[where_result])

condition_array = np.where(numbers > 5, numbers *2 , numbers)
print(condition_array)

#Adding and removing data -------------

arr1= np.array([1,2,3])
arr2 = np.array([4,5,6])

combined = np.concatenate((arr1,arr2))
print(combined)

#array compatibility -------------
a= np.array([1,2,3])
b= np.array([4,5,6])
c= np.array([7,8,9])

print("Compaibility Shape", a.shape == b.shape)

original = np.array([[1,2],[2,4]])
new_row = np.array([[5,6]])

with_new_row = np.vstack((original, new_row))#vstack add data in row wise
print("origanl",original)
print("new",with_new_row)

new_col = np.array([[7],[8]])
with_new_col = np.hstack((original,new_col)) # hstack add data in colom wise
print("origanl",original)
print("new",with_new_col)

#delete array data ----

arr1 = np.array([1,2,3,4,5,6])
delete = np.delete(arr1, 2)
print(delete)