# Q15. Write a program to implement Graph using adjacency list.

print("Name= Ritesh Dhekane")

# Graph class using adjacency list
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {}  # Dictionary to store adjacency list
        for vertex in vertices:
            self.adj_list[vertex] = []

    # Add edge (directed)
    def add_edge(self, u, v):
        if u in self.adj_list:
            self.adj_list[u].append(v)
        else:
            self.adj_list[u] = [v]

    # Display adjacency list
    def display(self):
        print("Graph adjacency list:")
        for vertex in self.adj_list:
            print(f"{vertex} -> {', '.join(map(str, self.adj_list[vertex]))}")

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
