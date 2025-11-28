print("Name= Ritesh Dhekane")

arr = [10, 20, 30, 40, 50]
element = 30
found = -1

for i in range(len(arr)):
    if arr[i] == element:
        found = i
        break

if found != -1:
    print("Element found at index:", found)
else:
    print("Element not found")
