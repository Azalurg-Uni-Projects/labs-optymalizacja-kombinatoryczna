# Karatsuba multiplication algorithm
# Path: lab07\main.py

def karatsuba(x: int, y: int):
    if x.bit_length() <= 64 or y.bit_length() < 64:
        return x * y

    n = max(x.bit_length(), y.bit_length())
    m = n // 2

    a = x >> m
    b = x - (a << m)
    c = y >> m
    d = y - (c << m)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    return ac * (1 << (2 * m)) + (ad_bc * (1 << m)) + bd


def main():
    x = 123456789 ** 20
    y = 987654321 ** 20

    print(karatsuba(x, y) == x * y)


if __name__ == "__main__":
    main()
