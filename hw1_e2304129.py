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


def extract_min(queue, costs):
    min_cost = 1_000_000
    min_cost_item = None

    for item in queue:
        if costs[item] < min_cost:
            min_cost = costs[item]
            min_cost_item = item

    queue.remove(min_cost_item)
    return min_cost_item


def is_within_graph(graph_size, coords):
    size_x, size_y = graph_size
    x, y = coords
    return size_x > x >= 0 and size_y > y >= 0


def get_potential_neighbors(coords):
    result = []
    x, y = coords
    result.append((x - 1, y))
    result.append((x + 1, y))
    result.append((x, y - 1))
    result.append((x, y + 1))
    return result


def get_walkable_neighbors(graph, graph_size, coords):
    result = []
    for potential in get_potential_neighbors(coords):
        if is_within_graph(graph_size, potential) and not is_obstacle(graph, potential):
            result.append(potential)

    return result


def construct_path(previous_dict, end):
    result = []
    current = end
    while current is not None:
        result.append(current)
        current = previous_dict[current]

    return result


def get_heuristic(graph, coords):
    letter = get_letter(graph, coords)

    if letter == '.':
        return 0
    elif letter == 'E':
        return 0
    elif letter == 'S':
        return 0
    elif letter == '#':
        print("Error: Shouldn't query blocked cell")
        return -1

    return int(letter)


def search(graph):
    graph_size = get_graph_size(graph)
    start = get_start_coords(graph, graph_size)
    frontier = []
    expanded = set()
    costs = {}
    previous = {}

    costs[start] = 0
    previous[start] = None

    frontier.append(start)

    while len(frontier) > 0:
        current_coords = extract_min(frontier, costs)
        current_cost = costs[current_coords]

        if is_end(graph, current_coords):
            return construct_path(previous, current_coords)

        expanded.add(current_coords)

        for neighbor in get_walkable_neighbors(graph, graph_size, current_coords):
            if neighbor not in expanded:
                print(neighbor)
                update_cost = current_cost + 1 + get_heuristic(graph, neighbor)
                if neighbor not in frontier:
                    frontier.append(neighbor)
                    costs[neighbor] = update_cost
                    previous[neighbor] = current_coords
                elif update_cost < costs[neighbor]:
                    costs[neighbor] = update_cost
                    previous[neighbor] = current_coords

    print("Error: Shouldn't reach here!")
    return []


def astar(graph):
    # TODO
    return


def InformedSearch(method_name, problem_file_name):
    if method_name == 'UCS':
        graph = parse_file_ucs(problem_file_name)
        return search(graph)
    elif method_name == 'AStar':
        graph = parse_file_ucs(problem_file_name)
        return search(graph)
    else:
        print("Unexpected method name: " + method_name)


if __name__ == '__main__':
    print(InformedSearch("UCS", "sampleUCS.txt"))
    print("Done!")
