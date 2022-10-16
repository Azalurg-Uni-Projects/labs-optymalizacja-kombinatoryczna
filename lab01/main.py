def print_line(n):
    print("")
    for i in range(n):
        if i % 4 == 0:
            print("|", end="")
        else:
            print("-", end="")
    print("")


def print_matrix(v_a, v):
    print("| X", end=" | ")
    for i in range(v_a):
        print(i, end=" | ")

    for i in range(v_a):
        print_line(4*v_a + 5)
        print(f"| {i}", end=" | ")
        for u in range(v_a):
            k = True
            for j in range(len(v)):
                if v[j][1] == u and v[j][0] == i:
                    print(1, end=" | ")
                    k = False
                    break
            if k:
                print(0, end=" | ")


def main():
    isDirect = input("Is graph direct? (y/N) ")

    if isDirect in ["y", "Y"]:
        isDirect = True
    else:
        isDirect = False

    vertices_amount = int(input("Vertices amount: "))
    edges_amount = int(input("Edges amount: "))

    print(f"Enter vertex numbers separated by a space. Range 0-{vertices_amount - 1}")

    vertices = []
    for i in range(edges_amount):
        v = str(input(f"{i + 1}. ")).split(" ")
        vertices.append([int(v[0]), int(v[1])])
        if not isDirect:
            vertices.append([int(v[1]), int(v[0])])

    print_matrix(vertices_amount, vertices)


main()
