# Karatsuba multiplication algorithm
# Path: lab07\main.py
import time
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
    x = 123456789 ** 200
    y = 987654321 ** 200

    start1 = time.time()
    result1 = karatsuba(x, y)
    end1 = time.time()

    start2 = time.time()
    result2 = x * y
    end2 = time.time()

    print("Karatsuba: ", end1 - start1)
    print("Standard: ", end2 - start2)
    print(result1 == result2)


if __name__ == "__main__":
    main()
