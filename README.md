# Algorithms

Python implementation of basic algorithms and data structures. 

![Alt text](/wallpaper.jpg?raw=true "Title")


## Graph Theory

Algorithm  | Goal | Runtime
------------- | ------------- | -------------
[Articulation Nodes](/graphs/connectivity.py)  | Find nodes and bridges to ensure graph connectivity. | **O(n+m)**
[BFS](/graphs/bfs.py)  | Perform Breadth-First-Search on the graph. | **O(n+m)**
[Bellman Ford](/graphs/bellman_ford.py)  | One-to-all shortest path, even with negative weights. | **O(nm)**
[DFS](/graphs/dfs.py)  | Perform Depth-First-Search on the graph. | **O(n+m)**
[Dijkstra](/graphs/dijkstra.py)  | One-to-all shortest path, weights must be non-negative. | **O(n log n + m)** (with Fibonacci-Heaps, this version is less efficient)
[Euler Tour](/graphs/euler.py)  | Decide if the graph contains an Euler Tour. | **O(m)** 
[Floyd Warshall](/graphs/floyd_warshall.py)  | All-to-all shortest path. | **O(n^3)** 
[Kruskal](/graphs/kruskal.py)  | MST by applying the blue rule. | **O(m log m)** 
[Prim](/graphs/prim.py)  | MST by applying the blue/ red rule. | **O(m log n)**
[Boruvka](/graphs/boruvka.py)  | Boruvka'algorithm. It is not the most efficient implementation but it shows the idea. | **O(m log n)**
[Topological Sorting](/graphs/topo_sort.py)  | Determine if the graph has a topological order | **O(n + m)**

## Searching

Algorithm  | Key Idea | Runtime
------------- | ------------- | -------------
[Linear Search](/searching/linear_search.py)  | Check every element. | **O(n)** (worst-case)
[Binary Search](/searching/binary_search.py)  | Searching in a dictionary of a foreign language. | **O(log n)** (worst-case)
[Interpolation Search](/searching/interpolation_search.py)  | Searching in a dictionary when you have an estimate of the words distribution. | **O(log n)** (worst-case)
[Exponential Search](/searching/exponential_search.py)  | Find range and use binary search. | **O(log n)** (worst-case)
[Knuth-Morris-Pratt](/searching/pattern_matching.py) | Find pattern of length m in text of length n using | **O(n+m)** with **O(m)** auxiliary space
## Sorting

Algorithm  | Key Idea | Runtime
------------- | ------------- | -------------
[Bubble Sort](/sorting/bubble_sort.py)  | Double for loop. | **O(n^2)** (worst-case)
[Insertion Sort](/sorting/insertion_sort.py)  | Sorting a deck of card. | **O(n^2)** (worst-case)
[Selection Sort](/sorting/selection_sort.py)  | Pick the maximum of the unsorted part of the array and put it at the end. | **O(n^2)** (worst-case)
[Heap Sort](/sorting/heap_sort.py)  | Selection sort with efficient data structure | **O(n log n)** (worst-case)
[Merge Sort](/sorting/merge_sort.py)  | Divide and conquer. | **O(n log n)** (worst-case)
[Quick Sort](/sorting/quick_sort.py)  | Use a (random) pivot to partition the array. | **O(n log n)** average-case, but **O(n^2)** worst-case

## Data Structures

Data Structure  | Supported Operations 
------------- | -------------
[Binary Search Tree](/data_structures/binary_search_tree.py)  | Add, find, delete: everything **O(h)** (h is the height of the tree)
[Max heap](/data_structures/max_heap.py)  | Enque, Deque: both **O(log n)**
[Queue](/data_structures/queue.py)  | Enque, Deque: both **O(1)** 
[Stack](/data_structures/stack.py)  | Push, Pop, Top: everything **O(1)**
[Segment Treee](/data_structures/segment_tree.py) | Create **O(n)**, find **O(log n)**, update **O(log n)**
[Set](/data_structures/set.py)  | Add, remove, find: everything **O(1)** on average (hashing)
[Trie](/data_structures/trie.py)  | Add and search prefixes efficiently | Find **O(k)**
[Union Find](/data_structures/union_find.py)  | Find, Union: both **O(log n)** using path compression 
