word = input().strip()

stack = []

for char in word:
    if char == '<':
        stack.pop()
    else:
        stack.append(char)

print("".join(stack))
    
    