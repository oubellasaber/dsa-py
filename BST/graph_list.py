class Graph:
    def __init__(self, num_vertices, directed=False):
        self.n = num_vertices
        self.directed = directed
        self.adj_list = [[] for _ in range(num_vertices)]  # list of lists

    def add_edge(self, u, v, weight=1):
        """Add an edge from u to v. Weight defaults to 1."""
        self.adj_list[u].append((v, weight))
        if not self.directed:
            self.adj_list[v].append((u, weight))

    def remove_edge(self, u, v):
        """Remove edge from u to v."""
        self.adj_list[u] = [pair for pair in self.adj_list[u] if pair[0] != v]
        if not self.directed:
            self.adj_list[v] = [pair for pair in self.adj_list[v] if pair[0] != u]

    def has_edge(self, u, v):
        """Check if there is an edge from u to v."""
        return any(pair[0] == v for pair in self.adj_list[u])

    def print_graph(self):
        print("Adjacency List:")
        for i, neighbors in enumerate(self.adj_list):
            print(f"{i} -> {neighbors}")

# Example usage:
g = Graph(4, directed=True)  # Directed graph with 4 vertices
g.add_edge(0, 1, 3)  # A->B weight 3
g.add_edge(0, 2, 5)  # A->C weight 5
g.add_edge(1, 3, 2)  # B->D weight 2
g.add_edge(2, 3, 7)  # C->D weight 7

g.print_graph()