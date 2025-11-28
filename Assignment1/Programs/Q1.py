print("Name= Ritesh Dhekane")

arr = [10, 20, 30, 40, 50]

print("Original Array:", arr)

element = 25
position = 2  

arr.append(0)
for i in range(len(arr)-1, position, -1):
    arr[i] = arr[i-1]

arr[position] = element

print("Array after insertion:", arr)
