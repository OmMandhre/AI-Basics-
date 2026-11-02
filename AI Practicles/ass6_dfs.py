# dfs for water jug problem
def dfs_water_jug(capacity1, capacity2, target):
    # Initial state: both jugs are empty
    start = (0, 0)

    # Keep track of visited states
    visited = {start}

    # Stack stores (current_state, path_taken)
    stack = [(start, [start])]

    while stack:
        # Remove the top element from the stack
        (j1, j2), path = stack.pop()

        # Check if the target amount has been reached
        if j1 == target or j2 == target:
            return path

        # Generate all possible next states
        states = [
            # 1. Fill Jug 1 completely
            (capacity1, j2),

            # 2. Fill Jug 2 completely
            (j1, capacity2),

            # 3. Empty Jug 1
            (0, j2),

            # 4. Empty Jug 2
            (j1, 0),

            # 5. Pour water from Jug 1 into Jug 2
            (
                max(0, j1 - (capacity2 - j2)),
                min(capacity2, j1 + j2)
            ),

            # 6. Pour water from Jug 2 into Jug 1
            (
                min(capacity1, j1 + j2),
                max(0, j2 - (capacity1 - j1))
            )
        ]

        # Add unvisited states to the stack
        for state in states:
            if state not in visited:
                visited.add(state)

                # Add the new state to the current path
                stack.append((state, path + [state]))

    # Return None if no solution exists
    return None


# Jug capacities
capacity1 = 4
capacity2 = 3

# Required target amount
target = 2

# Find the solution using DFS
path = dfs_water_jug(capacity1, capacity2, target)

# Display the solution
if path:
    print("Water Jug Solution Path (DFS):")

    for state in path:
        print(f"Jug1 = {state[0]}L, Jug2 = {state[1]}L")

    print("\nNumber of steps:", len(path) - 1)

else:
    print("No solution found.")
