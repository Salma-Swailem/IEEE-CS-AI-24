library_catalogue = [
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publication_year": "1813"
    },
    {
        "title": "American Psycho",
        "author": "Bret Easton Ellis",
        "publication_year": "1991"
    },
    {
        "title": "Sherlock Holmes: The Sign of Four",
        "author": "Arthur Conan Doyle",
        "publication_year": "1890"
    }
]

for book in library_catalogue:
    print("Title:", book["title"])
    print("Author:", book["author"])
    print("Publication Year:", book["publication_year"])
    print()