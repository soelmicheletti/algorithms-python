import graphs.bfs
import graphs.bfs_shortest_path
import graphs.dfs

def test_graphs():
    # Undirected graphs with thre connected components
    undirected_graph = [[1], [0, 4], [5, 6, 7], [], [1], [2, 6, 7], [2, 5, 7], [2, 5, 6]]

    assert graphs.bfs.bfs(undirected_graph, 0) == [True, True, False, False, True, False, False, False]
    assert graphs.bfs.bfs(undirected_graph, 3) == [False, False, False, True, False, False, False, False]
    assert graphs.bfs.bfs(undirected_graph, 6) == [False, False, True, False, False, True, True, True]
    print("BFS tests passed succesfully!")

    assert graphs.bfs_shortest_path.bfs_shortest_path(undirected_graph, 0) == [0, 1, -1, -1, 2, -1, -1, -1]
    assert graphs.bfs_shortest_path.bfs_shortest_path(undirected_graph, 3) == [-1, -1, -1, 0, -1, -1, -1, -1]
    assert graphs.bfs_shortest_path.bfs_shortest_path(undirected_graph, 6) == [-1, -1, 1, -1, -1, 1, 0, 1]
    print("BFS shortest path tests passed successfully!")

    assert graphs.dfs.dfs(undirected_graph, 0) == [True, True, False, False, True, False, False, False]
    assert graphs.dfs.dfs(undirected_graph, 3) == [False, False, False, True, False, False, False, False]
    assert graphs.dfs.dfs(undirected_graph, 6) == [False, False, True, False, False, True, True, True]
    print("DFS tests passed succesfully!")

if __name__ == "__main__":
    test_graphs()
