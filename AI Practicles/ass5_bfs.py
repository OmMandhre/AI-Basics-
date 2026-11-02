# bfs for robot path planning
from collections import deque


def bfs_path(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    frontier = deque([start])
    came_from = {start: None}

    while frontier:
        current = frontier.popleft()

        if current == goal:
            break

        r, c = current

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)

            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and grid[nr][nc] == 0
                and neighbor not in came_from
            ):
                frontier.append(neighbor)
                came_from[neighbor] = current

    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = came_from.get(node)

    path.reverse()

    return path if path and path[0] == start else None


grid = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [1, 0, 0, 0]
]

path = bfs_path(grid, (0, 0), (3, 3))

print("Shortest path found using BFS:")
print(path)

if path:
    print("Number of moves:", len(path) - 1)
else:
    print("No path exists.")
