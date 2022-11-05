def parse_file_ucs(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    process_lines = []

    # Replace tabs and newlines with empty string, so we can use this graph easily
    for line in lines:
        line = line.replace('\t', '')
        line = line.replace('\n', '')
        process_lines.append(line)

    print("process")
    print(process_lines)


    # TODO
    return


def parse_file_astar(file_name):
    # TODO
    return


def ucs(graph):
    # TODO
    return


def astar(graph):
    # TODO
    return


def InformedSearch(method_name, problem_file_name):
    if method_name == 'UCS':
        graph = parse_file_ucs(problem_file_name)
        return ucs(graph)
    elif method_name == 'AStar':
        graph = parse_file_astar(problem_file_name)
        return astar(graph)
    else:
        print("Unexpected method name: " + method_name)


if __name__ == '__main__':
    print(InformedSearch("UCS", "sampleUCS.txt"))
    print("Done!")