accounts = [[1, 2, 3], [3, 2, 1]]
maxi = 0
for customer in accounts:
    curr = 0
    for money in customer:
        curr += money
        maxi = max(curr, maxi)
print(maxi)
