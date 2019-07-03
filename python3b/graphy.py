import unittest

def next_node(starting_node, graph):
    if not graph:
        return set()
    
    list_of_matches = [x for x in graph if x[0] == starting_node or x[1] == starting_node]

    if not list_of_matches:
        return set()

    # get the other element of the tuple for each match B: (A,B),(B,C) = [A,C]
    next_nodes = set()
    for match in list_of_matches:
        if match[0] == starting_node:
            next_nodes.add(match[1])
        else:
            next_nodes.add(match[0])
    return next_nodes

def pathfinder(starting_node, ending_node, graph):
    return [['B']]

class TestGraphy(unittest.TestCase):
    def test_can_get_from_a_to_b(self):
        self.assertEqual({'B'}, next_node('A', [('A', 'B')]))

    def test_can_get_from_b_to_a(self):
        self.assertEqual({'A'}, next_node('B', [('A', 'B')]))

    def test_no_next_node_in_a_one_node_graph(self):
        self.assertEqual(set(), next_node('A', []))

    def test_no_next_node_if_starting_node_not_in_graph(self):
        self.assertEqual(set(), next_node('C', [('A', 'B')]))

    def test_can_get_from_a_to_b_in_a_three_node_graph(self):
        self.assertEqual({'B'}, next_node('A', [('A', 'B'), ('B', 'C')]))

    def test_can_get_from_b_to_c_in_a_three_node_graph(self):
        self.assertEqual({'A', 'C'}, next_node('B', [('A', 'B'), ('B', 'C')]))

    def test_can_get_from_a_to_b_and_c_in_a_triangular_graph(self):
        self.assertEqual({'B', 'C'}, next_node('A', [('A', 'B'), ('B', 'C'), ('C', 'A')]))

    def test_can_get_from_a_to_b_and_c_in_a_triangular_graph(self):
        self.assertEqual({'A', 'C'}, next_node('B', [('A', 'B'), ('B', 'C'), ('C', 'A')]))

    def test_can_get_from_a_to_b_and_c_in_a_triangular_graph(self):
        self.assertEqual({'A', 'B'}, next_node('C', [('A', 'B'), ('B', 'C'), ('C', 'A')]))

    def test_pathfinder_return_set_of_paths(self):
        self.assertEqual([['B']], pathfinder('A', 'B', [('A', 'B')]))


if __name__ == '__main__':
    unittest.main()


    # path = [], A -> B -> C
    # path = [A], B -> C
    # path = [A, B], C
    # path = [A, B, C], e

    # path = [A], (A, B), (B, C), (C, A)
    # path = [A, B], (B, C)
    #        [A, C], (B, C)
    # path = [A, B, C], ()
    #        [A, C], done
