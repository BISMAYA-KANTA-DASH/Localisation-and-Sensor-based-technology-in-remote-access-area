import random
import matplotlib.pyplot as plt

def generate_random_points_in_trapezium(bottom_base, top_base, height, num_rows, num_cols):
    """
    Generate random points within each grid cell of a trapezium.
    """
    points = []
    step_y = height / num_rows

    for i in range(num_rows):
        current_base = bottom_base - i * (bottom_base - top_base) / num_rows
        step_x = current_base / num_cols
        start_x = (bottom_base - current_base) / 2  # Center-align the row

        for j in range(num_cols):
            x = random.uniform(start_x + j * step_x, start_x + (j + 1) * step_x)
            y = random.uniform(i * step_y, (i + 1) * step_y)
            points.append((x, y))

    return points


def generate_anchor_points(bottom_base, top_base, height, num_rows, num_cols):
    """
    Generate anchor points in a grid structure over the trapezium.
    """
    step_y = height / num_rows
    anchors = []

    for i in range(num_rows + 1):
        current_base = bottom_base - i * (bottom_base - top_base) / num_rows
        step_x = current_base / num_cols
        start_x = (bottom_base - current_base) / 2  # Center-align the row

        for j in range(num_cols + 1):
            x = start_x + j * step_x
            y = i * step_y
            anchors.append((x, y))

    return anchors


def plot_trapezium_with_grid(bottom_base, top_base, height, num_rows, num_cols, points, anchors):
    """
    Plot the trapezium with grid lines, sensors, and anchors.
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_aspect('equal')

    trapezium = [
        (0, 0),
        (bottom_base, 0),
        ((bottom_base - top_base) / 2 + top_base, height),
        ((bottom_base - top_base) / 2, height),
    ]

    # Draw the trapezium outline
    ax.add_patch(plt.Polygon(trapezium, fill=False, linestyle="--", edgecolor="black"))

    # Draw grid lines
    step_y = height / num_rows
    for i in range(num_rows + 1):
        current_base = bottom_base - i * (bottom_base - top_base) / num_rows
        step_x = current_base / num_cols
        start_x = (bottom_base - current_base) / 2

        # Draw horizontal lines
        if i < num_rows:
            ax.plot(
                [start_x, start_x + current_base], [i * step_y, i * step_y], color="gray", linestyle="--"
            )

        # Draw vertical lines
        for j in range(num_cols + 1):
            x = start_x + j * step_x
            if i < num_rows:
                next_base = bottom_base - (i + 1) * (bottom_base - top_base) / num_rows
                next_step_x = next_base / num_cols
                next_start_x = (bottom_base - next_base) / 2
                ax.plot(
                    [x, next_start_x + j * next_step_x],
                    [i * step_y, (i + 1) * step_y],
                    color="gray",
                    linestyle="--",
                )

    # Plot sensors (points)
    px, py = zip(*points)
    ax.scatter(px, py, color="blue", label="Sensors")

    # Plot anchors
    ax.scatter(*zip(*anchors), color="red", label="Anchors", marker="x")

    ax.legend()
    ax.set_title("Trapezium with Grid, Sensors, and Anchors")
    plt.show()


# Parameters
bottom_base = 20
top_base = 10
height = 15
num_rows = 6
num_cols = 6

# Generate random points (sensors) in the trapezium
points = generate_random_points_in_trapezium(bottom_base, top_base, height, num_rows, num_cols)

# Generate anchors in a grid structure
anchors = generate_anchor_points(bottom_base, top_base, height, num_rows, num_cols)

# Plot trapezium with grid, sensors, and anchors
plot_trapezium_with_grid(bottom_base, top_base, height, num_rows, num_cols, points, anchors)
