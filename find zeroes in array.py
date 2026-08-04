#count the no. of zeroes in a sorted array
 
a = [1,0,1,2,0,3,4]
count = 0
n = len(a)
for i in range(n):
    if a[i] == 0:
        count += 1
print(count)
