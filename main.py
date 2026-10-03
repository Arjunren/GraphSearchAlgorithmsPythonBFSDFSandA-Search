from collections import deque
import heapq


graph = {
    "A": {"B": 1, "C": 4},
    "B": {"D": 2, "E": 5},
    "C": {"F": 3},
    "D": {"G": 4},
    "E": {"G": 2},
    "F": {"G": 1},
    "G": {}
}


heuristic = {
    "A": 7,
    "B": 6,
    "C": 4,
    "D": 4,
    "E": 2,
    "F": 1,
    "G": 0
}


# BFS

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        current_node, path = queue.popleft()

        if current_node == goal:
            return path

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


# DFS 

def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        current_node, path = stack.pop()

        if current_node == goal:
            return path

        if current_node in visited:
            continue

        visited.add(current_node)

        # reversed() keeps traversal order easier to follow
        for neighbor in reversed(list(graph[current_node].keys())):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None


# A* SEARCH

def a_star(graph, heuristic, start, goal):
    # Priority queue contains:
    # (f_score, g_score, current_node, path)
    priority_queue = [(heuristic[start], 0, start, [start])]

    # Stores the cheapest known cost to each node
    best_cost = {start: 0}

    while priority_queue:
        f_score, g_score, current_node, path = heapq.heappop(
            priority_queue
        )

        if current_node == goal:
            return path, g_score

        # Skip outdated queue entries
        if g_score > best_cost.get(current_node, float("inf")):
            continue

        for neighbor, edge_cost in graph[current_node].items():
            new_g_score = g_score + edge_cost

            if new_g_score < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_g_score

                new_f_score = (
                    new_g_score + heuristic[neighbor]
                )

                heapq.heappush(
                    priority_queue,
                    (
                        new_f_score,
                        new_g_score,
                        neighbor,
                        path + [neighbor]
                    )
                )

    return None, float("inf")


# =========================
# MAIN PROGRAM
# =========================

start_node = "A"
goal_node = "G"

print("Start Node:", start_node)
print("Goal Node:", goal_node)

print("\n--- BFS ---")
bfs_path = bfs(graph, start_node, goal_node)

if bfs_path:
    print("Path:", " -> ".join(bfs_path))
else:
    print("No path found.")


print("\n--- DFS ---")
dfs_path = dfs(graph, start_node, goal_node)

if dfs_path:
    print("Path:", " -> ".join(dfs_path))
else:
    print("No path found.")


print("\n--- A* Search ---")
astar_path, astar_cost = a_star(
    graph,
    heuristic,
    start_node,
    goal_node
)

if astar_path:
    print("Path:", " -> ".join(astar_path))
    print("Total Cost:", astar_cost)
else:
    print("No path found.")