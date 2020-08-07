def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    nums = {}
    result = []

    for i in a:
        if i < 0 and i not in nums:
            nums[i] = i

    for i in a:
        if i > 0 and (i * -1) in nums:
            result.append(i)

    if len(result) > 0:
        return result
    else:
        return []


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
