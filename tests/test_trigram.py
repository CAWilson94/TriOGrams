from unittest import TestCase
from trigram import Trigram


class TestTrigram(TestCase):

    def setUp(self):
        input = "I wish I may I wish I might"
        self.trigram = Trigram(input)

    def test_find_trigrams(self):
        expected_trigram_collection = {
            "I wish": ["I", "I"],
            "wish I": ["may", "might"],
            "may I": ["wish"],
            "I may": ["I"]
        }
        actual_trigram_collection = self.trigram.findTrigrams()
        self.assertEqual(expected_trigram_collection, actual_trigram_collection)
