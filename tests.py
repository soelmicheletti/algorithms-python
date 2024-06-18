import data_structures.heap_sort
import data_structures.max_heap
import graphs.bfs
import graphs.bfs_shortest_path
import graphs.dfs
import heapq
import random
from typing import List
import searching.binary_search
import searching.exponential_search
import searching.interpolation_search
import searching.linear_search
import sorting.bubble_sort
import sorting.heap_sort
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
    print("\t BFS tests passed succesfully!")

    assert graphs.bfs_shortest_path.bfs_shortest_path(undirected_graph, 0) == [0, 1, -1, -1, 2, -1, -1, -1]
    assert graphs.bfs_shortest_path.bfs_shortest_path(undirected_graph, 3) == [-1, -1, -1, 0, -1, -1, -1, -1]
    assert graphs.bfs_shortest_path.bfs_shortest_path(undirected_graph, 6) == [-1, -1, 1, -1, -1, 1, 0, 1]
    print("\t BFS shortest path tests passed successfully!")

    assert graphs.dfs.dfs(undirected_graph, 0) == [True, True, False, False, True, False, False, False]
    assert graphs.dfs.dfs(undirected_graph, 3) == [False, False, False, True, False, False, False, False]
    assert graphs.dfs.dfs(undirected_graph, 6) == [False, False, True, False, False, True, True, True]
    print("\t DFS tests passed succesfully!")

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
    print("\t Bubble sort succeeded")
    assert is_sorted(sorting.insertion_sort.insertion_sort(unsorted_list))
    print("\t Insertion sort succeeded")
    assert is_sorted(sorting.selection_sort.selection_sort(unsorted_list))
    print("\t Selection sort succeeded")
    assert is_sorted(sorting.merge_sort.merge_sort(unsorted_list))
    print("\t Merge sort succeeded")
    assert is_sorted(data_structures.heap_sort.heap_sort(unsorted_list))
    print("\t Heap sort no input succeeded")
    assert is_sorted(sorting.heap_sort.heap_sort(unsorted_list))
    print("\t Heap sort succeeded")

    unsorted_list = [] # long list to sort
    for _ in range(1000):
        unsorted_list.append(random.randint(1, 1000000))
    assert is_sorted(sorting.quick_sort.quick_sort(unsorted_list))
    print("\t Quick sort succeeded")

def test_searching():
    L = [1, 4, 89, 100, 105]
    
    assert not searching.linear_search.linear_search(L, 5)
    assert searching.linear_search.linear_search(L, 4)
    print("\t Linear search succeeded")
    assert not searching.binary_search.binary_search(L, 5)
    assert searching.binary_search.binary_search(L, 4)
    print("\t Binary search succeeded")
    assert not searching.exponential_search.exponential_search(L, 5)
    assert searching.exponential_search.exponential_search(L, 4)
    print("\t Exponential search succeeded")
    assert not searching.interpolation_search.interpolation_search(L, 5)
    assert searching.interpolation_search.interpolation_search(L, 4)
    print("\t Interpolation search succeeded")

def test_data_structures():
    heap = data_structures.max_heap.MaxHeap()
    L = [17, 3, 19, 25, 36, 100]
    for l in L: heap.insert(l)
    assert heap.arr == [100, 36, 25, 17, 3, 19]
    L_sorted = sorted(L)
    for l in L_sorted[::-1]:
        assert heap.pop() == l
    heap = [-17, -3, -19, -25]
    heapq.heapify(heap)
    heapq.heappush(heap, -36)
    heapq.heappush(heap, -100)
    for l in L_sorted[::-1]:
        assert -heapq.heappop(heap) == l
    print("\t Heap succeeded")

if __name__ == "__main__":
    print("Testing graphs... ")
    test_graphs()
    print("Graph tests COMPLETED!")

    print("Testing searching... ")
    test_searching()
    print("Searching tests COMPLETED!")

    print("Testing sorting...")
    test_sorting()
    print("Sorting tests COMPLETED!")

    print("Testing data structures...")
    test_data_structures()
    print("Data structure tests COMPLETED")