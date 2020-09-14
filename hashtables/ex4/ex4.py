def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    # number dictionary
    num_dict = {}

    # result list
    result = []

    # loop through array
    for num in a:
        # check if absolute number is not in dictionary
        if abs(num) not in num_dict:
            # if not, tally 1
            num_dict[abs(num)] = 1
        else:
            # if it is, plus add 1
            num_dict[abs(num)] += 1

    # loop through the list of dictionary items
    for num in list(num_dict.items()):
        # if item value is equal to 2
        # then there is a corresponding negative number
        if num[1] == 2:
            # append number that has corresponding negative number to list
            result.append(num[0])

    # return list of results
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
