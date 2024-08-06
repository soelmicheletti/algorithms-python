import data_structures.avl_tree
import data_structures.binary_search_tree
import data_structures.hash_map
import data_structures.heap_sort
import data_structures.max_heap
import data_structures.trie
import data_structures.union_find
import graphs.boruvka
import graphs.connectivity
import graphs.bellman_ford
import graphs.bfs
import graphs.bfs_shortest_path
import graphs.dijkstra
import graphs.dfs
import graphs.euler
import graphs.floyd_warshall
import graphs.kruskal
import graphs.prim
import graphs.topo_sort
import heapq
import pytest
import random
import searching.binary_search
import searching.exponential_search
import searching.interpolation_search
import searching.linear_search
import searching.pattern_matching
import sorting.bubble_sort
import sorting.heap_sort
import sorting.insertion_sort
import sorting.merge_sort
import sorting.quick_sort
import sorting.selection_sort
from typing import List

def test_graphs():
    G = [[1], [2], []]
    assert graphs.topo_sort.topo_sort(G) == [0, 1, 2]
    G = [[1], [2], [0]]
    with pytest.raises(ValueError):
        graphs.topo_sort.topo_sort(G)
    print("\t Topological sorting tests passed succesfully!")

    G = [[1, 9], [2], [3, 8], [4], [5], [6], [7], [3, 5], [0, 1], [10], [11], [9]]
    articulation_node, low, bridges = graphs.connectivity.articulation(G)
    assert low == [1, 1, 1, 4, 4, 4, 4, 4, 1, 10, 10, 10]
    assert articulation_node == [True, False, False, True, False, False, False, False, False, True, False, False]
    assert bridges == [[0, 9], [2, 3]]
    print("\t Articulation nodes and bridges tests passed succesfully!")

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

    G = [[(2, 1)], [], [(4, 1), (3, 5)], [(4, 3)], [(3, 30)]]
    assert graphs.dijkstra.dijkstra(G, 0) == [0, 100000, 1, 6, 2]
    print("\t Dijkstra tests passed succesfully!")

    G = [[(2, 1)], [], [(4, 1), (3, -5)], [(4, 30)], [(3, 30)]]
    assert graphs.bellman_ford.bellman_ford(G, 0) == [0, 100000, 1, -4, 2]
    G[4].append((0, -10))
    with pytest.raises(ValueError):
        graphs.bellman_ford.bellman_ford(G, 0)
    print("\t Bellman Ford tests passed succesfully!")

    G = [[0, 3, 8, 0, -4], [0, 0, 0, 1, 7], [0, 4, 0, 0, 0], [2, 0, -5, 0, 0], [0, 0, 0, 6, 0]]
    d = [[0, 1, -3, 2, -4], [3, 0, -4, 1, -1], [7, 4, 0, 5, 3], [2, -1, -5, 0, -2], [8, 5, 1, 6, 0]]
    assert d == graphs.floyd_warshall.floy_warshall(G)
    print("\t Floyd Warshall tests passed succesfuly!")

    G = [[1, 2, 3, 4], [0, 2], [0, 1], [0, 4], [0, 3]]
    assert graphs.euler.eulerian_circuit(G) == [0, 3, 4, 0, 1, 2, 0]
    print("\t Eulerian circuit tests passed succesfully!")

    G = [[(1, 1), (2, 9), (5, 14)], [(0, 1), (2, 10), (3, 15)], [(5, 2), (0, 9), (1, 10), (3, 11)], [(4, 6), (2, 11), (1, 15)], [(5, 9), (3, 6)], [(4, 9), (0, 14), (2, 2)]]
    assert graphs.prim.prim(G) == 27
    print("\t Prim tests passed succesfully!")

    assert graphs.kruskal.kruskal(G) == 27
    print("\t Kruskal tests passed succesfully!")

    assert graphs.boruvka.boruvka(G) == 27
    print("\t Boruvka test passed successfully!")


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
    assert searching.pattern_matching.kmp("ABABCABAB", "ABABDABACDABABCABAB") == [10]
    print("\t Knuth-Morris-Pratt test succedeed")

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

    M = data_structures.hash_map.HashMap()
    M.add(1, 3)
    M.add(2, 3)
    M.add(3, 3)
    M.add(1, 5)
    assert M.find(3) == 3
    assert M.find(1) == 5

    L = [5, 1, 2, 9, 0]
    bst = None
    for l in L: bst = data_structures.binary_search_tree.insert(bst, l)
    assert data_structures.binary_search_tree.pre_order(bst) == "5 (1 (0 (None) (None)) (2 (None) (None))) (9 (None) (None))"
    for l in L:
        assert data_structures.binary_search_tree.search(bst, l)
    assert not data_structures.binary_search_tree.search(bst, -1)
    bst = data_structures.binary_search_tree.delete(bst, 5)
    assert data_structures.binary_search_tree.pre_order(bst) == "9 (1 (0 (None) (None)) (2 (None) (None))) (None)"
    bst = data_structures.binary_search_tree.delete(bst, 9)
    assert data_structures.binary_search_tree.pre_order(bst) == "1 (0 (None) (None)) (2 (None) (None))"
    assert not data_structures.binary_search_tree.search(bst, 5)
    assert not data_structures.binary_search_tree.search(bst, 9)
    print("\t Binary search tree succeeded")

    nodes = [data_structures.union_find.make_set(i) for i in range(7)]
    data_structures.union_find.union(nodes[0], nodes[1])
    data_structures.union_find.union(nodes[2], nodes[1])
    data_structures.union_find.union(nodes[1], nodes[6])
    data_structures.union_find.union(nodes[3], nodes[4])
    data_structures.union_find.union(nodes[4], nodes[5])
    data_structures.union_find.union(nodes[0], nodes[5])
    for node in nodes:
        data_structures.union_find.find(node).val == 5
    print("\t Union find succeeded")

    trie = data_structures.trie.Trie()
    trie.insert("apple")
    assert trie.search("apple")
    assert not trie.search("app")
    assert trie.startsWith("app")
    print("\t Trie tests succeeded")

    T = data_structures.avl_tree.AVL()
    T.add(1)
    T.add(2)
    T.add(3)
    assert T.pre_order() == "2{1{}{}}{3{}{}}"
    T.add(0)
    assert T.pre_order() == "2{1{0{}{}}{}}{3{}{}}"
    T.add(4)
    T.add(5)
    T.add(7)
    T.add(8)
    T.add(6)
    assert T.pre_order() == "2{1{0{}{}}{}}{5{4{3{}{}}{}}{7{6{}{}}{8{}{}}}}"
    for i in range(9):
        assert T.search(i)
    assert not T.search(3.4)
    print("\t AVL tree tests succeeded")


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