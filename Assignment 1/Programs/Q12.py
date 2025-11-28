print("Name= Ritesh Dhekane")

arr = [10, 20, 5, 30, 15]
max_val = arr[0]
min_val = arr[0]

for x in arr:
    if x > max_val:
        max_val = x
    if x < min_val:
        min_val = x

print("Maximum element:", max_val)
print("Minimum element:", min_val)
