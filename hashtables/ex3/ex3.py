def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # array dictionary
    array_dict = {}

    # result list
    result = []

    # loop through the arrays
    for array in arrays:
        # loop through numbers in array
        for num in array:
            if num not in array_dict:
                # tally 1 as value if not in dict
                array_dict[num] = 1
            else:
                # if num is in dict plus add 1
                array_dict[num] += 1

    length = len(arrays)

    # loop through dict as a list
    for item in list(array_dict.items()):
        # if item value is equal length
        # then all arrays have same item number
        if item[1] == length:
            # add item number to list
            result.append(item[0])

    # return list of same item numbers
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
