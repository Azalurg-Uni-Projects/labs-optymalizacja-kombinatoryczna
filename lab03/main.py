n = 6   # liczba wierzchołków
m = 8   # liczba krawędzi    
v = 5   # wierzchołek startowy
visited = [v] # odwiedzone 
A = {
    0: [1, 2, 3, 5],
    1: [0, 2],
    2: [0, 1, 3],
    3: [0, 2, 5],
    4: [5],
    5: [0, 3, 4]
}  

current = [v]
helper = []
while len(current) > 0:
    c = current[-1]
    counter = 0
    for g in A[c]:
        if not g in visited:
            visited.append(g)
            current.append(g)
            helper.append((c, g))
            break
        counter += 1
    if counter == len(A[c]):
        current.pop()

print(helper)

