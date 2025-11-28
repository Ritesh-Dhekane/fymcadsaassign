print("Name= Ritesh Dhekane")

rows = 2
cols = 3
matrix = [[0]*cols for _ in range(rows)]

count = 1
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = count
        count += 1

for row in matrix:
    print(row)
