from collections import deque
def dfs(graph,start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
    return visited
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex]-visited)
    return visited

g = {}
n = int(input("Enter no.of vertices:"))
for i in range(n):
    vertex = input(f"Enter vertex {i+1}:")
    a_v = input(f"Enter adjacent vertex of {vertex}:").split()
    g[vertex] = set(a_v)
start = input("Enter start vertex:")
dfs = dfs(g,start)
bfs = bfs(g,start)
print("DFS: ",dfs)
print("BFS: ",bfs)
