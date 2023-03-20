# TODO: Feature 1
import unittest
from app import app
from app import get_all_movies

class TestGetAllMovies(unittest.TestCase):
    
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_all_movies_status_code(self):
        result = self.app.get('/movies')
        self.assertEqual(result.status_code, 200)

    def test_get_all_movies_content(self):
        expected_output = [
            {'title': 'The Shawshank Redemption', 'year': 1994, 'director': 'Frank Darabont'},
            {'title': 'The Godfather', 'year': 1972, 'director': 'Francis Ford Coppola'},
            {'title': 'The Godfather: Part II', 'year': 1974, 'director': 'Francis Ford Coppola'}
        ]
        result = get_all_movies()
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
