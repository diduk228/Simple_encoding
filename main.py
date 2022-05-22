import numpy as np
import time

def encode(str, row):
    start = 0
    end = int(len(str) / row)
    arr = []
    while int(len(str) - row*end) != 0:
            str = str + "+"
            end = int(len(str) / row)

    for i in range(row):
        if end > len(str):
            arr.append(list(str[start:len(str) + 1]))
            break
        arr.append(list(str[start:end]))
        start = end
        end = end + int(len(str)/row)
    encode_str = ""

    for k in range(len(arr[0])):
        for i in range(row):
            encode_str = encode_str + "".join(arr[i][k])
    print(f'encode: {encode_str}')

    for i in range(len(arr)):
        print(f'array: {arr[i]}')

    return arr

def decode(arr, row):

    decode_str = ""
    for i in range(row):
        decode_str = decode_str + ''.join(arr[i])
    print(f'decode: {decode_str.replace("+", "")}')


ans = "BAD"
while ans == "BAD":
    print("Input your string: ")
    str1 = str(input())
    print("Input row:")
    row = int(input())
    if "+" in str1:
        print("Please, input your string without +")
        continue
    encode_arr = encode(str1,row)
    decode_str = decode(encode_arr,row)
    ans = "GOOD"


