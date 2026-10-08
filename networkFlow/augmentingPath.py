n, m, s, t = map(int, input().split())

residual_graph = {i: {} for i in range(n)}

for i in range(m):
  u, v, c, f = map(int, input().split())
  
  for _ in range(m):
    # Forward edge: if flow < capacity, residual capacity is (c - f)
    if f < c:
      # In case multiple edges exist, keep max capacity or accumulate
      residual_graph[u][v] = c - f

    # Backward edge: if flow > 0, residual capacity is f
    if f > 0:
      residual_graph[v][u] = f

def BFS( s, t, parent, residual_graph, n):
  visited = [False]*n
  queue = []
  queue.append(s)
  visited[s] = True
  
  while queue:
    u = queue.pop(0)
    for v, res_cap in residual_graph[u].items():
      if not visited[v] and res_cap > 0:
        queue.append(v)
        visited[v] = True
        parent[v] = u
        if v == t:
          return True
  
  return False

def FordFulkerson(source, sink):
  parent = 
      
      

print(residual_graph)