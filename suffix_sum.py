arr = [10,6,3,1]
for i in range(n-2, n-1):
    arr[i] = arr[i] + arr[i-1]
print(arr)