import graphs.bfs

def test_graphs():
    # Undirected graphs with thre connected components
    undirected_graph = [[1], [0, 4], [5, 6, 7], [], [1], [2, 6, 7], [2, 5, 7], [2, 5, 6]]

    assert graphs.bfs.bfs(undirected_graph, 0) == [True, True, False, False, True, False, False, False]
    assert graphs.bfs.bfs(undirected_graph, 3) == [False, False, False, True, False, False, False, False]
    assert graphs.bfs.bfs(undirected_graph, 6) == [False, False, True, False, False, True, True, True]
    print("BFS tests passed succesfully!")

if __name__ == "__main__":
    test_graphs()