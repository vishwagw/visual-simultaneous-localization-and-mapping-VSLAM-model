import matplotlib.pyplot as plt
import numpy as np

def plot_drone_path(positions, title="Drone Path"):
    plt.figure(figsize=(10, 6))
    plt.plot(positions[:, 0], positions[:, 1], marker='o', color='b', label='Drone Path')
    plt.title(title)
    plt.xlabel('X Position (m)')
    plt.ylabel('Y Position (m)')
    plt.grid()
    plt.legend()
    plt.axis('equal')
    plt.show()

def plot_map(landmarks, title="3D Map"):
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(landmarks[:, 0], landmarks[:, 1], landmarks[:, 2], c='r', marker='o', label='Landmarks')
    ax.set_title(title)
    ax.set_xlabel('X Position (m)')
    ax.set_ylabel('Y Position (m)')
    ax.set_zlabel('Z Position (m)')
    ax.legend()
    plt.show()

def visualize_vslam(positions, landmarks):
    plot_drone_path(positions)
    plot_map(landmarks)