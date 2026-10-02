t = input().strip()
answers = []

for i in range(int(t)):
  n = input().strip()
  for i in range(1):
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))
    line1.sort()
    line2.sort(reverse=True)
    res = [line1[i] * line2[i] for i in range(len(line1))]
    answers.append(sum(res))
  
for i in range(len(answers)):
  print(f"Case #{i + 1}: ", answers[i])
    
