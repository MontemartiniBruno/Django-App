import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

class QuestionModelTest(TestCase):

    def was_published_recently(self):
        """ This method should return false for question whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text='Esta es una pregunta del futuro', pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
    
