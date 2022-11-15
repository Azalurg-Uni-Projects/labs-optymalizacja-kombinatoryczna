edges = 5
graph = [
    {"edge": "ab", "weight": 3},
    {"edge": "ae", "weight": 1},
    {"edge": "bc", "weight": 5},
    {"edge": "be", "weight": 4},
    {"edge": "cd", "weight": 2},
    {"edge": "ed", "weight": 7},
    {"edge": "ec", "weight": 6}
]

graph.sort(key=lambda x : x["weight"])
visited = set()
cycle_check = set()
edges_in_tree = []
sum = 0

while True:
    edge = graph.pop(0)
    if not edge["edge"][0] in cycle_check or not edge["edge"][1] in cycle_check:
        cycle_check.add(edge["edge"][1])
        edges_in_tree.append(edge["edge"])
        sum += edge["weight"]
    if len(edges_in_tree) == edges-1:
        break

print(edges_in_tree)
print(sum)

