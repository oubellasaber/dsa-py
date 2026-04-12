def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    visited.add(start)

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def dfs_recursive(graph, node, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(node)
    order.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, order)

    return order


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            order.append(node)

            # reverse to mimic recursive order
            stack.extend(reversed(graph[node]))

    return order


# =========================
# Tests
# =========================

def run_tests():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("Graph:")
    for k, v in graph.items():
        print(f"{k} -> {v}")

    print("\n=== BFS ===")
    bfs_result = bfs(graph, 'A')
    print("BFS Order:", bfs_result)

    print("\n=== DFS Recursive ===")
    dfs_rec_result = dfs_recursive(graph, 'A')
    print("DFS Recursive Order:", dfs_rec_result)

    print("\n=== DFS Iterative ===")
    dfs_it_result = dfs_iterative(graph, 'A')
    print("DFS Iterative Order:", dfs_it_result)

    # Basic correctness checks
    assert bfs_result == ['A', 'B', 'C', 'D', 'E', 'F']
    assert dfs_rec_result == ['A', 'B', 'D', 'E', 'F', 'C']
    assert dfs_it_result == ['A', 'B', 'D', 'E', 'F', 'C']

    print("\n✅ All tests passed!")


# =========================
# Entry Point
# =========================

if __name__ == "__main__":
    run_tests()