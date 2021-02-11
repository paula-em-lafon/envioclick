def pairSum(array, sum):
    dict = {}
    for i in array:
        if sum - i in dict:
            return [i, sum-i]
        dict[i] = 1
    return []
 
 
if __name__ == '__main__':
 
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    sum = 10
 
    print(pairSum(array, sum))