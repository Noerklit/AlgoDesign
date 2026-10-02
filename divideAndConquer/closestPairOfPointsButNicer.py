import math

n = int(input().strip())
points = []
closest_pair_dist = 999999

for i in range(n):
  x, y = map(float, input().strip().split())
  points.append((x, y))

if len(points) <= 3:
  for i in range(len(points)):
    p1 = points[i]
    for j in range(len(points)):
      p2 = points[j]
      if i != j:
        dist = math.dist(p1, p2)
        if dist < closest_pair_dist:
          closest_pair_dist = dist
          closest_pair = p1, p2 

points.sort()
L: list = points[: n // 2]
R: list = points[n // 2 :]
print("Here is L", L)
print("Here is R", R)





