class EdgeNode:
    def __init__(self, y):
        self.y = y
        self.next = None

class Graph:
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.edges = [None] * num_vertices

    def add_edge(self, x, y):
        edge = EdgeNode(y)
        edge.next = self.edges[x]
        self.edges[x] = edge
        if not self.directed:
            self.add_edge(y, x)

def process_vertex_early(v):
    print("Processing vertex", v, "early")

def process_vertex_late(v):
    print("Processing vertex", v, "late")

def process_edge(x, y):
    print("Processing edge", (x, y))

def dfs(g, v):
    global time, finished
    
    if finished:
        return
    
    discovered[v] = True
    time += 1
    entry_time[v] = time
    process_vertex_early(v)
    
    p = g.edges[v]
    while p is not None:
        y = p.y
        if not discovered[y]:
            parent[y] = v
            process_edge(v, y)
            dfs(g, y)
        elif (not processed[y]) or (g.directed):
            process_edge(v, y)
        
        p = p.next
    
    if finished:
        return
    
    process_vertex_late(v)
    time += 1
    exit_time[v] = time
    processed[v] = True
    
# Example usage
num_vertices = 6
g = Graph(num_vertices)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

discovered = [False] * num_vertices
processed = [False] * num_vertices
parent = [-1] * num_vertices
entry_time = [0] * num_vertices
exit_time = [0] * num_vertices
time = 0
finished = False

dfs(g, 0)



