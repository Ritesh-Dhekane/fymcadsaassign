print("Name= Ritesh Dhekane")

arr = [10, 20, 10, 30, 20, 10]
freq = {}
for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
print("Frequencies:", freq)
