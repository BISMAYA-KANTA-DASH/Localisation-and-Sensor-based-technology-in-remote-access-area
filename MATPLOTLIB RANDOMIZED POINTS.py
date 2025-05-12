import random
import matplotlib.pyplot as plt
import mplcursors

def generate_random_points(square_size, num_points):
    """
    Generate random points within the outermost square.
    """
    points = [(random.uniform(0, square_size), random.uniform(0, square_size)) for _ in range(num_points)]
    return points

def construct_concentric_squares(center, max_side_length, num_squares):
    """
    Define concentric squares with specified side lengths.
    """
    step = max_side_length / num_squares
    side_lengths = [step * (i + 1) for i in range(num_squares)]
    return side_lengths

def assign_points_to_squares(points, center, side_lengths):
    """
    Assign points to the corresponding concentric square.
    """
    assignments = {i: [] for i in range(len(side_lengths))}

    for px, py in points:
        distance_x = abs(px - center[0])
        distance_y = abs(py - center[1])

        # Find the square where the point lies
        for idx, side_length in enumerate(side_lengths):
            half_side = side_length / 2
            if distance_x <= half_side and distance_y <= half_side:
                assignments[idx].append((px, py))
                break
    return assignments

def select_points_from_squares(assignments):
    """
    Randomly select one point from each square with points.
    """
    selected_points = []
    for points in assignments.values():
        if points:
            selected_points.append(random.choice(points))
    return selected_points

def plot_points(square_size, points, title):
    """
    Plot only the randomized points.
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, square_size)
    ax.set_ylim(0, square_size)
    ax.set_aspect('equal')

    x, y = zip(*points)
    ax.scatter(x, y, color='blue', label='Randomized Points')
    ax.set_title(title)
    ax.legend()
    plt.show()

def plot_points_and_squares(square_size, points, center, side_lengths=None, selected_points=None, iteration=None):
    """
    Plot points, concentric squares, and selected points.
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, square_size)
    ax.set_ylim(0, square_size)
    ax.set_aspect('equal')

    # Plot all points
    x_all, y_all = zip(*points)
    scatter_all = ax.scatter(x_all, y_all, color='blue', label='Randomized Points')

    # Plot concentric squares
    if side_lengths:
        for side_length in side_lengths:
            half_side = side_length / 2
            bottom_left = (center[0] - half_side, center[1] - half_side)
            square = plt.Rectangle(bottom_left, side_length, side_length, color='gray', fill=False, linestyle='--')
            ax.add_artist(square)

    # Plot selected points
    scatter_sel = None
    if selected_points:
        x_sel, y_sel = zip(*selected_points)
        scatter_sel = ax.scatter(x_sel, y_sel, color='red', label='Selected Points', s=100)

    # Title and legend
    title = f'Iteration {iteration}' if iteration else 'Concentric Squares with Points'
    ax.set_title(title)
    ax.legend()

    plt.show()
    return scatter_all, scatter_sel
def plot_all_iterations(selected_coords, square_size, num_iterations):
    """
    Plot the selected points from all iterations in a single graph as a line plot.
    Each line represents one iteration.
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, square_size)
    ax.set_ylim(0, square_size)
    ax.set_aspect('equal')

    # Plot the selected points from each iteration as a line graph
    for iteration, points in enumerate(selected_coords, 1):
        x, y = zip(*[tuple(map(float, coord.strip("()").split(","))) for coord in points])
        ax.plot(x, y, marker='o', label=f"Iteration {iteration}")

    # Title, labels, and legend
    ax.set_title("Selected Points Across Iterations")
    ax.set_xlabel("X-Coordinate")
    ax.set_ylabel("Y-Coordinate")
    ax.legend()
    plt.show()

# Parameters
square_size = 10  # Size of the outermost square
center = (square_size / 2, square_size / 2)  # Center of the concentric squares
num_points = random.randint(500, 1000)  # Total random points
max_side_length = square_size  # Side length of the outermost square
num_squares = 5  # Number of concentric squares

# Step 1: Generate random points
points = generate_random_points(square_size, num_points)
plot_points(square_size, points, title='Randomized Points')  # First figure with only randomized points

# Step 2: Define concentric squares
side_lengths = construct_concentric_squares(center, max_side_length, num_squares)

# Step 2.1: Plot concentric squares along with randomized points (Second figure)
plot_points_and_squares(square_size, points, center, side_lengths, iteration='Concentric Squares')

# Step 3: Assign points to squares
assignments = assign_points_to_squares(points, center, side_lengths)

# Step 4: Iteratively select points and visualize for 5 iterations
selected_coords = []  # List to store selected coordinates for each iteration
for i in range(1, 7):  # 5-6 iterations
    selected_points = select_points_from_squares(assignments)
    scatter_all, scatter_sel = plot_points_and_squares(square_size, points, center, side_lengths, selected_points, iteration=i)

    # Add hover functionality to selected points to show their coordinates
    mplcursors.cursor(scatter_sel, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"Selected: ({sel.target[0]:.2f}, {sel.target[1]:.2f})"))

    # Store the selected coordinates for this iteration
    selected_coords.append([f"({x:.2f}, {y:.2f})" for x, y in selected_points])
plot_all_iterations(selected_coords, square_size, len(selected_coords))
# Display the selected coordinates after all iterations
print("Selected coordinates for each iteration:")
for idx, coords in enumerate(selected_coords, 1):
    print(f"Iteration {idx}: {', '.join(coords)}")
