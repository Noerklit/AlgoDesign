n = int(input().strip())
intervals = []

for i in range(n):
  s, f = input().strip().split()
  intervals.append((int(s), int(f)))

intervals.sort(key=lambda iv: iv[1])

A = []
free = 0
for iv in intervals:
  if iv[0] >= free:
    free = iv[1]
    A.append(iv)
  
print(len(A))