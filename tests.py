import graphs.bfs
import graphs.bfs_shortest_path
import graphs.dfs
import random
from typing import List
import sorting.bubble_sort
import sorting.insertion_sort
import sorting.merge_sort
import sorting.quick_sort
import sorting.selection_sort

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

def test_sorting():
    random.seed(42) # for reproducibility

    def is_sorted(nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True
    
    unsorted_list = [] # long list to sort
    for _ in range(1000):
        unsorted_list.append(random.randint(1, 10000))
        
    assert is_sorted(sorting.bubble_sort.bubble_sort(unsorted_list))
    print("Bubble sort succeeded")
    assert is_sorted(sorting.insertion_sort.insertion_sort(unsorted_list))
    print("Insertion sort succeeded")
    assert is_sorted(sorting.selection_sort.selection_sort(unsorted_list))
    print("Selection sort succeeded")
    assert is_sorted(sorting.merge_sort.merge_sort(unsorted_list))
    print("Merge sort succeeded")

    unsorted_list = [] # long list to sort
    for _ in range(1000):
        unsorted_list.append(random.randint(1, 1000000))
    assert is_sorted(sorting.quick_sort.quick_sort(unsorted_list))
    print("Quick sort succeeded")

if __name__ == "__main__":
    test_graphs()
    test_sorting()
