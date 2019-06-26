import unittest


def remove_from_graph(graph, node):
    new_graph = graph
    del(new_graph[node])
    for key in new_graph:
        if node in new_graph[key]:
            new_graph[key].remove(node)
    return new_graph

def find_shortest_path(graph, start, end):
    routes = []
    route = [start]
    list_of_next_places = graph[start]
    # return the shortest of multiple paths
    for next_node in list_of_next_places:
        if next_node in route:
            break
        while next_node != end:
            route.append(next_node)
            list_of_next_next_places = graph[next_node]
            if list_of_next_next_places[-1] == end:
                route.append(list_of_next_next_places[-1])
                return len(route)
        route.append(next_node) # B
    routes.append(len(route))
    return min(routes)

def shortest(graph, start, end, counter):
    for next_node in graph(start):
        if end in graph[start]:
            return 1 + counter
        else:
            return shortest(remove_from_graph(graph, "A"), next_node, end, counter + 1)


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

    # def test_a_graph_with_three_nodes_in_a_triangle(self):
    #     graph = {"A": ["B", "C"],
    #              "B": ["A", "C"],
    #              "C": ["B", "A"]}
    #     self.assertEqual(find_shortest_path(graph, "A", "C"), 2)


class TestGraphNinja(unittest.TestCase):

    def test_removing_B_from_a_two_node_graph_leaves_A(self):
        graph = {"A": ["B"],
                 "B": ["A"]}
        self.assertEqual(remove_from_graph(graph, "A"), {"B": []})

    def test_removing_A_from_a_two_node_graph_leaves_B(self):
        graph = {"A": ["B"],
                 "B": ["A"]}
        self.assertEqual(remove_from_graph(graph, "B"), {"A": []})

    def test_removing_C_from_a_three_node_graph_leaves_A_and_B(self):
        graph = {"A": ["B"],
                 "B": ["A", "C"],
                 "C": ["B"]}
        self.assertEqual(remove_from_graph(graph, "C"), {"A":["B"], "B":["A"]})

    def test_removing_B_from_a_three_node_graph_leaves_A_and_C(self):
        graph = {"A": ["B"],
                 "B": ["A", "C"],
                 "C": ["B"]}
        self.assertEqual(remove_from_graph(graph, "B"), {"A":[],"C":[]})


if __name__ == '__main__':
    unittest.main()
