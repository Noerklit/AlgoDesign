from collections import Counter

n, t = map(int, input().split())

array = list(map(int, input().split()))

match t:
  case 1:
    set = set([])
    for num in array:
      y = 7777 - num
      if y in set: 
        print("Yes")
        break
      set.add(num)
    else:
      print("No")  
      
  case 2:
    set = set(array)
    if(len(array) != len(set)):
      print("Contains duplicate")
    else:
      print("Unique")
  
  case 3:
    frequency = Counter(array)
    target = n//2
    for num, frequency in frequency.items():
      if frequency > target:
        print(num)
        break
    else:
      print(-1)
    
  case 4:
    array.sort()
    if(n % 2 != 0):
      median = array[n // 2]
      print(median)
    else:
      median1 = array[(n // 2) - 1]
      median2 = array[n // 2]
      print(median1, median2)
    
  case 5:
    array.sort()
    result = list(filter(lambda x: x >= 100 and x<= 999, array))
    print(*result)