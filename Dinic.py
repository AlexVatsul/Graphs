from collections import defaultdict, deque

class DinicMaxFlow:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph)
        self.level = [0] * self.V

    def bfs(self, s, t):
        self.level = [-1] * self.V
        self.level[s] = 0
        queue = deque([s])

        while queue:
            u = queue.popleft()
            for v, capacity in enumerate(self.graph[u]):
                if self.level[v] < 0 and capacity > 0:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)

        return self.level[t] >= 0

    def dfs(self, u, t, flow):
        if u == t:
            return flow

        for v, capacity in enumerate(self.graph[u]):
            if capacity > 0 and self.level[v] == self.level[u] + 1:
                bottleneck = min(flow, capacity)
                partial_flow = self.dfs(v, t, bottleneck)

                if partial_flow > 0:
                    self.graph[u][v] -= partial_flow
                    self.graph[v][u] += partial_flow
                    return partial_flow

        return 0

    def dinic_max_flow(self, source, sink):
        max_flow = 0

        while self.bfs(source, sink):
            while True:
                flow = self.dfs(source, sink, float('inf'))
                if flow == 0:
                    break
                max_flow += flow

        return max_flow

# Пример использования
if __name__ == "__main__":
    # N = int(input("Введите количество вершин: "))
    # graph = [[0] * N for _ in range(N)]
    #
    # for u in range(N):
    #     for v in range(N):
    #         if u != v:
    #             capacity = int(input(f"Введите вес связи между вершинами {u} и {v}: "))
    #             graph[u][v] = capacity

    graph = [[0, 4, 3, 7, 1, 10],
             [4, 0, 9, 0, 0, 0],
             [3, 9, 0, 12, 0, 0],
             [7, 0, 12, 0, 6, 0],
             [1, 0, 0, 6, 0, 3],
             [10, 0, 0, 0, 3, 0]]

    source = int(input("Введите вершину-источник: "))
    sink = int(input("Введите вершину-сток: "))

    dinic = DinicMaxFlow(graph)
    max_flow = dinic.dinic_max_flow(source, sink)
    print("Максимальный поток:", max_flow)
