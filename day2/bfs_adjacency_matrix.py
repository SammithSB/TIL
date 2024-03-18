def bfs(graph, start):
    # create graph
    G = []
    # enqueue the start and mark it as visited
    G.append(start)
    visited = [False]*len(graph)
    visited[start] = True
    
    while G:
        # remove the first vertex and print it
        removed_vertext = G.pop(0)
        print(f"Current vertex {removed_vertext}")

        # get all neighbours of the removex vertex and if not visited
        # add them to queue and mark as visited
        for i in range(len(graph[removed_vertext])):
            if graph[removed_vertext][i] == 1 and not visited[i]:
                G.append(i)
                visited[i] = True

# Example graph represented as an adjacency matrix
graph = [
    [0, 1, 1, 0, 0, 0],  # A
    [1, 0, 0, 1, 1, 0],  # B
    [1, 0, 0, 0, 0, 1],  # C
    [0, 1, 0, 0, 0, 0],  # D
    [0, 1, 0, 0, 0, 1],  # E
    [0, 0, 1, 0, 1, 0]   # F
]

# Perform BFS starting from vertex 0 (A)
bfs(graph, 0)