print("Name= Ritesh Dhekane")

arr = [10, 20, 30, 40, 50]
print("Original Array:", arr)

element = 30
pos = -1

for i in range(len(arr)):
    if arr[i] == element:
        pos = i
        break

if pos != -1:
    for i in range(pos, len(arr)-1):
        arr[i] = arr[i+1]
    arr = arr[:-1]
    print("Array after deletion:", arr)
else:
    print("Element not found")
