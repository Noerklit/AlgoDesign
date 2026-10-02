n, m = map(int, input().strip().split())

adj = [[]for _ in range(n +1)]

for i in range(m):
  s,t,c = map(int, input().strip().split())
  adj[s].append((t, c))
  
max_path = [-1 for _ in range(n + 1)]

def get_max_path(u):
  if max_path[u] != -1:
    return max_path[u]
  
  best = 0
  for neighbor, weight in adj[u]:
    print("Neighbor ", neighbor)
    print("weight ", weight)
    score = weight + get_max_path(neighbor)
    print("Calculated score ", score)
    if score > best:
      print("The best that was beaten ", best)
      best = score
  
  max_path[u] = best
  return max_path[u]

ans = 0
for i in range(1, n + 1):
  ans = max(ans, get_max_path(i))

print(ans)