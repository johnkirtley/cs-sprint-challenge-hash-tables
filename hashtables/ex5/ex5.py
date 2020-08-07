# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    file_paths = {}
    result = []

    for path in files:
        temp = path.split("/")
        key = temp[-1]

        if key not in file_paths:
            file_paths[key] = path

    for query in queries:
        if query in file_paths:
            result.append(file_paths[query])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
