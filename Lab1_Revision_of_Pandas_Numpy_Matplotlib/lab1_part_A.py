import numpy as np

print("1. Empty and Full NumPy Arrays")
empty_arr = np.empty((3, 3))
full_arr = np.full((3, 3), 7)
print(empty_arr)
print(full_arr)

print("\n2. Array filled with zeros")
zeros_arr = np.zeros((3, 3))
print(zeros_arr)

print("\n3. Array filled with ones")
ones_arr = np.ones((3, 3))
print(ones_arr)

print("\n4. Compare two NumPy arrays")
a = np.array([1, 2, 3])
b = np.array([1, 2, 3])
comparison = np.array_equal(a, b)
print(comparison)

print("\n5. Check if value exists in array")
arr = np.array([1, 2, 3, 4])
result = 3 in arr
print(result)

print("\n6. Flatten a matrix using flatten()")
matrix = np.array([[1, 2], [3, 4]])
flat1 = matrix.flatten()
print(flat1)

print("\n7. Flatten a 2D array using ravel()")
flat2 = matrix.ravel()
print(flat2)

print("\n8. Count non-zero values")
arr = np.array([0, 1, 2, 0, 3])
count = np.count_nonzero(arr)
print(count)

print("\n9. Maximum and Minimum in matrix")
max_val = matrix.max()
min_val = matrix.min()
print("Max:", max_val, "Min:", min_val)

print("\n10. Add and Subtract matrices")
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
add = a + b
sub = a - b
print("Addition:\n", add)
print("Subtraction:\n", sub)

print("\n11. Kronecker product")
kron = np.kron(a, b)
print(kron)

print("\n12. Replace elements not satisfying condition")
arr = np.array([10, 5, 2, 8])
arr[arr < 6] = 0
print(arr)

print("\n13. Replace negative values with zero")
arr = np.array([-1, 2, -3, 4])
arr[arr < 0] = 0
print(arr)

print("\n14. Replace NaN with column mean")
arr = np.array([[1, np.nan], [3, 4]])
col_mean = np.nanmean(arr, axis=0)
inds = np.where(np.isnan(arr))
arr[inds] = np.take(col_mean, inds[1])
print(arr)

print("\n15. Indices of elements equal to zero")
arr = np.array([1, 0, 2, 0, 3])
indices = np.where(arr == 0)
print(indices)

print("\n16. Remove columns with non-numeric values")
arr = np.array([[1, 2], [3, np.nan]])
clean = arr[:, ~np.isnan(arr).any(axis=0)]
print(clean)

print("\n17. Row indices having element greater than X")
arr = np.array([[1, 2], [5, 6]])
rows = np.where(arr > 4)[0]
print(rows)

print("\n18. Random NumPy array")
rand_arr = np.random.rand(3, 3)
print(rand_arr)

print("\n19. Indices of sorted array")
arr = np.array([10, 5, 8])
indices = np.argsort(arr)
print(indices)

print("\n20. k smallest and n largest values")
arr = np.array([7, 2, 10, 4, 9])
k_smallest = np.partition(arr, 2)[:2]
n_largest = np.partition(arr, -2)[-2:]
print("Smallest:", k_smallest)
print("Largest:", n_largest)

print("\n21. Sum of columns in 2D array")
arr = np.array([[1, 2, 3], [4, 5, 6]])
col_sum = arr.sum(axis=0)
print(col_sum)

print("\n22. Average of two arrays")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
avg = (a + b) / 2
print(avg)

print("\n23. Mean of array")
arr = np.array([1, 2, 3, 4])
mean_val = np.mean(arr)
print(mean_val)

print("\n24. Mean of matrix")
mean_matrix = matrix.mean()
print(mean_matrix)

print("\n25. Average, Variance, Standard Deviation")
arr = np.array([1, 2, 3, 4, 5])
average = np.mean(arr)
variance = np.var(arr)
std_dev = np.std(arr)
print("Average:", average)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
