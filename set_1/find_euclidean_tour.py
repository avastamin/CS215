from collections import defaultdict

__author__ = 'andrea'

# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]


def count(graph):
    nums = defaultdict(int)
    for edge in graph:
        nums[edge[0]] += 1
        nums[edge[1]] += 1
    return nums


def are_matching(node, edge):
    return node == edge[0] or node == edge[1]


def get_matching_node_from_edge(node, edge):
    if node == edge[0]:
        return edge[1]

    return edge[0]


def get_next_nodes(current_node, graph):
    matching_nodes = []
    for edge in graph:
        if are_matching(current_node, edge):
            matching_nodes.append(get_matching_node_from_edge(current_node, edge))

    if current_node in matching_nodes:
        matching_nodes.remove(current_node)
    return matching_nodes


def get_edge_from_nodes(current_node, next_node, graph):
    if (current_node, next_node) in graph:
        return current_node, next_node

    return next_node, current_node


def find_next(current_node, remaining_edges, eulerian_path):
    print("current: ", current_node, " remaining: ", remaining_edges, " path:", eulerian_path)

    next_nodes = get_next_nodes(current_node, remaining_edges)
    if not next_nodes:
        return None

    for next_node in next_nodes:
        eulerian_path.append(current_node)
        remaining_edges.remove(get_edge_from_nodes(current_node, next_node, remaining_edges))
        if not remaining_edges:
            eulerian_path.append(next_node)
            return eulerian_path
        if find_next(next_node, remaining_edges, eulerian_path) is not None:
            return eulerian_path
        # eulerian_path.remove(current_node)
        # remaining_edges.append(get_edge_from_nodes(current_node, next_node, remaining_edges))

    print("finished loop: current: ", current_node, " remaining: ", remaining_edges, " path:", eulerian_path)


    return None


def find_eulerian_tour(graph):
    edges_num = count(graph)

    for node in edges_num.keys():
        print("Starting node: ", node)
        tour = list(graph)
        eulerian_path = []
        if find_next(node, tour, eulerian_path):
            return eulerian_path

    print("No solutions found.")
    return None


test_set = [(1, 2), (2, 3), (3, 1)]
test_set2 = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
test_set3 = [(1, 13), (1, 6), (6, 11), (3, 13), (8, 13), (0, 6), (8, 9), (5, 9), (2, 6), (6, 10), (7, 9), (1, 12), (4, 12) ,(5, 14), (0, 1), (2, 3), (4, 11), (6, 9), (7, 14), (10, 13)]
test_set4 = [(8, 16), (8, 18), (16, 17), (18, 19), (3, 17), (13, 17), (5, 13), (3, 4), (0, 18), (3, 14), (11, 14), (1, 8), (1, 9), (4, 12), (2, 19), (1, 10), (7, 9), (13, 15), (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]

print(count(test_set3))
print("solution= ", find_eulerian_tour(test_set3))
# print(find_eulerian_tour(test_set2))
# print(find_eulerian_tour(test_set3))
# print(find_eulerian_tour(test_set4))