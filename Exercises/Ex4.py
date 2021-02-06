from random import randrange

from pandas import *



def getNumberOfSoS(x, y):
    Matrix = [[0 for rows in range(x)] for columns in range(y)]

    for j in range(y):
        for i in range(x):
            Matrix[0][0] = 0

    cnt = (y * x) / 2

    while cnt >= 0:
        row = randrange(0, x)
        col = randrange(0, y)
        if Matrix[row][col] == 0:
            Matrix[row][col] = 83
            cnt -= 1

    for j in range(y):
        for i in range(x):
            if Matrix[j][i] == 0:
                Matrix[j][i] = 79

    # Horizontal check
    horizontalCnt = 0
    for row in range(x):
        for col in range(y - 2):
            ch1 = Matrix[row][col]
            ch2 = Matrix[row][col + 1]
            ch3 = Matrix[row][col + 2]
            if ch1 == 83 and ch3 == 83 and ch2 == 79:
                horizontalCnt += 1

    # Vertical check
    verticalCnt = 0
    for col in range(y):
        for row in range(x - 2):
            ch1 = Matrix[row][col]
            ch2 = Matrix[row + 1][col]
            ch3 = Matrix[row + 2][col]
            if ch1 == 83 and ch3 == 83 and ch2 == 79:
                verticalCnt += 1

    cnt = verticalCnt + horizontalCnt
    print(str(DataFrame(Matrix)))
    return cnt