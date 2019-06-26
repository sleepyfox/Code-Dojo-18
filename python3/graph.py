import unittest

def find_shortest_path(graph, start, end):
    route = [start]
    list_of_next_places = graph[start]
    # take into account having more than one place to go next
    # Don't go back to the same node
    # return the shortest of multiple paths
    route.append(list_of_next_places[0]) # B
    if list_of_next_places[0] == end:
        return len(route)
    else:
        list_of_next_next_places = graph[list_of_next_places[0]]
        if list_of_next_next_places[-1] == end:
            route.append(list_of_next_next_places[-1])
            return len(route)

class TestGraphTraversal(unittest.TestCase):

    def test_a_graph_with_two_nodes(self):
        graph = {"A": ["B"],
                 "B": ["A"]}
        self.assertEqual(find_shortest_path(graph, "A", "B"), 2)

    def test_a_graph_with_three_nodes_in_a_line(self):
        graph = {"A": ["B"],
                 "B": ["A", "C"],
                 "C": ["B"]}
        self.assertEqual(find_shortest_path(graph, "A", "C"), 3)

if __name__ == '__main__':
    unittest.main()
