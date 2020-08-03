import sys

N=int(sys.stdin.readline().strip())

books=dict()

for _ in range(N):
    book = sys.stdin.readline().strip()
    if book in books:
        books[book]+=1
    else:
        books[book]=1

# books.values()
# print(books)
cnt=sorted(books.values())
titles=sorted(books)
for title in titles:
    if books[title]==cnt[-1]:
        print(title)
        break

