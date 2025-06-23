import heapq
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge("A", "B", weight=1)
G.add_edge("B", "C", weight=2)
G.add_edge("C", "D", weight=3)


def dijkstra(graph, start):
    shortest_paths = {vertex: float("infinity") for vertex in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > shortest_paths[current_vertex]:
            continue
        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor].get("weight", 1)
            distance = current_distance + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return shortest_paths


all_shortest_paths = {}
for node in G.nodes:
    all_shortest_paths[node] = dijkstra(G, node)

print(all_shortest_paths)
