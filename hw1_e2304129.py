def get_start_coords(graph, graph_size):
    size_x, size_y = graph_size
    for x in range(size_x):
        for y in range(size_y):
            coords = (x, y)
            if is_start(graph, coords):
                return coords

    print("Error: Couldn't find start coordinates")
    return -1, -1


def is_obstacle(graph, coords):
    return get_letter(graph, coords) == '#'


def is_end(graph, coords):
    return get_letter(graph, coords) == 'E'


def is_start(graph, coords):
    return get_letter(graph, coords) == 'S'


def get_letter(graph, coords):
    x, y = coords
    return graph[y][x]


def get_graph_size(graph):
    size_x = len(graph[0])
    size_y = len(graph)
    return size_x, size_y


def parse_file_ucs(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    process_lines = []

    # Replace tabs and newlines with empty string, so we can use this graph easily
    for line in lines:
        line = line.replace('\t', '')
        line = line.replace('\n', '')
        process_lines.append(line)

    print(process_lines)
    return process_lines


def parse_file_astar(file_name):
    # TODO
    return


def ucs(graph):
    graph_size = get_graph_size(graph)
    start = get_start_coords(graph, graph_size)

    print(f"Start {start}")

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
