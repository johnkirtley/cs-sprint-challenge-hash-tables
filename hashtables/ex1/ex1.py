def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    nums = {}

    if len(weights) == 1:
        return None

    for index, val in enumerate(weights):
        nums[val] = index

    for index, val in enumerate(weights):
        difference = limit - val

        if difference in nums and nums[difference] != index:
            print(f"{weights}", nums[difference], index)
            return (nums[difference], index)
