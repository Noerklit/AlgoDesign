n = int(input())
weights = [int(input()) for _ in range(n)]

pos_sums = {0}

for w in weights:
  # print("current possible sums: ", pos_sums)
  # print("current weight: ", w)
  
  # Make a new set of unique sums, by adding the weight to all current possible sums, but discard any of these that are above 
  # 2000, as we already know Wallace would choose 0 instead of a number that is bigger than 2000
  new_sums = {sum + w for sum in pos_sums if sum + w <= 2000}
  # print("new sums: ", new_sums)
  pos_sums.update(new_sums)
  

# print(pos_sums)
best_sum = min(pos_sums, key=lambda x: (abs(x - 1000), -x))
print(best_sum)