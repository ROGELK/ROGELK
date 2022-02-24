from random import randint


def arrays(n):
    arrays = []
    array_length = []
    for i in range(n):
        array = []
        size = randint(1, n)
        if size not in array_length:
            array_length.append(size)
        else:
            while True:
                size = randint(1,n)
                if size not in array_length:
                    array_length.append(size)
                    break
        for k in range(size):
            array.append(randint(1, n))
        if i % 2 == 1:
            array = sorted(array)
        else:
            array = sorted(array, reverse=True)
        arrays.append(array)
        print(size)
    return (arrays)


number = int(input())
array = arrays(number)
print(array)