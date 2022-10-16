def print_line(n):
    print("")
    for i in range(n):
        if i % 4 == 0:
            print("|", end="")
        else:
            print("-", end="")
    print("")


def print_matrix(vertices_amount: int, vertices: list[tuple]):
    print("| X", end=" | ")
    for i in range(vertices_amount):
        print(i, end=" | ")

    for i in range(vertices_amount):
        print_line(4 * vertices_amount + 5)
        print(f"| {i}", end=" | ")
        for u in range(vertices_amount):
            k = True
            for j in range(len(vertices)):
                if vertices[j][1] == u and vertices[j][0] == i:
                    print(1, end=" | ")
                    k = False
                    break
            if k:
                print(0, end=" | ")
    print("\n")


def swap(vertices: list[tuple], edge, isDirect):
    if edge in vertices:
        vertices.remove(edge)
        if not isDirect:
            vertices.remove((edge[1], edge[0]))
    else:
        vertices.append(edge)
        if not isDirect:
            vertices.append((edge[1], edge[0]))
    return vertices


def print_degree(vertices_amount: int, vertices: list[tuple]):
    degrees = {}
    for x in range(vertices_amount):
        degrees[x] = 0

    for v in vertices:
        degrees[v[0]] += 1

    print(degrees, "\n")


def main():
    isDirect = input("Is graph direct? (y/N) ")

    if isDirect in ["y", "Y"]:
        isDirect = True
    else:
        isDirect = False

    vertices_amount = int(input("Vertices amount: "))
    edges_amount = int(input("Edges amount: "))

    print(f"Enter vertex numbers separated by a space. Range 0-{vertices_amount - 1}")

    vertices: list[tuple] = []
    for i in range(edges_amount):
        v = str(input(f"{i + 1}. ")).split(" ")
        vertices.append((int(v[0]), int(v[1])))
        if not isDirect:
            vertices.append((int(v[1]), int(v[0])))
        vertices = list(set(vertices))

    while True:
        print(" 1. Print matrix \n 2. Add/remove edge \n 3. Print degree \n 0. Exit")
        signal = int(input("Chose (0-3): "))
        if signal == 1:
            print_matrix(vertices_amount, vertices)
        if signal == 2:
            v = str(input("1. ")).split(" ")
            vertices = swap(vertices, [int(v[0]), int(v[1])], isDirect)
        if signal == 3:
            print_degree(vertices_amount, vertices)
        if signal == 0:
            break


main()
