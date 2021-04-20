def print_book_info(title, author=None, year=None):
    result = f"\"{title}\""
    if author is not None or year is not None:
        result = f"{result} was written"
    if author is not None:
        result = f"{result} by {author}"
    if year is not None:
        result = f"{result} in {year}"

    print(result)
