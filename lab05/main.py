# https://inf.ug.edu.pl/~hanna/grafy/w2_CPP.pdf

def make_matrix(edges, vertices):
    matrix = []
    for i in range(vertices):
        matrix.append([])
        for j in range(vertices):
            matrix[i].append(0)

    for i in range(len(edges)):
        matrix[edges[i][0]][edges[i][1]] = edges[i][2]
        matrix[edges[i][1]][edges[i][0]] = edges[i][2]
    return matrix


def get_degree(matrix, vertices):
    degrees = []
    for i in range(vertices):
        degree = 0
        for j in range(vertices):
            if matrix[i][j] != 0:
                degree += 1
        degrees.append(degree)
    return degrees


def find_odd(degrees):
    odd = []
    for i in range(len(degrees)):
        if degrees[i] % 2 != 0:
            odd.append(i)
    return odd


def bfs(graph, start, end):
    if start == end:
        return 0, []
    queue: list[list[int]] = [[start]]
    stop = False
    while not stop and queue:
        stop = True
        for path in queue:
            if path[-1] != end:
                stop = False
        if stop:
            break
        new_queue = []
        for path in queue:
            nodes = graph[path[-1]]
            if end in path:
                new_queue.append(path)
            else:
                for i in range(len(nodes)):
                    if nodes[i] != 0 and i not in path:
                        path_copy = path.copy()
                        path_copy.append(i)
                        new_queue.append(path_copy.copy())
        queue = new_queue
    weights = []
    for path in queue:
        weight = 0
        for i in range(len(path) - 1):
            weight += graph[path[i]][path[i + 1]]
        weights.append(weight)

    min_weight = min(weights)
    min_index = weights.index(min_weight)
    return min_weight, queue[min_index]


def gen_pairs(odds):
    pairs = []
    for i in range(len(odds) - 1):
        for j in range(i + 1, len(odds)):
            pairs.append([odds[i], odds[j]])
    return pairs


def gen_edges_to_add(pairs, graph, odds: list[int]):
    pairs = pairs.copy()
    odds = odds.copy()
    weights = []
    paths = []

    for pair in pairs:
        weight, path = bfs(graph, pair[0], pair[1])
        weights.append(weight)
        paths.append(path)

    edges_to_add = []

    while len(odds) != 0:
        min_weight = min(weights)
        min_index = weights.index(min_weight)
        path = paths[min_index]
        for i in range(len(path) - 1):
            edges_to_add.append((min(path[i], path[i + 1]), max(path[i], path[i + 1]), graph[path[i]][path[i + 1]]))

        odds.remove(pairs[min_index][0])
        odds.remove(pairs[min_index][1])
        weights.remove(min_weight)
        paths.remove(path)
        pairs.remove(pairs[min_index])
    return edges_to_add


def find_min_euler_cycle(edges, start):
    stack = []
    ce = []
    stack.append(start)
    ce.append(start)
    while stack:
        v = stack[-1]
        for i in range(len(edges)):
            if edges[i][0] == v:
                stack.append(edges[i][1])
                ce.append(edges[i][1])
                edges.pop(i)
                break
            elif edges[i][1] == v:
                stack.append(edges[i][0])
                ce.append(edges[i][0])
                edges.pop(i)
                break
        if stack[-1] == v:
            stack.pop()
    return ce


edges = [(0, 1, 3), (0, 5, 4),
         (1, 2, 5), (1, 5, 8),
         (2, 3, 5), (2, 4, 10),
         (2, 5, 14), (3, 4, 9),
         (4, 5, 6)]

# edges = [(0, 1, 2), (0, 7, 1), (1, 2, 2), (1, 8, 2), (2, 3, 3), (3, 4, 4), (3, 8, 3), (3, 9, 1),
#          (4, 5, 3), (4, 9, 2), (5, 6, 5), (5, 9, 2), (6, 7, 1), (6, 8, 2), (6, 9, 4), (7, 8, 4)]

start = 1
vertices = 10


def main():
    graph = make_matrix(edges, vertices)
    degrees = get_degree(graph, vertices)
    odds = find_odd(degrees)
    pairs = gen_pairs(odds)
    edges_to_add = gen_edges_to_add(pairs, graph, odds)
    for x in edges_to_add:
        edges.append(x)
    print(find_min_euler_cycle(edges, start))


main()
