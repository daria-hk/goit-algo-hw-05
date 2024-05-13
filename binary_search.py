def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iter = 0
    upper_border = None
 
    while low <= high:
        iter += 1
 
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1
 
        elif arr[mid] >= x:
            high = mid - 1
            upper_border = arr[mid]
 
        else:
            upper_bound = arr[mid]
            return iter, upper_bound
 
    return  iter, upper_border

arr = [2.2, 3.4, 4.4, 10.1, 40.0]
x = 40
iter, upper_border = binary_search(arr, x)
if x > arr[-1]:
  print(f"Amount of iterations: {iter}, upper border: {arr[-1]} ")
else:
  print(f"Amount of iterations: {iter}, max element: {upper_border} ")

