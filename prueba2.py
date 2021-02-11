def isValidSubsequence(array, sequence):
    sequence_len = len(sequence)
    counter = 0
    for i in array:
        if i == sequence[counter]:
            counter += 1   
            if counter == sequence_len:
                return True
    return False

if __name__ == '__main__':
    sequence = [1, 6, -1, 10]
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    print(isValidSubsequence(array, sequence))