word = input().strip()
new_word = []
bool = True

for char in word:
  if (char == 'b'):
    if (bool):
      new_word.append("0")
      bool = False
    else: 
      new_word.append("1")
      bool = True
  else: new_word.append(char)
word = "".join(new_word)
print(word)