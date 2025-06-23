import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex, to_rgb
import numpy as np
from collections import deque


class Node:
    def __init__(self, key, color="#3B0072"):
        self.left: "Node | None" = None
        self.right: "Node | None" = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_tree_from_heap(arr, i=0):
    if i >= len(arr):
        return None
    node = Node(arr[i])
    node.left = build_tree_from_heap(arr, 2 * i + 1)
    node.right = build_tree_from_heap(arr, 2 * i + 2)
    return node


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def get_nodes_in_order(root, method="dfs"):
    order = []
    if method == "dfs":

        def dfs(node):
            if node:
                order.append(node)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
    elif method == "bfs":
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                order.append(node)
                queue.append(node.left)
                queue.append(node.right)
    return order


def generate_gradient_colors(n, start="#4e00b4", end="#7700ff"):
    # start: dark blue, end: light blue
    start_rgb = np.array(to_rgb(start))
    end_rgb = np.array(to_rgb(end))
    colors = [to_hex(start_rgb + (end_rgb - start_rgb) * i / (n - 1)) for i in range(n)]
    return colors


def draw_tree(tree_root, highlight_nodes=None, highlight_colors=None, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = []
    labels = {}
    for node_id, data in tree.nodes(data=True):
        if highlight_nodes and node_id in highlight_nodes:
            idx = highlight_nodes.index(node_id)
            colors.append(highlight_colors[idx])
        else:
            colors.append(data["color"])
        labels[node_id] = data["label"]
    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.title(title)
    plt.show()


def visualize_traversal(root, method="dfs"):
    nodes = get_nodes_in_order(root, method)
    colors = generate_gradient_colors(len(nodes))
    highlight_nodes = [node.id for node in nodes]
    highlight_colors = colors
    draw_tree(
        root, highlight_nodes, highlight_colors, title=f"{method.upper()} traversal"
    )


heap = [0, 4, 1, 5, 10, 3]
root = build_tree_from_heap(heap)

visualize_traversal(root, method="dfs")
visualize_traversal(root, method="bfs")
