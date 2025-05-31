# N, M = map(int, input("Введите через пробел количество вершин и ребер:").split())  # количество вершин - N, количество ребер - M
#
# start = input("Введите номер вершины, от которой будет произведен обход")
#
#
# Graph = {}
# for i in range(M):
#     v1, v2 = input(f"Введите через пробел {i}-ое ребро графа:").split()
#     if v1 not in Graph and v2 not in Graph:
#         Graph[v1], Graph[v2] = set(v2), set(v1)
#     elif v1 not in Graph:
#         Graph[v1] = set(v2)
#         Graph[v2].add(v1)
#     elif v2 not in Graph:
#         Graph[v2] = set(v1)
#         Graph[v1].add(v2)
#     else:
#         Graph[v1].add(v2)
#         Graph[v2].add(v1)


# связный граф
# N = 7
# M = 9
# start = '2'
# Graph = {'0': {'4', '2', '1'},
#          '1': {'0', '5', '2'},
#          '2': {'0', '5', '3', '1'},
#          '3': {'2'},
#          '4': {'0', '6'},
#          '5': {'6', '2', '1'},
#          '6': {'4', '5'}}


# несвязный граф
N = 13
M = 16
start = '2'
Graph = {'0': {'4', '2', '1'},
         '1': {'5', '0', '2'},
         '2': {'5', '0', '3', '1'},
         '3': {'2'},
         '4': {'6', '0'},
         '5': {'6', '2', '1'},
         '6': {'5', '4'},
         '7': {'9', '12'},
         '8': {'12', '10'},
         '9': {'7', '11'},
         '10': {'8', '11'},
         '11': {'12', '10', '9'},
         '12': {'7', '8', '11'}}



visited = []
queue = []
all_visited = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0)
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

bfs(visited, Graph, start)

all_visited.append(visited)

for i in range(N):
    if len(all_visited) == 1:
        all_node = all_visited[0]
    else:
        all_node = all_visited[0] + all_visited[1]
    if str(i) not in all_node:
        print()
        visited1 = []
        bfs(visited1, Graph, str(i))
        all_visited.append(visited1)

# print(Graph)
