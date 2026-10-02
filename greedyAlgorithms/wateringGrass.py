while True:
  try:
    n, l, w = map(int, input().strip().split())
    
    
    sprinklers = []
    for i in range(n):
      x, r = map(int, input().strip().split())
      sprinklers.append((x,r))
    
    # Sorting the sprinklers on their radius, from biggest to smallest radius
    sprinklers.sort(reverse=True, key=lambda sprinkler: sprinkler[1])
    print(sprinklers)
  except EOFError:
    break