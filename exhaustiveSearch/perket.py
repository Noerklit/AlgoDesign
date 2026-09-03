number_ingredients = int(input().strip())
lowest = 1000000000
ingredients = []

for _ in range(number_ingredients):
  s, b = input().split(" ")
  ingredients.append((int(s), int(b)))
  
for k in range(1,1 << number_ingredients):
  sourness = 1
  bitterness = 0
  subset = [i for i in range(number_ingredients) if k >> i & 1]
  print(subset)
  for i in subset:
    s, b = ingredients[i]
    sourness *= s
    bitterness += b
  diff = abs(sourness - bitterness)
  if (diff < lowest):
    lowest = diff
  
print(lowest)
