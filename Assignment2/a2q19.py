# Q19. Given an undirected graph with V vertices and E edges, 
# Write a program to check whether it contains any cycle or not.

print("Name= Ritesh Dhekane")

# Graph class using adjacency list
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in vertices}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # Undirected graph

    # DFS utility to detect cycle
    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True
        for neighbor in self.adj_list[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, v):
                    return True
            elif parent != neighbor:
                return True
        return False

    # Function to check cycle
    def is_cyclic(self):
        visited = {v: False for v in self.vertices}
        for v in self.vertices:
            if not visited[v]:
                if self.is_cyclic_util(v, visited, None):
                    return True
        return False

# Example usage
vertices = ['A', 'B', 'C', 'D']
g = Graph(vertices)
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('D', 'A')  # Adding this edge creates a cycle

if g.is_cyclic():
    print("The graph contains a cycle.")
else:
    print("The graph does not contain any cycle.")
