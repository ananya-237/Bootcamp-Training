arr = [1, 3, 6, 10]
for i in range(1, len(arr)):
    arr[i] = arr[i] + arr[i-1]
print(arr)
