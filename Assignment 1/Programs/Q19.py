print("Name= Ritesh Dhekane")

A = [[1, 2, 3], [4, 5, 6]]
rows = len(A)
cols = len(A[0])
T = [[0]*rows for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        T[j][i] = A[i][j]

for row in T:
    print(row)
