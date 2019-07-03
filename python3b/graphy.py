import unittest

EMPTY_GRAPH = []
SIMPLE_GRAPH = [('A', 'B')]
LINEAR_GRAPH = [('A', 'B'), ('B', 'C')]
TRIANGULAR_GRAPH = [('A', 'B'), ('B', 'C'), ('C', 'A')]

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

def minus(graph, node):
    return [x for x in graph if node not in x]

def pathfinder(starting_node, ending_node, graph):
    next_nodes = list(next_node(starting_node, graph))
    print('nn', next_nodes)
    if ending_node in next_nodes:
        next_next_nodes = [next_nodes]
    else:
        next_next_nodes = [[node] + list(next_node(node, minus(graph, starting_node))) for node in next_nodes]
    print('nnn', next_next_nodes)
    lol = [[starting_node] + x for x in next_next_nodes if ending_node in x]
    return lol

class TestMinus(unittest.TestCase):
    def test_removing_a_from_simple_graph_returns_b(self):
        self.assertEqual([], minus(SIMPLE_GRAPH, 'A'))

    def test_remove_a_from_linear_graph_returns_b_c(self):
        self.assertEqual([('B', 'C')], minus(LINEAR_GRAPH, 'A'))
        
class TestGraphy(unittest.TestCase):
    def test_can_get_from_a_to_b(self):
        self.assertEqual({'B'}, next_node('A', SIMPLE_GRAPH))

    def test_can_get_from_b_to_a(self):
        self.assertEqual({'A'}, next_node('B', SIMPLE_GRAPH))

    def test_no_next_node_in_a_one_node_graph(self):
        self.assertEqual(set(), next_node('A', EMPTY_GRAPH))

    def test_no_next_node_if_starting_node_not_in_graph(self):
        self.assertEqual(set(), next_node('C', SIMPLE_GRAPH))

    def test_can_get_from_a_to_b_in_a_three_node_graph(self):
        self.assertEqual({'B'}, next_node('A', LINEAR_GRAPH))

    def test_can_get_from_b_to_c_in_a_three_node_graph(self):
        self.assertEqual({'A', 'C'}, next_node('B', LINEAR_GRAPH))

    def test_can_get_from_a_to_b_and_c_in_a_triangular_graph(self):
        self.assertEqual({'B', 'C'}, next_node('A', TRIANGULAR_GRAPH))

    def test_can_get_from_a_to_b_and_c_in_a_triangular_graph(self):
        self.assertEqual({'A', 'C'}, next_node('B', TRIANGULAR_GRAPH))

    def test_can_get_from_a_to_b_and_c_in_a_triangular_graph(self):
        self.assertEqual({'A', 'B'}, next_node('C', TRIANGULAR_GRAPH))

class TestPathFinder(unittest.TestCase):
    # def test_pathfinder_for_simple_graph(self):
    #     self.assertEqual([['A', 'B']], pathfinder('A', 'B', SIMPLE_GRAPH), 'Cannot get from A to B')
    #     self.assertEqual([['B', 'A']], pathfinder('B', 'A', SIMPLE_GRAPH), 'Cannot get from B to A')
        
    def test_pathfinder_for_linear_graph(self):
        self.assertEqual([['A', 'B']], pathfinder('A', 'B', LINEAR_GRAPH), 'Cannot get from A to B')
        self.assertEqual([['B', 'C']], pathfinder('B', 'C', LINEAR_GRAPH), 'Cannot get from B to C')
        self.assertEqual([['A', 'B', 'C']], pathfinder('A', 'C', LINEAR_GRAPH), 'Cannot get from# A to C')
        
        
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
