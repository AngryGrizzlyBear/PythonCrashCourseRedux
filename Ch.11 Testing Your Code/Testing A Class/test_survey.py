import unittest
from survey import AnnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase):
    """Test for the class AnnoymousSurvey"""

    def test_store_single_responses(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language di you first learn to speak?"
        my_survey = AnnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

unittest.main()
