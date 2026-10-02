from graphlib import TopologicalSorter

n = int(input().strip())

timeOfSteps = input().split()
times = [int(x) for x in timeOfSteps]
stepMapping = {}

shortest_time = float('inf')

for i in range(n):
  preReqAmount, *dependencies = map(int, input().strip().split())
  stepMapping[i + 1] = dependencies

ts = TopologicalSorter(stepMapping)
sorted = tuple(ts.static_order())

def compute_total_time(stepDurations):
  accStepTimes = {}
  for step in sorted:
    stepTime = stepDurations[step - 1]
    deps = stepMapping[step]
    if not deps:
      accStepTimes[step] = stepTime
    else:
      accStepTimes[step] = max(accStepTimes[d] for d in deps) + stepTime
  return (accStepTimes[n])

for step_to_eliminate in range(1, n +1):
  copied_times = times.copy()
  copied_times[step_to_eliminate - 1] = 0
  total_time = compute_total_time(copied_times)
  shortest_time = min(shortest_time, total_time)

print(shortest_time)
