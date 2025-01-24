# write tests for bfs
import pytest
from search import graph
from search.graph import Graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class
    using the 'tiny_network.adjlist' file and assert
    that all nodes are being traversed (ie. returns
    the right number of nodes, in the right order, etc.)
    """
    graph = Graph('data/tiny_network.adjlist')

    # Test traversal starting from 'Luke Gilbert'
    luke = graph.bfs('Luke Gilbert')
    assert luke == ['Luke Gilbert', '33483487', '31806696', '31626775', '31540829', 'Martin Kampmann', 'Neil Risch', 'Nevan Krogan', '32790644', '29700475', '34272374', '32353859', '30944313', 'Steven Altschuler', 'Lani Wu', 'Michael Keiser', 'Atul Butte', 'Marina Sirota', 'Hani Goodarzi', '32036252', '32042149', '30727954', '33232663', '33765435', '33242416', '31395880', '31486345', 'Michael McManus', 'Charles Chiu', '32025019']
    assert len(luke) == 30

    # Test traversal starting from 'Michael Keiser'
    michael = graph.bfs('Michael Keiser')
    assert michael == ['Michael Keiser', '33232663', 'Charles Chiu', 'Martin Kampmann', '33242416', '33483487', '32790644', '31806696', '31626775', '31540829', 'Atul Butte', 'Luke Gilbert', 'Steven Altschuler', 'Lani Wu', 'Neil Risch', 'Nevan Krogan', '33765435', '31395880', '30944313', '32036252', '32042149', '30727954', '29700475', '34272374', '32353859', 'Marina Sirota', 'Hani Goodarzi', 'Michael McManus', '31486345', '32025019']
    assert len(michael) == 30

    # Test traversal starting from 'Marina Sirota'
    marina = graph.bfs('Marina Sirota')
    assert marina == ['Marina Sirota', '31486345', 'Michael Keiser', '33232663', 'Charles Chiu', 'Martin Kampmann', '33242416', '33483487', '32790644', '31806696', '31626775', '31540829', 'Atul Butte', 'Luke Gilbert', 'Steven Altschuler', 'Lani Wu', 'Neil Risch', 'Nevan Krogan', '33765435', '31395880', '30944313', '32036252', '32042149', '30727954', '29700475', '34272374', '32353859', 'Hani Goodarzi', 'Michael McManus', '32025019']
    assert len(marina) == 30

    # Test traversal starting from an invalid start node
    with pytest.raises(ValueError, match="Start node invalid."):
        graph.bfs('InvalidNode')

    # Test traversal on an empty graph
    empty_graph = Graph('data/blank_network.adjlist')
    with pytest.raises(ValueError, match="The graph is empty."):
        empty_graph.bfs('Luke Gilbert')

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file
    and assert that nodes that are connected return
    a (shortest) path between them.

    Include an additional test for nodes that are not connected
    which should return None.
    """
    graph = Graph('data/citation_network.adjlist')

    # Test shortest path from Luke to Hani
    obs_luke = graph.bfs('Luke Gilbert', 'Hani Goodarzi')
    assert obs_luke == ['Luke Gilbert', '33859415', 'Hani Goodarzi']

    # Test shortest path from Lani Wu to Marina Sirota
    obs_lani = graph.bfs('Lani Wu', 'Marina Sirota')
    assert obs_lani == ['Lani Wu', '30478424', 'Sourav Bandyopadhyay', '30944313', 'Marina Sirota']

    # Test nodes that are not connected
    not_connect = graph.bfs('34533455', 'Marina Sirota')
    assert not_connect == "None"

    # Test invalid end node
    with pytest.raises(ValueError, match="End node invalid."):
        graph.bfs('Luke Gilbert', 'InvalidNode')
