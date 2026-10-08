import itertools

num_vertex, num_edges, source, sink = map(int, input().split())

residual_graph = {i: {} for i in range(num_vertex)}

for _ in range(num_edges):
  u, v, capacity, flow = map(int, input().split())
  
  # Forward edge: if flow < capacity, residual capacity is (c - f)
  if flow < capacity:
    # In case multiple edges exist, keep max capacity or accumulate
    residual_graph[u][v] = capacity - flow

  # Backward edge: if flow > 0, residual capacity is f
  if flow > 0:
    residual_graph[v][u] = flow

def BFS(source, sink, parent, residual_graph, num_vertex):
  visited = [False]*num_vertex
  queue = []
  queue.append(source)
  visited[source] = True
  
  while queue:
    u = queue.pop(0)
    for v, res_cap in residual_graph[u].items():
      if not visited[v] and res_cap > 0:
        queue.append(v)
        visited[v] = True
        parent[v] = u
        if v == sink:
          return True
  
  return False

parent = [-1] * num_vertex
has_path = BFS(source, sink, parent, residual_graph, num_vertex) 

def retrace_path():
  path_taken = []
  path_taken.append(sink)
  child = parent[sink]
  while True:
    if source in path_taken:
      # print("Here is the path taken", path_taken)
      return path_taken
    else:
      # print("Here is a child", child)
      if child in path_taken:
        child = parent[child]
        # print("New child", child)
      else:
        path_taken.append(child)

if not has_path:
  print("impossible")
else:  
  retraced_path = retrace_path()
  retraced_path.reverse()
  vertex_pairs = list(itertools.pairwise(retraced_path))
  bottleneck = float('inf')
  for vertex_pair in vertex_pairs:
    # print(vertex_pair[0], vertex_pair[1])
    test = residual_graph[vertex_pair[0]]
    number = test[vertex_pair[1]]
    # print(test)
    # print(number)
    if number < bottleneck:
      bottleneck = number

  print(bottleneck)
  print(*retraced_path)
  # print(residual_graph)


