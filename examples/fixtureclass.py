from attr import dataclass
from pytest import fixture, FixtureRequest

from pytest_fixtureclass import fixtureclass

MOVIES = [
    "Lord Of The Rings",
    "Star Wars",
    "Star Trek",
    "The Princess Bride"
]


@dataclass
class Book:
    name: str
    
    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

def book_id(book: Book) -> str:
    return str(book)

BOOKS = [
    Book("Lord Of The Flies"),
    Book("Dune"),
    Book("The Hobbit"),
]

@fixture(params=MOVIES)
def movie_fixture(request: FixtureRequest) -> str:
    return request.param


@fixture(params=BOOKS, ids=str)
def book_fixture(request: FixtureRequest) -> Book:
    return request.param


def test_sanity(movie_fixture, book_fixture):
    assert movie_fixture in MOVIES
    assert book_fixture in BOOKS


@fixtureclass
class TestFixtureClass:

    movie_fixture: str
    book_fixture: Book

    def test_fixtureclass(self):
        assert self.movie_fixture in MOVIES
        assert self.book_fixture in BOOKS

