from django.test import TestCase
from django.contrib.auth.models import User

from .models import Test, Question


class TestTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user',
            email='user@example.com',
            password='hunter2'
        )

    def test_correct_questions(self):
        test = Test(owner=self.user, name='test', source='a\n\nb\n\n')
        test.save()

        names_indexes = [(q.name, q.index) for q in test.question_set.all()]
        self.assertEqual(names_indexes, [
            ('a', 1),
            ('', 2),
            ('b', 3),
            ('', 4),
        ])
