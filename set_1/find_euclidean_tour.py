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
    nums = {}
    for edge in graph:
        if edge[0] in nums:
            nums[edge[0]] += 1
        else:
            nums[edge[0]] = 1

        if edge[1] in nums:
            nums[edge[1]] += 1
        else:
            nums[edge[1]] = 1
    return nums

def find_next(start, graph):
    for edge in graph:
        print( "checking ", edge)
        if start[1] == edge[0]:
            return edge
    return None

def find_eulerian_tour(graph):

    tour = list(graph)
    res = [tour[0], tour[1]]

    while len(tour) > 0:
        for edge in tour:
            next_edge = find_next(edge, tour)
            #print start_node, " ", end_node
            if next_edge == None:
                res.append(graph[len(graph)-1][1])
                return res
            res.append(next_edge)
            tour.remove(edge)
            tour.remove(next_edge)


    # your code here
    return []



t = [(1, 2), (2, 3), (3, 1)]
t2 = [(0, 1), (1, 5), (1, 7), (4, 5),(4, 8), (1, 6), (3, 7), (5, 9),(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
t3 = [(1, 13), (1, 6), (6, 11), (3, 13), (8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9), (1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),(7, 14),  (10, 13)]
t4 = [(8, 16), (8, 18), (16, 17), (18, 19), (3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14), (1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15), (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
print(count(t4))
print(find_eulerian_tour(t2))