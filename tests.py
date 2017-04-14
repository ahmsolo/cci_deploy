import unittest
from server import app


class FlaskTestsBasic(unittest.TestCase):
    """Flask tests."""

    def setUp(self):
        """ Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Display Flask errors that occur during tests
        app.config['TESTING'] = True

    def test_index(self):
        """Test that homepage is loading as expected """

        result = self.client.get("/")
        print "result,", result
        # Confirm that copy unique to homepage is present
        self.assertIn("Ahm Lee's Circle CI Challenge", result.data)

if __name__ == '__main__':
    unittest.main()
