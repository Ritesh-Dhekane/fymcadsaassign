print("Name= Ritesh Dhekane")

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
rows = len(A)
cols = len(B[0])
C = [[0]*cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(row)
