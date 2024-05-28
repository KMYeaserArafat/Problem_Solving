
#here n is total number of pages in books,
n = int(input().strip())
#here p is total number of pages in book you turn, 
p = int(input().strip())

pagesInBooks = p/2
totalPages = n/2

frontPage = pagesInBooks
EndPage = totalPages - pagesInBooks

print(min(frontPage,EndPage))