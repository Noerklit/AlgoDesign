import string

n, t = map(int, input().split())

a = list(map(int, input().split()))

if t == 1:
    print(7)
elif t == 2:
    if a[0] > a[1]: print("Bigger")
    elif a[0] == a[1]: print("Equal")
    else: print("Smaller")
elif t == 3:
    sortedArray = sorted([a[0], a[1], a[2]])
    print(sortedArray[1])
elif t == 4:
    sum = 0
    for number in a:
        sum += number
    print(sum)
elif t == 5:
    even_sum = 0
    for number in a:
        if number % 2 == 0:
            even_sum += number
    print(even_sum)
elif t == 6:
    letters = [string.ascii_lowercase[n % 26] for n in a]
    print("".join(letters))
elif t == 7:
    i = 0
    visited = set()
    while True:
        i=a[i]
        if i < 0 or i >= n:
            print("Out")
            break
        elif i == n-1:
            print("Done")
            break
        elif i in visited: 
            print("Cyclic") 
            break
        visited.add(i)