def find_cycle(edge, choosen_edges):
    start = edge[0]
    go_to = edge[1]
    old_goto = ""
    to_return = True
    while True:
        for x in choosen_edges:
            old_goto = go_to
            if go_to == x[1]:
                go_to = x[0]
                choosen_edges.remove(x)
                break
            if go_to == x[0]:
                go_to = x[1]
                choosen_edges.remove(x)
                break
        if old_goto == go_to:
            break
        if go_to == start:
            to_return = False
            break
        if len(choosen_edges) < 2:
            break
    return to_return


graph = [
    {"edge": "ab", "weight": 7},
    {"edge": "ad", "weight": 5},
    {"edge": "bc", "weight": 8},
    {"edge": "bd", "weight": 9},
    {"edge": "be", "weight": 7},
    {"edge": "ce", "weight": 5},
    {"edge": "de", "weight": 15},
    {"edge": "df", "weight": 6},
    {"edge": "ef", "weight": 8},
    {"edge": "eg", "weight": 9},
    {"edge": "fg", "weight": 11}
]

graph.sort(key=lambda x: x["weight"])  # sortowanie

cycle_check = set()
choosen_edges = []
weight_sum = 0
points = 7

while True:
    try:
        edge = graph.pop(0)
    except:
        print("I can't find a tree")
        exit(0)

    if find_cycle(edge["edge"], choosen_edges.copy()):
        cycle_check.add(edge["edge"][1])
        choosen_edges.append(edge["edge"])
        weight_sum += edge["weight"]
        print(edge["weight"])

    if len(choosen_edges) == points - 1:
        break

print(choosen_edges)
print(weight_sum)
