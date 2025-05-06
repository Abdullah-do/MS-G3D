import numpy as np

class Graph:
    def __init__(self, labeling_mode='spatial'):
        self.num_node = 75
        self_link = [(i, i) for i in range(self.num_node)]

        # Pose edges (simplified MediaPipe 33 points)
        pose_edges = [
            (0, 1), (1, 2), (2, 3), (3, 7),
            (0, 4), (4, 5), (5, 6), (6, 8),
            (9, 10), (11, 12), (12, 14), (14, 16),
            (11, 13), (13, 15),
            (23, 24), (24, 26), (26, 28), (28, 32),
            (23, 25), (25, 27), (27, 29), (29, 31)
        ]

        # Hand edges
        hand_edges = []
        for i in range(33, 54 - 1):
            hand_edges.append((i, i + 1))
        for i in range(54, 75 - 1):
            hand_edges.append((i, i + 1))

        # Wrist to hand connection
        hand_edges += [(15, 33), (16, 54)]

        # Final edges
        neighbor_link = pose_edges + hand_edges
        self.edge = self_link + neighbor_link
        self.center = 0

        self.A_binary = self.get_adjacency_matrix()

    def get_adjacency_matrix(self):
        A = np.zeros((self.num_node, self.num_node))
        for i, j in self.edge:
            A[i, j] = 1
            A[j, i] = 1
        return A

    def get_edge(self):
        return self.edge
