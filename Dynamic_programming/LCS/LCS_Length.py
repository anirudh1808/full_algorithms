

def LCS(X, Y, m, n):
    t = [[0]*(n + 1) for i in range(m + 1)]
    print(t)
    for i in range(1,m + 1):
        for j in range(1,n + 1):
            if X[i - 1] == Y[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i][j - 1], t[i - 1][j])
    return t


def print_LCS(X, Y, m, n):
    t=LCS(X, Y, m, n)
    print(t)
    print(t[m][n])
    i, j = m, n
    s1 = ""
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            s1 = X[i - 1] + s1
            i = i - 1
            j = j - 1
        else:
            if t[i][j - 1] > t[i - 1][j]:
                j = j - 1
            else:
                i = i - 1
    print(s1)


print_LCS("abcde", "abfce", 5, 5)

