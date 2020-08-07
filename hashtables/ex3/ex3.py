

def intersection(arrays):
    """
    YOUR CODE HERE
    """

    nums = {}

    for array in arrays:
        for val in array:

            if val not in nums:
                nums[val] = 1
            else:
                nums[val] += 1

    return [key for key, value in nums.items() if value == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
