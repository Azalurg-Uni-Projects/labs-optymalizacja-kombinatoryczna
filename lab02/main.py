def multiply(ma, mb):
    result = [[sum(a * b for a, b in zip(A_row, B_col))
               for B_col in zip(*mb)]
              for A_row in ma]
    return result


m1 = [[0, 1, 1, 0, 1],
      [1, 0, 1, 0, 0],
      [1, 1, 0, 1, 0],
      [0, 0, 1, 0, 1],
      [1, 0, 0, 1, 0]]

m2 = multiply(m1, m1)
m3 = multiply(m1, m2)


sum = 0
for i in range(len(m3)):
    sum += m3[i][i]

print(f"b)\n {sum / 6 >= 1}\n")


def find(o, r, s):
    if s == 2 and m1[r][o] == 1 and r != o:
        print("\n"+str(r), end=" ")
        return True
    if s != 2:
        for c in range(len(m1)):
            if m1[r][c] == 1:
                if find(o, c, s+1):
                    print(r, end=" ")
                    return True
    return False


print("c)", end="")

isThereC3 = False
for i in range(5):
    if find(i, i, 0):
        isThereC3 = True

print(f"\n\na)\n {isThereC3}")
