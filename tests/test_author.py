from models.author import Author

def test_author_creation():
    author = Author(name="Jane Doe", nationality="Kenyan")
    assert author.name == "Jane Doe"
    assert author.nationality == "Kenyan"
