cases = int(input())

for _ in range(cases):
    trips = int(input())
    cities = set()
    
    for _ in range(trips):
        city = input().strip()
        cities.add(city)
    
    print(len(cities))
