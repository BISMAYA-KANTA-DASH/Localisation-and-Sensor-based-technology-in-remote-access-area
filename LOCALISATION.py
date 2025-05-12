import numpy as np
import matplotlib.pyplot as plt
A = np.array([1, 1])  # Bottom-left
B = np.array([5, 1])  # Bottom-right
C = np.array([4, 4])  # Top-right
D = np.array([2, 4])  # Top-left
def is_inside_trapezium(x, y):
    P = np.array([x, y])
    AB = B - A
    AD = D - A
    AP = P - A
    BC = C - B
    BD = D - B
    BP = P - B
    
    return (0 <= np.dot(AP, AB) <= np.dot(AB, AB) and
            0 <= np.dot(AP, AD) <= np.dot(AD, AD)) or \
           (0 <= np.dot(BP, BC) <= np.dot(BC, BC) and
            0 <= np.dot(BP, BD) <= np.dot(BD, BD))
num_points = 50
x_min, x_max = A[0], C[0]
y_min, y_max = A[1], C[1]
points = []
while len(points) < num_points:
    x_rand = np.random.uniform(x_min, x_max)
    y_rand = np.random.uniform(y_min, y_max)
    if is_inside_trapezium(x_rand, y_rand):
        points.append((x_rand, y_rand))
points = np.array(points)
plt.figure(figsize=(6, 6))
plt.fill([A[0], B[0], C[0], D[0]], [A[1], B[1], C[1], D[1]], 'lightblue', alpha=0.5, label='Trapezium')
plt.scatter(points[:, 0], points[:, 1], color='red', label='Random Points')
plt.legend()
plt.xlim(0, 6)
plt.ylim(0, 5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Random Points Inside a Trapezium')
plt.grid()
plt.show()
