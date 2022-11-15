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

graph.sort(key=lambda x: x["weight"])  # sortowanie

cycle_check = set()
choosen_edges = []
weight_sum = 0

while True:
    try:
        edge = graph.pop(0)
    except:
        print("I can't find a tree")
        exit(0)

    if not edge["edge"][0] in cycle_check or not edge["edge"][1] in cycle_check:
        cycle_check.add(edge["edge"][1])
        choosen_edges.append(edge["edge"])
        weight_sum += edge["weight"]

    if len(choosen_edges) == edges - 1:
        break

print(choosen_edges)
print(weight_sum)
