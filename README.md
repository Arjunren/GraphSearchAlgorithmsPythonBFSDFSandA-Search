# Graph Search Algorithms in Python

This project demonstrates three common graph search and pathfinding algorithms using Python:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- A* Search

The program searches for a path from **Node A** to **Node G** in a weighted graph.

---

## Project Overview

Graph searching is an important concept in computer science and artificial intelligence. It is used in applications such as:

- Route planning
- GPS navigation
- Network traversal
- Game development
- Artificial intelligence
- Pathfinding systems

This project compares how BFS, DFS, and A* Search explore the same graph.

---

## Graph Structure

The graph used by the program is:

```text
        A
       / \
    1 /   \ 4
     B     C
    / \     \
 2 /   \5    \3
  D     E     F
   \     \   /
   4\    2\ /1
        G
```

The graph is represented in Python using a dictionary:

```python
graph = {
    "A": {"B": 1, "C": 4},
    "B": {"D": 2, "E": 5},
    "C": {"F": 3},
    "D": {"G": 4},
    "E": {"G": 2},
    "F": {"G": 1},
    "G": {}
}
```

Each key represents a node.

The nested dictionary contains neighboring nodes and the cost required to travel to each neighbor.

For example:

```python
"A": {"B": 1, "C": 4}
```

means:

```text
A -> B has a cost of 1
A -> C has a cost of 4
```

---

## Heuristic Values

A* Search uses heuristic values to estimate how close each node is to the goal.

```python
heuristic = {
    "A": 7,
    "B": 6,
    "C": 4,
    "D": 4,
    "E": 2,
    "F": 1,
    "G": 0
}
```

The goal node `G` has a heuristic value of `0` because it has already reached the destination.

A* evaluates nodes using:

```text
f(n) = g(n) + h(n)
```

Where:

- `g(n)` = actual cost from the starting node
- `h(n)` = estimated cost from the current node to the goal
- `f(n)` = estimated total cost

---

## Breadth-First Search

Breadth-First Search explores the graph **level by level**.

The program uses Python's `deque` as a queue:

```python
queue = deque([(start, [start])])
```

BFS removes nodes from the front of the queue:

```python
current_node, path = queue.popleft()
```

New nodes are added to the back of the queue.

Because BFS explores nodes by depth level, it is useful for finding a path with the smallest number of edges in an unweighted graph.

---

## Depth-First Search

Depth-First Search explores one branch of the graph as deeply as possible before backtracking.

The program uses a Python list as a stack:

```python
stack = [(start, [start])]
```

Nodes are removed using:

```python
current_node, path = stack.pop()
```

DFS uses Last-In, First-Out behavior.

The program also uses:

```python
reversed(list(graph[current_node].keys()))
```

to make the traversal order easier to follow based on the graph's insertion order.

---

## A* Search

A* Search considers both:

1. The actual path cost
2. The estimated remaining cost to the goal

A priority queue is implemented using Python's `heapq` module.

Each queue entry contains:

```python
(f_score, g_score, current_node, path)
```

The total estimated score is calculated using:

```python
new_f_score = new_g_score + heuristic[neighbor]
```

The algorithm prioritizes nodes with the smallest `f_score`.

The `best_cost` dictionary stores the cheapest known cost for reaching each node:

```python
best_cost = {start: 0}
```

This prevents more expensive paths from replacing previously discovered cheaper paths.

---

## Program Execution

The program starts searching from:

```python
start_node = "A"
```

and attempts to reach:

```python
goal_node = "G"
```

It then executes each search algorithm:

```python
bfs(graph, start_node, goal_node)

dfs(graph, start_node, goal_node)

a_star(graph, heuristic, start_node, goal_node)
```

---

## Example Output

Running the program produces output similar to:

```text
Start Node: A
Goal Node: G

--- BFS ---
Path: A -> B -> D -> G

--- DFS ---
Path: A -> B -> D -> G

--- A* Search ---
Path: A -> B -> D -> G
Total Cost: 7
```

Depending on graph ordering and heuristic behavior, traversal choices may differ.

---

## Important Difference Between the Algorithms

| Algorithm | Strategy | Uses Edge Cost | Uses Heuristic |
|---|---|---:|---:|
| BFS | Explores level by level | No | No |
| DFS | Explores deeply before backtracking | No | No |
| A* | Chooses nodes using estimated total cost | Yes | Yes |

BFS and DFS use the graph structure to determine traversal order but do not use the numeric edge weights when choosing which path to explore.

A* uses both the edge weights and heuristic values.

---

## Requirements

The project uses Python's standard library only.

Required Python modules:

```python
from collections import deque
import heapq
```

No third-party packages are required.

Recommended Python version:

```text
Python 3.10+
```

---

## How to Run

Clone or download the project.

Navigate to the project folder:

```bash
cd graph-search-algorithms
```

Run the Python program:

```bash
python main.py
```

or:

```bash
python3 main.py
```

---

## Project Structure

```text
graph-search-algorithms/
│
├── main.py
└── README.md
```

---

## Video Explanation

A video explanation of the program is available here:

**Video:** [Watch the Program Explanation](YOUR_VIDEO_URL_HERE)

The video explains:

- The graph structure
- Edge costs
- Heuristic values
- How BFS works
- How DFS works
- How A* Search works
- The differences between the algorithms
- The program output

---

## Technologies Used

- Python
- `collections.deque`
- `heapq`
- Graph data structures
- Search algorithms

---

## Learning Objectives

Through this project, I learned how to:

- Represent a weighted graph in Python
- Implement Breadth-First Search
- Implement Depth-First Search
- Implement A* Search
- Work with queues and stacks
- Use priority queues with `heapq`
- Track visited nodes
- Calculate path costs
- Use heuristic functions
- Compare different graph searching strategies

---

## Author

**Von**

Software / Cloud Engineering

---

**Video:** [Watch the Program Explanation](https://drive.google.com/file/d/1PwOXxjx-3lcwC4gNqemknCIPIlbeZGiy/view?usp=sharing)

---
## License

This project is intended for educational purposes.
