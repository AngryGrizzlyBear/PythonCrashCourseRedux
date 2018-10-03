import unittest
from survey import AnnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase):
    """Test for the class AnnoymousSurvey"""

    def test_store_single_responses(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)


unittest.main()
