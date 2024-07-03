def bfs(graph, start):
    # create a queue
    queue = []
    # enqueue it with start index and mark it as visited
    queue.append(start)
    visited = {start}
    while queue:
        # dequeue the vertex
        removed_vertext = queue.pop(0)
        print(f"Current vertext {removed_vertext}")

        # get all neighbours of dequeued vertex and if not visited
        # add it too the queue and mark it as visited
        for neighbour in graph[removed_vertext]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Perform BFS starting from vertex 'A'
bfs(graph, 'A')
