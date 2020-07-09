if __name__ == "__main__":
    n = int(input())
    s = float(1)
    for _ in range(n):
        s = s * 2 % (1e9 + 7)
    print(int(s))
