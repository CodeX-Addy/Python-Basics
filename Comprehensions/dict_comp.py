books_inr = {
    "Atomic Habits" : 200,
    "The Lord of the rings": 500,
    "The Alchemist": 400
}

books_usd = {book: price/90 for book, price in books_inr.items()}
print(books_usd)

## output: {'Atomic Habits': 2.2222222222222223, 'The Lord of the rings': 5.555555555555555, 'The Alchemist': 4.444444444444445}
