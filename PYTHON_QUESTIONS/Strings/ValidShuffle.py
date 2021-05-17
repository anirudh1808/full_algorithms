# https://www.programiz.com/java-programming/examples/check-valid-shuffle-of-strings

def shufflecheck(s1, s2, result):
    '''for pointers to each string'''
    i, j, k = 0, 0, 0

    while k < len(result):
        if i < len(s1) and s1[i] == result[k]:
            i = i + 1
        elif j < len(s2) and s2[j] == result[k]:
            j = j + 1
        else:
            return False
        k = k + 1
    return True


print(shufflecheck('XY', '12', 'X1Y2'))
print(shufflecheck('XY', '12', '2X1Y'))
print(shufflecheck('XY', '21', '2X1Y'))
print(shufflecheck('XY', '21', '2Y1Y'))
