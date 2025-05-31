class FordFulkerson:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph)
        self.parent = [-1] * self.V

    def bfs(self, s, t):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for v, capacity in enumerate(self.graph[u]):
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    self.parent[v] = u

        return visited[t]

    def ford_fulkerson(self, source, sink):
        max_flow = 0

        while self.bfs(source, sink):
            path_flow = float('inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.graph[self.parent[s]][s])
                s = self.parent[s]

            max_flow += path_flow
            v = sink

            while v != source:
                u = self.parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = self.parent[v]

        return max_flow

# Пример использования
if __name__ == "__main__":

    # # Считываем количество вершин N
    # N = int(input("Введите количество вершин: "))
    #
    # # Инициализируем пустой граф с N вершинами
    # graph = [[0] * N for _ in range(N)]
    #
    # # Считываем веса связей между вершинами
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


    ff = FordFulkerson(graph)
    max_flow = ff.ford_fulkerson(source, sink)
    print("Максимальный поток:", max_flow)
