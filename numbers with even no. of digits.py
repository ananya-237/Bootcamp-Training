nums = [555,901,482,1771]
count = 0
for num in nums:
    if len(str(num)) % 2 == 0:
        count += 1
print(count)
        