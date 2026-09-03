import heapq

n, m, k = map(int, input().split())

book_pile = []
new_books = []
current_time = 0
gift_book_id = 0

for i in range(n):
  _, title, pages = input().strip().split('"')
  if (title < "Jane Eyre"):
    book_pile.append((title, int(pages)))   

for i in range(m):
  time, title, pages = input().strip().split('"')
  if (title < "Jane Eyre"):
    new_books.append((int(time), title, int(pages)))
    
book_pile.append(("Jane Eyre", k))

book_pile.sort()
new_books.sort(key=lambda x: x[0])

while len(book_pile) > 0:
  title, pages = book_pile.pop(0)
  # print("Current title: ", title, "pages: ", pages)
  # print("Time before pages has been added", current_time)
  current_time += pages
  # print("Time after pages has been added", current_time)
  if title == "Jane Eyre":
    print(current_time)
    break
  # print(gift_book_id, len(new_books))
  # print(new_books[i][0], current_time)
  while gift_book_id < len(new_books) and new_books[gift_book_id][0] <= current_time:
    time, title, pages = new_books[gift_book_id]
    # print("Time, title and pages of book from the new pile: ", time, title, pages)
    book_pile.append((title, pages))
    book_pile.sort()
    gift_book_id += 1
  
