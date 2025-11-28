# Q20. Write a program to find in-degree and out-degree of all vertices.

print("Name= Ritesh Dhekane")

# Graph class using adjacency list
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in vertices}

    # Add directed edge u -> v
    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    # Calculate in-degree and out-degree
    def degrees(self):
        in_degree = {v: 0 for v in self.vertices}
        out_degree = {v: len(self.adj_list[v]) for v in self.vertices}

        for u in self.vertices:
            for v in self.adj_list[u]:
                in_degree[v] += 1

        print("Vertex\tIn-Degree\tOut-Degree")
        for v in self.vertices:
            print(f"{v}\t{in_degree[v]}\t\t{out_degree[v]}")

# Example usage
vertices = ['A', 'B', 'C', 'D']
g = Graph(vertices)
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('C', 'D')

g.degrees()
