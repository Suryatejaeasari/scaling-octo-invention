def sp(graph):
    n = len(graph)
    dist = [[float('inf')]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                dist[i][j] = 0
    for nodes,neighbours in graph.items():
        for neighbour, distance in neighbours.items():
            dist[nodes-1][neighbour-1] = distance
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return dist

num = int(input("Enter no.of nodes:"))

graph = {}
for i in range(num):
    graph[i+1] = {}
    while True:
        neighbour, distance = map(int,input(f"Enter a neighbour node and distance for node {i+1}:").split())
        if neighbour == -1 and distance == -1:
            break
        graph[i+1][neighbour] = distance
apsp = sp(graph)
print("Shortest Path:")
for i in apsp:
    print(i)
