import unittest

from src.content import Book, Movie, Music, Series


class ContentTestCase(unittest.TestCase):
    def test_movie_instance(self):
        movie = Movie("Inception", 2010, director="Christopher Nolan", duration=2.5)
        self.assertEqual(movie.name, "Inception")
        self.assertEqual(movie.year, 2010)
        self.assertEqual(movie.director, "Christopher Nolan")
        self.assertEqual(movie.duration, 2.5)
        self.assertEqual(movie.content_type, "Movie")

    def test_music_instance(self):
        music = Music("Bohemian Rhapsody", 1975, artist="Queen", duration=5.5)
        self.assertEqual(music.name, "Bohemian Rhapsody")
        self.assertEqual(music.year, 1975)
        self.assertEqual(music.artist, "Queen")
        self.assertEqual(music.duration, 5.5)
        self.assertEqual(music.content_type, "Music")

    def test_series_instance(self):
        series = Series("Friends", 1994, season=10, duration=22.0)
        self.assertEqual(series.name, "Friends")
        self.assertEqual(series.year, 1994)
        self.assertEqual(series.season, 10)
        self.assertEqual(series.duration, 22.0)
        self.assertEqual(series.content_type, "Series")

    def test_book_instance(self):
        book = Book("To Kill a Mockingbird", 1960, author="Harper Lee", pages=336)
        self.assertEqual(book.name, "To Kill a Mockingbird")
        self.assertEqual(book.year, 1960)
        self.assertEqual(book.author, "Harper Lee")
        self.assertEqual(book.pages, 336)
        self.assertEqual(book.content_type, "Book")

    def test_movie_str(self):
        movie = Movie("Inception", 2010, director="Christopher Nolan", duration=2.5)
        expected_output = "Inception is a 2.5 long Movie, released in 2010, directed by Christopher Nolan"
        self.assertEqual(str(movie), expected_output)


if __name__ == "__main__":
    unittest.main()
