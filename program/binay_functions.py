import os
import blifparser.blifparser as blifparser


def binary_array_to_int(array):
    result = int("".join(str(x) for x in array), 2)
    return result


def binary_array_to_string(array):
    result = "".join(str(x) for x in array)
    return result


def int_to_binary_array(number, size=-1):
    if size == -1:
        string = format(number, 'b')
        return bin_string_to_binary_array(string)
    else:
        string = format(number, 'b')
        array = bin_string_to_binary_array(string)
        if len(array) < size:
            array = concat_zeros(array, size - len(array))
        return array


def bin_string_to_binary_array(string):
    array = list(string)
    result = [eval(i) for i in array]
    return result


def concat_zeros(array, amount):
    zeros = []
    for i in range(amount):
        zeros.append(0)
    zeros.extend(array)
    # print("zeros:", zeros)
    return zeros
