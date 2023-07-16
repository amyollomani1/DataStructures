from collections import deque

def BFS(graph, source):
    # Initialize state and parent dictionaries
    state = {}
    parent = {}
    for vertex in graph:
        state[vertex] = "undiscovered"
        parent[vertex] = None

    # Set the state and parent of the source vertex
    state[source] = "discovered"
    parent[source] = None

    # Create a queue and enqueue the source vertex
    queue = deque()
    queue.append(source)

    # Perform BFS
    while queue:
        u = queue.popleft()  # Dequeue a vertex from the queue

        # Process vertex u as desired
        print("Processing vertex:", u)

        # Traverse all adjacent vertices of u
        for v in graph[u]:
            # Process edge (u, v) as desired
            print("Processing edge:", (u, v))

            if state[v] == "undiscovered":
                state[v] = "discovered"  # Mark vertex v as discovered
                parent[v] = u  # Set u as the parent of v
                queue.append(v)  # Enqueue vertex v for exploration

        state[u] = "processed"  # Mark vertex u as processed

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C', 'F'],
    'F': ['E']
}

BFS(graph, 'A')