# Q16. Write a program to perform following graph traversal operations: 
# a. DFS graph traversal
# b. BFS graph traversal

print("Name= Ritesh Dhekane")

# Graph class using adjacency list
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {vertex: [] for vertex in vertices}

    def add_edge(self, u, v):
        if u in self.adj_list:
            self.adj_list[u].append(v)
        else:
            self.adj_list[u] = [v]

    def display(self):
        print("Graph adjacency list:")
        for vertex in self.adj_list:
            print(f"{vertex} -> {', '.join(map(str, self.adj_list[vertex]))}")

    # DFS traversal
    def dfs_util(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")
        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start_vertex):
        visited = {v: False for v in self.vertices}
        print("DFS Traversal starting from", start_vertex, ":", end=" ")
        self.dfs_util(start_vertex, visited)
        print()

    # BFS traversal
    def bfs(self, start_vertex):
        visited = {v: False for v in self.vertices}
        queue = []
        visited[start_vertex] = True
        queue.append(start_vertex)
        print("BFS Traversal starting from", start_vertex, ":", end=" ")
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")
            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        print()

# Example usage
vertices = ['A', 'B', 'C', 'D']
g = Graph(vertices)
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('D', 'A')

g.display()
g.dfs('A')
g.bfs('A')
