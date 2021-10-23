def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    m = 0
 
    while l <= r:
 
        m = (r + l) // 2
        
        if arr[m] < x:
            l = m + 1
 
        elif arr[m] > x:
            r = m - 1
            
        else:
            return m
    return -1

arr = [ 1, 4, 7, 11, 46 ]
x = 1

result = binary_search(arr, x)
print("Pos>",str(result))

