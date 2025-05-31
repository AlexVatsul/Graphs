import heapq

graph = {
    'A': {'B': 1},
    'B': {'A': 1, 'C': 1, 'D': 6},
    'C': {'B': 1, 'G': 1},
    'D': {'B': 6, 'G': 1, 'H': 2},
    'G': {'C': 1, 'D': 1, 'E': 1},
    'E': {'G': 1},
    'H': {'D': 2}
}


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        # Обрабатываем только вершину с наименьшим расстоянием
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Рассматриваем этот новый путь только в том случае, если он лучше любого пути, который мы нашли до сих пор
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


dist = (dijkstra(graph, 'D'))

for value, keys in dist.items():
    print(f"{value} -- {keys}")