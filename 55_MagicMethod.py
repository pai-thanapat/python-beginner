# 56. Megic Method


class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.num_pages} pages"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return (
            keyword.lower() in self.title.lower()
            or keyword.lower() in self.author.lower()
        )

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return "Key not found. Valid keys are 'title', 'author', and 'num_pages'."


book1 = Book("The Hobbit", "J.R.R. Tolkein", 310)
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 208)

print(book1)
print(book2)
print(book3)

print(f"Is book1 equal to book2? {book1 == book2}")
print(f"Is book2 is less than book3? {book2 < book3}")
print(f"Is book1 is greater than book3? {book1 > book3}")
print(f"Total number of pages in book1 and book2: {book1 + book2}")
print(f"Does book1 contain 'Hobbit'? { 'Hobbit' in book1 }")
print(f"Does book2 contain 'Rowling'? { 'Rowling' in book2 }")
print(f"Does book3 contain 'Narnia'? { 'Narnia' in book3 }")
print(f"Title of book1: {book1['title']}")
print(f"Author of book2: {book2['author']}")
print(f"Number of pages in book3: {book3['num_pages']}")
print(f"Trying to access an invalid key in book1: {book1['publisher']}")
