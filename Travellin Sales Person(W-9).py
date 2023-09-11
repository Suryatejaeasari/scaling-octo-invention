import itertools
import sys

def tsp(graph, start):
    num = len(graph)
    all_nodes = set(range(num))

    min_dist = sys.maxsize
    short_path = []
    for permutation in itertools.permutations(all_nodes):
        if permutation[0] == start:
            current_dist = sum(graph[permutation[i]][permutation[((i+1)%num)]] for i in range(num))

        if current_dist < min_dist:
            min_dist = current_dist
            short_path = list(permutation)
    return short_path, min_dist
graph = [
    [0, 10, 15, 20],
    [5, 0, 9, 10],
    [6, 13, 0, 12],
    [8, 8, 9, 0]
]
start = 0
short,mi = tsp(graph,start)

print("Shortest Path:")
print("->".join(str(node) for node in short+[start]))
print("Shortest Distance:", mi)
