import math


def calc_length(number):
    length = 0
    while number != 0:
        number >>= 1
        length += 1
    return length


def get_delta(l, P):
    delta = 0
    while P * math.pow(2, delta) < math.pow(2, l) - 1:
        delta += 1
    return delta


def mod_bit_by_bit(X, P, delta):
    while delta >= 0:
        if X >= P * math.pow(2, delta):
            X -= P * math.pow(2, delta)
        print("X" + str(delta) + " : ", X)
        delta -= 1
    return X


def main():
    l = calc_length(X)
    delta = get_delta(l, P)
    R = mod_bit_by_bit(X, P, delta)
    print("Ilosc bitow: ", l)
    print("Ile iteracji: ", delta)
    print("Reszta: ", R)


if __name__ == "__main__":
    X = 888
    P = 21
    main()
