import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Generate random sensor positions within a circular area
def generate_sensors(num_sensors, radius=10):
    angles = np.linspace(0, 2 * np.pi, num_sensors, endpoint=False)
    x = radius * np.cos(angles) + np.random.uniform(-0.5, 0.5, num_sensors)
    y = radius * np.sin(angles) + np.random.uniform(-0.5, 0.5, num_sensors)
    return np.column_stack((x, y))

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Form triangular connections based on parent-child relationships
def connect_sensors(sensors):
    G = nx.Graph()
    for i, sensor in enumerate(sensors):
        G.add_node(i, pos=sensor)
    
    visited = set()
    queue = [0]  # Start with the first sensor
    
    while queue:
        parent = queue.pop(0)
        if parent in visited:
            continue
        visited.add(parent)
        
        distances = [(i, euclidean_distance(sensors[parent], sensors[i])) for i in range(len(sensors)) if i not in visited]
        distances.sort(key=lambda x: x[1])
        
        if len(distances) >= 2:
            child1, child2 = distances[0][0], distances[1][0]
            G.add_edge(parent, child1)
            G.add_edge(parent, child2)
            queue.extend([child1, child2])
    
    return G

# Plot the sensor network
def plot_network(G):
    pos = nx.get_node_attributes(G, 'pos')
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, with_labels=True, node_size=300, node_color='skyblue', edge_color='gray', font_size=10)
    plt.xlim(-12, 12)
    plt.ylim(-12, 12)
    plt.title("Remote Area Sensor Network")
    plt.show()

# Main execution
num_sensors = 50
sensors = generate_sensors(num_sensors)
G = connect_sensors(sensors)
plot_network(G)
