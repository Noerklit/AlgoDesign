# This is the quadratic bad solution, but enough to pass
import math

n = int(input().strip())
points = []

for i in range(n):
  x, y = map(float, input().strip().split())
  points.append((x, y))

closest_pair_dist = 999999
closest_pair = []
points.sort()

for i in range(len(points)):
  p1 = points[i]
  for j in range(len(points)):
    p2 = points[j]
    if i != j:
      dist = math.dist(p1, p2)
      if dist < closest_pair_dist:
        closest_pair_dist = dist
        closest_pair = p1, p2

print(closest_pair[0][0], closest_pair[0][1])
print(closest_pair[1][0], closest_pair[1][1])



