def superDigit(n, k):
    n = sum([int(n[i]) for i in range(len(n))]) * k
    return superDigit(str(n), 1) if n > 9 else n

if __name__ == '__main__':
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = superDigit(n, k)
    print(str(result))
