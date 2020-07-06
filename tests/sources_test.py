import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    """
    SourcesTest class to test the behaviour of the Sources class
    """
    def setUp(self):
        """
        Method that runs before each other test runs

        """
        self.new_source = Sources('abc-news','ABC news','Your trusted source for breaking news',"https://abcnews.go.com","general","en","us")

    def instance_test(self):
        self.assertTrue(isinstance(self.new_source,Sources))

if __name__ == "__main__":
    unittest.main()