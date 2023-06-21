import math


def bit_counter(number):
    if number == 0:
        return 1

    count = 0
    while number > 0:

        count += 1
        number >>= 1
    return count


def create_binary_subvector_alg_gorodecky(number, nrOfBits, nrOfSubvectors):

    subvectors = []
    for _ in range(nrOfSubvectors):
        subvector = [0] * nrOfBits
        subvectors.append(subvector)

    for i in range(nrOfSubvectors):
        for j in range(nrOfBits - 1, -1, -1):
            subvectors[i][j] = number % 2
            number //= 2
    return subvectors


def binary_to_dec(subvector):

    dec = 0
    for i in range(len(subvector)):
        dec += subvector[i] * int(math.pow(2, len(subvector) - i - 1))
    return dec


def modulo_multiplication(A, B, P):

    bitsOfbiggerNumber = bit_counter(max(A, B))
    nrOfBits = 3  # r
    nrOfSubvectors = math.ceil(bitsOfbiggerNumber / nrOfBits)  # delta

    subvectorsA = create_binary_subvector_alg_gorodecky(
        A, nrOfBits, nrOfSubvectors)

    subvectorsB = create_binary_subvector_alg_gorodecky(
        B, nrOfBits, nrOfSubvectors)

    result = 0

    for i in range(len(subvectorsA)):
        for j in range(len(subvectorsB)):

            A_iter = binary_to_dec(subvectorsA[i])
            B_iter = binary_to_dec(subvectorsB[j])

            S_temp = A_iter * B_iter * int(math.pow(2,
                                                    ((i + 1) + (j + 1) - 2) * nrOfBits)) % P

            result += S_temp

    range_ = int(math.pow(2, 3 * nrOfSubvectors + nrOfSubvectors))

    rangeBitCount = bit_counter(range_)
    resultSubvectorCount = math.ceil(rangeBitCount / nrOfBits)
    resultSubvectors = create_binary_subvector_alg_gorodecky(result, nrOfBits,
                                                             resultSubvectorCount)

    power = 0
    finalResult = 0
    for i in range(nrOfSubvectors + 1):
        ans_temp = binary_to_dec(
            resultSubvectors[i]) * int(math.pow(2, power)) % P
        power += nrOfBits
        finalResult += ans_temp
    if finalResult > P:
        finalResult -= P
    print(finalResult)


A = 35
B = 77
P = 53

modulo_multiplication(A, B, P)
