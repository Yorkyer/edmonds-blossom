# Edmonds Blossom
A python implementation of Edmonds blossom algorithm for maximum-cardinality matching.

Note: Check `test.py` to know how to use it.
## Examples

```python
#   *   * - *
#  / \ / \
# * - * - *
def test_unmatched_nodes1():
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

    assert unmatched_nodes == 0    


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

    assert unmatched_nodes == 0

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

    assert unmatched_nodes == 0


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

    assert nodes[0].mate == nodes[1]
    assert nodes[1].mate == nodes[0]
    assert nodes[2].mate == nodes[3]
    assert nodes[3].mate == nodes[2]
    assert nodes[4].mate == nodes[5]
    assert nodes[5].mate == nodes[4]
```
