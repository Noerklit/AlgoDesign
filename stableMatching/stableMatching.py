n, m = input().strip().split()
matches = set()

proposers = {}
rejecters = {}

for i in range(int(n)):
  line = input().split()
  if i % 2 == 0:
    proposers[line[0]] = line[1:]
  else:
    rejecters[line[0]] = line[1:]

for p in proposers:
  array = []
  array.append(proposers.get(p))
  
  

# print("Proposers", proposers)
# print("Rejecters", rejecters)
  