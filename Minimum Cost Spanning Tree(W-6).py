import networkx as nx
from collections import defaultdict

def krushkal(graph):
    mst_edge = []
    rank = defaultdict(int)
    parent = {}

    def findparent(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = findparent(parent[vertex])
        return parent[vertex]
    def union(u,v):
        if rank[u] < rank[v]:
            parent[u] = v
        elif rank[u] > rank[v]:
            parent[v] = u
        else:
            parent[v] = u
            rank[u] +=1

    edges = [(u,v,weights) for u, neighbour in graph.items() for v, weights in neighbour]
    edges = sorted(edges, key=lambda x:x[2])

    for edge in edges:
        u,v,weights = edge
        if u not in parent:
            parent[u] = u
        if v not in parent:
            parent[v] = v
        parent_u = findparent(u)
        parent_v = findparent(v)
        if parent_u != parent_v:
            mst_edge.append(edge)
            union(parent_u, parent_v)
    mst_graph = nx.Graph()
    mst_graph.add_weighted_edges_from(mst_edge)
    return mst_graph

n = int(input("No.of vertices:"))
graph = defaultdict(list)
for _ in range(n):
    v = input("Enter name of vertes:")
    m = int(input(f"Enter no.of neighbours of vertex {v}:"))
    for _ in range(m):
        n_w = input("Enter name and weight of neighbour:")
        nei,w = n_w.split()
        graph[v].append((nei,int(w)))
mst = krushkal(graph)
print("Minimum Cost Spanning Tree:")
for edge in mst.edges(data=True):
    print(f"Edge: {edge[0]} - {edge[1]} Cost: {edge[2]['weight']}")
print(f"Minimum Cost: {sum(edge[2]['weight'] for edge in mst.edges(data=True))}")

    
                        
