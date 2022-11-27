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


edges = [(0, 1, 3), (0, 5, 4),
         (1, 2, 5), (1, 5, 8),
         (2, 3, 5), (2, 4, 10),
         (2, 5, 14), (3, 4, 9),
         (4, 5, 6)]

vertices = 6
graph = make_matrix(edges, vertices)
start = 1
end = 4

'''find eular path'''