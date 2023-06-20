import math


def getBitCount(X):
    if X == 0:
        return 1

    count = 0
    while X > 0:
        count += 1
        X >>= 1
    return count


def createSubvectors(X, subvectorBitCount, subvectorCount):

    subvectors = []
    for _ in range(subvectorCount):
        subvector = [0] * subvectorBitCount
        subvectors.append(subvector)

    for i in range(subvectorCount):
        for j in range(subvectorBitCount - 1, -1, -1):
            subvectors[i][j] = X % 2
            X //= 2
    return subvectors


def printSubvectors(subvectors):

    for subvector in subvectors:
        print("[ ", end="")
        for bit in subvector:
            print(bit, end=" ")
            print("]", end=" ")
            print()


def subvectorToDec(subvector):

    dec = 0
    for i in range(len(subvector)):
        dec += subvector[i] * int(math.pow(2, len(subvector) - i - 1))
    return dec


def getMultResult(A, B, P):

    bitsOfbiggerNumber = getBitCount(max(A, B))
    subvectorBitCount = 3  # r
    subvectorCount = math.ceil(bitsOfbiggerNumber / subvectorBitCount)  # delta
    print(bitsOfbiggerNumber, subvectorBitCount)

    subvectorsA = createSubvectors(A, subvectorBitCount, subvectorCount)
    printSubvectors(subvectorsA)

    subvectorsB = createSubvectors(B, subvectorBitCount, subvectorCount)
    printSubvectors(subvectorsB)

    result = 0

    for i in range(len(subvectorsA)):
        for j in range(len(subvectorsB)):

            A_iter = subvectorToDec(subvectorsA[i])
            B_iter = subvectorToDec(subvectorsB[j])

            S_temp = A_iter * B_iter * int(math.pow(2,
                                                    ((i + 1) + (j + 1) - 2) * subvectorBitCount)) % P

            result += S_temp

    print(result)

    range_ = int(math.pow(2, 3 * subvectorCount + subvectorCount))

    rangeBitCount = getBitCount(range_)
    resultSubvectorCount = math.ceil(rangeBitCount / subvectorBitCount)
    resultSubvectors = createSubvectors(result, subvectorBitCount,
                                        resultSubvectorCount)
    printSubvectors(resultSubvectors)

    power = 0
    ans = 0
    for i in range(subvectorCount + 1):
        ans_temp = subvectorToDec(
            resultSubvectors[i]) * int(math.pow(2, power)) % P
        power += subvectorBitCount
        ans += ans_temp
    if ans > P:
        ans -= P
    print(ans)


A = 45
B = 15
P = 47

getMultResult(A, B, P)
