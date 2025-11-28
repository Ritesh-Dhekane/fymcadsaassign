# Q17. Write a program to implement Graph using adjacency matrix.

print("Name= Ritesh Dhekane")

# Graph class using adjacency matrix
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.num_vertices = len(vertices)
        # Initialize adjacency matrix with 0s
        self.adj_matrix = [[0 for _ in range(self.num_vertices)] for _ in range(self.num_vertices)]
        # Map vertex names to indices
        self.vertex_index = {vertex: idx for idx, vertex in enumerate(vertices)}

    # Add edge (directed)
    def add_edge(self, u, v):
        i = self.vertex_index[u]
        j = self.vertex_index[v]
        self.adj_matrix[i][j] = 1  # 1 indicates an edge exists

    # Display adjacency matrix
    def display(self):
        print("Adjacency Matrix:")
        print("  ", " ".join(self.vertices))
        for i, row in enumerate(self.adj_matrix):
            print(self.vertices[i], " ".join(map(str, row)))

# Example usage
vertices = ['A', 'B', 'C', 'D']
g = Graph(vertices)

# Adding edges
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('D', 'A')

g.display()
