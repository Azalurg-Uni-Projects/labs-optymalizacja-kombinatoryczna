import time


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


# def eeee(graph, start, end):
#     path = []
#     if start == end:
#         return path
#     visited = []
#     path = [start]
#
#     while path[-1] != end:
#         print(path)
#         time.sleep(2)
#
#         current = path[-1]
#         next_nodes = graph[current]
#         lowest = next_nodes[0]
#         index = 0
#         for i in range(len(next_nodes)):
#             next_node = next_nodes[i]
#             if index not in visited and next_node != 0 and lowest == 0:
#                 lowest = next_node
#                 index = i
#             if index not in visited and next_node != 0 and next_node < lowest:
#                 lowest = next_node
#                 index = i
#
#         if lowest == 0:
#             path.pop()
#         else:
#             path.append(index)
#             visited.append(index)
#
#     return path


# def find_shortest(graph, odd):
#     shortest = []
#     for i in range(len(odd)):
#         for j in range(len(odd)):
#             if i != j:
#                 shortest.append(find_shortest_path(graph, odd[i], odd[j]))
#     return shortest


edges = [(0, 1, 3), (0, 5, 4),
         (1, 2, 5), (1, 5, 8),
         (2, 3, 5), (2, 4, 10),
         (2, 5, 14), (3, 4, 9),
         (4, 5, 6)]

start = "b"
vertices = 6


def main():
    graph = make_matrix(edges, vertices)
    print(graph)
    degrees = get_degree(graph, vertices)
    print(degrees)
    odd = find_odd(degrees)
    print(odd)
    print(find_shortest_path(graph, 1, 4))
    # shortest = find_shortest(graph, odd)
    # print(shortest)
    # path = find_eulerian_path(graph, shortest[0])
    # print_path(path)
    # print_length(path, graph)


main()
