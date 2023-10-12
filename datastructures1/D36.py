import random

def maxLongSequence (list):
    maxSequence = []
    currentSequence = []

    for i in list:
        if i % 2 != 0:
            currentSequence.append(i)
        else:
            if len(currentSequence) > len(maxSequence):
                maxSequence = currentSequence
                currentSequence = []

    # дополнительна проверка для случая, когда наибольшая последовательность находится в самом конце
    if len(currentSequence) > len(maxSequence):
        maxSequence = currentSequence

    return maxSequence

list = [2,54,3,3,5,7,9,13,26,27,27,13,13,1,1,1,1,1,1,1,1]
print(maxLongSequence(list))
