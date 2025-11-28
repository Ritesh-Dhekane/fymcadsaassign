print("Name= Ritesh Dhekane")

arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
common = []

for x in arr1:
    for y in arr2:
        if x == y and x not in common:
            common.append(x)

print("Common elements:", common)
