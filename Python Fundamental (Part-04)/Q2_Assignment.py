class Book:
    count = 0
    all_books = [];

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.review = []
        Book.count += 1
        Book.all_books.append(self)

    def add_new_review(self, new_review):
        self.review.append(new_review)
        print("Review added successfully")

    def display_review(self):
        for val in self.review:
            print(val)

    @classmethod
    def display_all_reviews(cls):
        for book in cls.all_books:
            for rv in book.review:
                print(rv)

book1 = Book("Python", "Rakibul")
book1.add_new_review("Good Product")

book2 = Book("CPP", "Shuvo")
book2.add_new_review("Amazing")

Book.display_all_reviews()
