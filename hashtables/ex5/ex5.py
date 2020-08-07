# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    file_paths = {}
    search_results = []
    result = []

    for path in files:
        temp = path.split("/")
        key = temp[-1]

        if key not in file_paths:
            file_paths[key] = [path]
        else:
            file_paths[key].append(path)

    for query in queries:
        if query in file_paths:
            search_results.append(file_paths[query])

    for i in range(len(search_results)):
        for j in range(len(search_results[i])):
            result.append(search_results[i][j])

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
