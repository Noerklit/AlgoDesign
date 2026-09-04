n, m = input().strip().split()
n = int(n)
matches = {}

proposers = {}
rejecters = {}
names_ordered = []

for i in range(n):
  line = input().split()
  names_ordered.append(line[0])
  if i < n // 2:
    proposers[line[0]] = line[1:]
  else:
    rejecters[line[0]] = line[1:]

singles = list(proposers.keys())

proposer_rank = {
  proposer: {pref: id for id, pref in enumerate(preferences)}
  for proposer, preferences in proposers.items()
}

rejecter_rank = {
  rejecter: {pref: id for id, pref in enumerate(preferences)}
  for rejecter, preferences in rejecters.items()
}

next_proposal = {p: 0 for p in proposers}

while singles:
  p = singles.pop()
  proposes_to = proposers[p][next_proposal[p]]
  next_proposal[p] += 1
  if proposes_to not in matches:
    matches[proposes_to] = p
  else:
    current = matches[proposes_to]
    if rejecter_rank[proposes_to][p] < rejecter_rank[proposes_to][current]:
      matches[proposes_to] = p
      singles.append(current)
    else:
      singles.append(p)

for proposer, rejecter in matches.items():
  print(proposer, rejecter)

  