import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
def generate_sensors(num_sensors, radius=10):
    sensors = []
    for _ in range(num_sensors - 1):
        r = np.sqrt(np.random.uniform(0, 1)) * radius
        theta = np.random.uniform(0, 2 * np.pi)
        x, y = r * np.cos(theta), r * np.sin(theta)
        sensors.append([x, y])
    r_out = np.random.uniform(radius * 1.2, radius * 1.8)
    theta_out = np.random.uniform(0, 2 * np.pi)
    x_out, y_out = r_out * np.cos(theta_out), r_out * np.sin(theta_out)
    sensors.append([x_out, y_out])
    
    return np.array(sensors)

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
def connect_sensors(sensors):
    G = nx.DiGraph()
    for i, sensor in enumerate(sensors):
        G.add_node(i, pos=sensor)
    
    visited = set()
    queue = [0]
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
    outside_index = len(sensors) - 1
    inside_distances = [(i, euclidean_distance(sensors[outside_index], sensors[i])) for i in range(len(sensors) - 1)]
    inside_distances.sort(key=lambda x: x[1])
    if len(inside_distances) >= 2:
        G.add_edge(outside_index, inside_distances[0][0])
        G.add_edge(outside_index, inside_distances[1][0])
    
    return G
def plot_network(G, sensors, radius=10):
    pos = nx.get_node_attributes(G, 'pos')
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, with_labels=True, node_size=300, node_color='skyblue', edge_color='gray', font_size=10, arrows=True)
    circle = plt.Circle((0, 0), radius, color='r', fill=False, linestyle='dashed')
    plt.gca().add_patch(circle)
    
    plt.xlim(-radius * 1.8, radius * 1.8)
    plt.ylim(-radius * 1.8, radius * 1.8)
    plt.title("Directed Remote Area Sensor Network")
    plt.show()
num_sensors = 50
sensors = generate_sensors(num_sensors)
G = connect_sensors(sensors)
plot_network(G, sensors)
