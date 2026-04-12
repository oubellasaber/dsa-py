class Graph:
    def __init__(self, num_vertices, directed=False):
        self.n = num_vertices
        self.directed = directed
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, weight=1):
        """Add an edge from u to v. Weight defaults to 1 (unweighted)."""
        self.adj_matrix[u][v] = weight
        if not self.directed:
            self.adj_matrix[v][u] = weight

    def remove_edge(self, u, v):
        """Remove edge from u to v."""
        self.adj_matrix[u][v] = 0
        if not self.directed:
            self.adj_matrix[v][u] = 0

    def has_edge(self, u, v):
        """Check if there is an edge from u to v."""
        return self.adj_matrix[u][v] != 0

    def print_matrix(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)

# Example usage:
g = Graph(4, directed=True)  # Create a directed graph with 4 vertices
g.add_edge(0, 1, 3)  # Edge A->B with weight 3
g.add_edge(0, 2, 5)  # Edge A->C with weight 5
g.add_edge(1, 3, 2)  # Edge B->D with weight 2
g.add_edge(2, 3, 7)  # Edge C->D with weight 7

g.print_matrix()