def solution(n):
    """
    given a int n
    divided the number 1, 2,..., n
    print two sets of equal sum. 
    123 -> 12, 3
    1234 -> 14, 23
    12 -> NO
    12345 -> NO
    123456 -> NO
    1234567 -> YES, 1247 356
    """

    nums = range(n+1)
    s = sum(nums)
    set1 = []
    set2 = []
    if s % 2 != 0:
        print("NO")
        return None

    if n % 4 == 3:
        j = 3
        set1.append(1)
        set1.append(2)
        set2.append(3)
    if n % 4 == 0:
        j = 4
        set1.append(1)
        set1.append(4)
        set2.append(2)
        set2.append(3)

    for num in range(j+1, n+1):
        piv = (num - j) % 4
        if piv == 1:
            set1.append(num)
        elif piv == 2:
            set2.append(num)
        elif piv == 3:
            set2.append(num)
        elif piv == 0:
            set1.append(num)
    print("YES")
    print(len(set1))
    print(" ".join(map(str, set1)))
    print(len(set2))
    print(" ".join(map(str, set2)))


if __name__ == "__main__":
    solution(int(input()))
