# Edmonds Blossom
A python implementation of Edmonds blossom algorithm for maximum-cardinality matching.

Note: Check `test.py` to know how to use it.
## Examples

```python
from max_matching import Match, Node

#     *
#    / \      
#   * - *
#  / \ / \
# * - * - *
def test1():
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
    
    for node in nodes:
        if node.mate != None:
            assert node.mate.mate == node
            print(node, node.mate)

#                   * - *
#                  /    |
# * - * - * - * - *     |
#                  \    |
#                   * - *
#                   |
#                   *
def test2():
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
    
    for node in match.nodes:
        if node.mate is not None:
            if node.index < node.mate.index:
                print(node.index, node.mate.index)
```
