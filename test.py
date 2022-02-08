import unittest
from max_matching import *


class TestMatch(unittest.TestCase):

    #   *   * - *
    #  / \ / \
    # * - * - *
    def test_unmatched_nodes1(self):
        nodes = [Node() for i in range(6)]
        nodes[0].neighbors.append(nodes[1])
        nodes[1].neighbors.append(nodes[0])
        nodes[0].neighbors.append(nodes[2])
        nodes[2].neighbors.append(nodes[0])
        nodes[1].neighbors.append(nodes[2])
        nodes[2].neighbors.append(nodes[1])
        nodes[2].neighbors.append(nodes[4])
        nodes[4].neighbors.append(nodes[2])
        nodes[3].neighbors.append(nodes[2])
        nodes[2].neighbors.append(nodes[3])
        nodes[4].neighbors.append(nodes[3])
        nodes[3].neighbors.append(nodes[4])
        nodes[4].neighbors.append(nodes[5])
        nodes[5].neighbors.append(nodes[4])

        match = Match(nodes)
        unmatched_nodes = match.unmatched_nodes()

        self.assertEqual(unmatched_nodes, 0)    



    #   * 
    #  / \ 
    # * - *
    def test_unmatched_nodes2(self):
        nodes = [Node() for i in range(3)]
        nodes[0].neighbors.append(nodes[1])
        nodes[1].neighbors.append(nodes[0])
        nodes[0].neighbors.append(nodes[2])
        nodes[2].neighbors.append(nodes[0])
        nodes[1].neighbors.append(nodes[2])
        nodes[2].neighbors.append(nodes[1])

        match = Match(nodes)
        unmatched_nodes = match.unmatched_nodes()

        self.assertEqual(unmatched_nodes, 1)

    #     *
    #    / \      
    #   * - *
    #  / \ / \
    # * - * - *
    def test_unmatched_nodes3(self):
        nodes = [Node() for i in range(6)]

        nodes[0].neighbors.append(nodes[1])
        nodes[1].neighbors.append(nodes[0])
        nodes[0].neighbors.append(nodes[2])
        nodes[2].neighbors.append(nodes[0])
        nodes[1].neighbors.append(nodes[2])
        nodes[2].neighbors.append(nodes[1])

        nodes[1].neighbors.append(nodes[3])
        nodes[3].neighbors.append(nodes[1])
        nodes[1].neighbors.append(nodes[4])
        nodes[4].neighbors.append(nodes[1])
        nodes[3].neighbors.append(nodes[4])
        nodes[4].neighbors.append(nodes[3])

        nodes[2].neighbors.append(nodes[4])
        nodes[4].neighbors.append(nodes[2])
        nodes[2].neighbors.append(nodes[5])
        nodes[5].neighbors.append(nodes[2])
        nodes[4].neighbors.append(nodes[5])
        nodes[5].neighbors.append(nodes[4])

        match = Match(nodes)
        unmatched_nodes = match.unmatched_nodes()

        self.assertEqual(unmatched_nodes, 0)


    #                   * - *
    #                  /    |
    # * - * - * - * - *     |
    #                  \    |
    #                   * - *
    #                   |
    #                   *
    def test_unmatched_node4(self):
        edges = [
            (0, 1),
            (1, 0),
            (0, 8),
            (8, 0),
            (1, 2),
            (2, 1),
            (2, 3),
            (3, 2),
            (3, 4),
            (4, 3),
            (3, 7),
            (7, 3),
            (4, 5),
            (5, 4),
            (5, 6),
            (6, 5),
            (6, 7),
            (7, 6),
            (7, 9),
            (9, 7),
        ]
        match = Match.from_edges(10, edges)
        unmatched_nodes = match.unmatched_nodes()

        self.assertEqual(unmatched_nodes, 0)


    #                   * - *
    #                  /    |
    # * - * - * - * - *     |
    #                  \    |
    #                   * - *
    #                       |
    #                       *
    def test_unmatched_node5(self):
        edges = [
            (0, 1),
            (1, 0),
            (0, 8),
            (8, 0),
            (1, 2),
            (2, 1),
            (2, 3),
            (3, 2),
            (3, 4),
            (4, 3),
            (3, 7),
            (7, 3),
            (4, 5),
            (5, 4),
            (5, 6),
            (6, 5),
            (6, 7),
            (7, 6),
            (6, 9),
            (9, 6),
        ]
        match = Match.from_edges(10, edges)
        unmatched_nodes = match.unmatched_nodes()

        self.assertEqual(unmatched_nodes, 0)


    def test_issue_3(self):
        edges = [(3, 0), (0, 3), (3, 1), (1, 3), (3, 2), (2, 3), (4, 3), (3, 4), (5, 0), (0, 5), (5, 1), (1, 5), (5, 2), (2, 5), (5, 3), (3, 5), (5, 4), (4, 5), (6, 0), (0, 6), (6, 1), (1, 6), (6, 2), (2, 6), (6, 3), (3, 6), (6, 4), (4, 6), (6, 5), (5, 6), (7, 0), (0, 7), (7, 1), (1, 7), (7, 2), (2, 7), (7, 3), (3, 7), (7, 4), (4, 7), (7, 5), (5, 7), (7, 6), (6, 7), (8, 0), (0, 8), (8, 1), (1, 8), (8, 2), (2, 8), (8, 3), (3, 8), (8, 4), (4, 8), (8, 5), (5, 8), (8, 6), (6, 8), (8, 7), (7, 8), (9, 0), (0, 9), (9, 1), (1, 9), (9, 2), (2, 9), (9, 3), (3, 9), (9, 4), (4, 9), (9, 5), (5, 9), (9, 6), (6, 9), (9, 7), (7, 9), (9, 8), (8, 9)]
        match = Match.from_edges(10, edges)
        unmatched_nodes = match.unmatched_nodes()

        self.assertEqual(unmatched_nodes, 0)


    def test_maximum_matching(self):
        nodes = [Node() for i in range(6)]
        nodes[0].neighbors.append(nodes[1])
        nodes[1].neighbors.append(nodes[0])
        nodes[0].neighbors.append(nodes[2])
        nodes[2].neighbors.append(nodes[0])
        nodes[1].neighbors.append(nodes[2])
        nodes[2].neighbors.append(nodes[1])
        nodes[2].neighbors.append(nodes[4])
        nodes[4].neighbors.append(nodes[2])
        nodes[3].neighbors.append(nodes[2])
        nodes[2].neighbors.append(nodes[3])
        nodes[4].neighbors.append(nodes[3])
        nodes[3].neighbors.append(nodes[4])
        nodes[4].neighbors.append(nodes[5])
        nodes[5].neighbors.append(nodes[4])
        nodes[1].mate = nodes[2]
        nodes[2].mate = nodes[1]
        nodes[3].mate = nodes[4]
        nodes[4].mate = nodes[3]

        match = Match(nodes)
        match.freenodes = [nodes[0], nodes[5]]
        match.maximum_matching()

        self.assertEqual(nodes[0].mate, nodes[1])
        self.assertEqual(nodes[1].mate, nodes[0])
        self.assertEqual(nodes[2].mate, nodes[3])
        self.assertEqual(nodes[3].mate, nodes[2])
        self.assertEqual(nodes[4].mate, nodes[5])
        self.assertEqual(nodes[5].mate, nodes[4])


    def test_find_augmenting_path(self):
        nodes = [Node() for i in range(6)]
        nodes[0].neighbors.append(nodes[1])
        nodes[1].neighbors.append(nodes[0])
        nodes[0].neighbors.append(nodes[2])
        nodes[2].neighbors.append(nodes[0])
        nodes[1].neighbors.append(nodes[2])
        nodes[2].neighbors.append(nodes[1])
        nodes[2].neighbors.append(nodes[4])
        nodes[4].neighbors.append(nodes[2])
        nodes[3].neighbors.append(nodes[2])
        nodes[2].neighbors.append(nodes[3])
        nodes[4].neighbors.append(nodes[3])
        nodes[3].neighbors.append(nodes[4])
        nodes[4].neighbors.append(nodes[5])
        nodes[5].neighbors.append(nodes[4])
        nodes[1].mate = nodes[2]
        nodes[2].mate = nodes[1]
        nodes[3].mate = nodes[4]
        nodes[4].mate = nodes[3]

        match = Match(nodes)
        path = match.find_augmenting_path(nodes[0])

        self.assertEqual(path.nodes,
            [nodes[5],nodes[4],nodes[3],nodes[2],nodes[1],nodes[0]])


    def test_shrink_blossom(self):
        nodes = [Node() for i in range(5)]
        nodes[3].neighbors.append(nodes[0])
        nodes[0].neighbors.append(nodes[3])
        nodes[4].neighbors.append(nodes[0])
        nodes[0].neighbors.append(nodes[4])
        nodes[2].neighbors.append(nodes[4])
        nodes[4].neighbors.append(nodes[2])

        match = Match(nodes)
        blossom = nodes[0:3]
        snode = match.shrink_blossom(blossom)

        self.assertEqual(snode.subnodes, blossom)
        self.assertEqual(snode.original_edges, [
            (nodes[0],nodes[3]),
            (nodes[0],nodes[4]),
            (nodes[2],nodes[4])])
        self.assertEqual(snode.neighbors,
            [nodes[3],nodes[4],nodes[4]])
        self.assertEqual(nodes[3].neighbors,
            [snode])
        self.assertEqual(nodes[4].neighbors,
            [snode,snode])
        self.assertFalse(nodes[4] in nodes[0].neighbors)
        self.assertFalse(nodes[4] in nodes[2].neighbors)
        self.assertFalse(nodes[3] in nodes[0].neighbors)



    def test_find_cycles(self):
        nodes = [Node() for i in range(4)]
        nodes[0].parent = nodes[1]
        nodes[1].parent = nodes[2]
        nodes[3].parent = nodes[2]

        match = Match(nodes)
        cycle = match.find_cycles(nodes[0], nodes[3])
        self.assertEqual(cycle,
            [nodes[0], nodes[1], nodes[2], nodes[3]])


    def test_invert_path(self):
        nodes = [Node() for i in range(4)]
        path = Path()
        for node in nodes:
            path.nodes.append(node)

        nodes[1].mate = nodes[2]
        nodes[2].mate = nodes[1]

        match = Match(nodes)
        match.invert_path(path)

        self.assertEqual(nodes[0].mate, nodes[1])
        self.assertEqual(nodes[1].mate, nodes[0])
        self.assertEqual(nodes[2].mate, nodes[3])
        self.assertEqual(nodes[3].mate, nodes[2])



    def test_expand_supernode(self):
        snode = SuperNode()
        nodes = [Node() for i in range(5)]
        snode.subnodes.append(nodes[0])
        snode.subnodes.append(nodes[1])
        snode.subnodes.append(nodes[2])
        snode.neighbors.append(nodes[3])
        snode.neighbors.append(nodes[4])
        snode.neighbors.append(nodes[4])
        nodes[3].neighbors.append(snode)
        nodes[4].neighbors.append(snode)
        nodes[4].neighbors.append(snode)
        snode.original_edges.append((nodes[0], nodes[3]))
        snode.original_edges.append((nodes[0], nodes[4]))
        snode.original_edges.append((nodes[2], nodes[4]))

        match = Match(nodes)
        match.expand_supernode(snode)

        self.assertTrue(nodes[0] in nodes[4].neighbors)
        self.assertTrue(nodes[4] in nodes[0].neighbors)
        self.assertTrue(nodes[0] in nodes[3].neighbors)
        self.assertTrue(nodes[3] in nodes[0].neighbors)
        self.assertTrue(nodes[2] in nodes[4].neighbors)
        self.assertTrue(nodes[4] in nodes[2].neighbors)

        self.assertFalse(nodes[3] in snode.neighbors)
        self.assertFalse(nodes[4] in snode.neighbors)
        self.assertFalse(snode in nodes[3].neighbors)
        self.assertFalse(snode in nodes[4].neighbors)



if __name__ == '__main__':
    unittest.main()
