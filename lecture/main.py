graph = [
    [0, 16, 13, 0, 0, 0],   # s
    [0, 0, 10, 12, 0, 0],   # 1
    [0, 4, 0, 0, 14, 0],    # 2
    [0, 0, 9, 0, 0, 20],    # 3
    [0, 0, 0, 7, 0, 4],     # 4
    [0, 0, 0, 0, 0, 0]      # t
]

v = 6
source = 0
target = 5
fifo = [0]
routes = []
routes_sum = 0

while True:
    wmi = fifo.pop(0)
    for x in range(v):
        if graph[wmi][x] > 0:
            fifo.append(x)
            routes.append((wmi, x, graph[wmi][x]))

    if not fifo:
        break

    if target in fifo:
        wmi = 5
        for x in range(len(routes)-1, -1, -1):
            if routes[x][1] == wmi:
                wmi = routes[x][0]
            else:
                routes.pop(x)
        routes.sort(key=lambda x: x[2])
        choosen_route = routes[0]
        routes_sum += choosen_route[2]
        for x in routes:
            graph[x[0]][x[1]] -= choosen_route[2]
        fifo = [0]
        routes = []
        ala = 0
        for x in graph:
            for y in x:
                if y != 0:
                    ala += 1
        if ala == v:
            break

print(routes_sum)
