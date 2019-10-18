#!/usr/bin/python


def sum(m, n):
    results = m
    if m >= 0 and n >= 0 or m < 0 and n >= 0:
        for i in range(n):
            results += 1
    elif m < 0 and n < 0 or m >= 0 and n < 0:
        for i in range(-n):
            results -= 1

    return results


def divide(D, d):
    '''
    Variable declarations:
    D -> Dividend 
    d -> divisor
    '''
    result = 0
    negativeResult = D > 0 and d < 0 or D < 0 and d > 0
    d = abs(d)
    D = abs(D)
    if d == 0:
        raise ZeroDivisionError('Is not allowed division by 0!')

    while (D - d >= 0):
        D -= d
        result += 1

    result = - result if negativeResult else result

    return result

print(sum(1,3))
print(divide(10,2))
print(divide(7,-2))
print(divide(7,0))