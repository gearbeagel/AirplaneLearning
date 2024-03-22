import unittest
from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase

from modules.views import complete_lesson, complete_quiz
from profile_page.models import Profile
from .models import Language, Module, Lesson, LessonStatus, Quiz, QuizStatus


class LessonCompletionTestCase(TestCase):

    def setUp(self):
        self.language = Language.objects.create(name='Test Language')
        self.module = Module.objects.create(title='Test Module', language=self.language)
        self.lesson = Lesson.objects.create(title='Test Lesson', module=self.module)
        self.user = User.objects.create(username='testuser')
        self.profile = Profile.objects.create(user=self.user)
        self.lesson_status = LessonStatus.objects.create(lesson=self.lesson, profile=self.profile, status='Not Started')

    @patch('modules.views.complete_lesson')
    def test_complete_lesson(self, mock_complete_lesson):
        mock_complete_lesson.return_value = None
        request_factory = RequestFactory()
        request = request_factory.get('/')
        request.user = self.user
        self.assertEqual(self.lesson_status.status, 'Not Started')
        complete_lesson(request, self.lesson.id)
        self.lesson_status.refresh_from_db()
        self.assertEqual(self.lesson_status.status, 'Completed')
        print(f"Lesson {self.lesson.title} is {self.lesson_status.status}!")



class QuizCompletionTestCase(TestCase):

    def setUp(self):
        self.language = Language.objects.create(name='Test Language')
        self.module = Module.objects.create(title='Test Module', language=self.language)
        self.quiz = Quiz.objects.create(title='Test Quiz', module=self.module)
        self.user = User.objects.create(username='testuser')
        self.profile = Profile.objects.create(user=self.user)
        self.quiz_status = QuizStatus.objects.create(quiz=self.quiz, profile=self.profile, status='Not Started')

    @patch('modules.views.complete_quiz')
    def test_complete_quiz(self, mock_complete_quiz):
        mock_complete_quiz.return_value = None
        request_factory = RequestFactory()
        request = request_factory.get('/')
        request.user = self.user
        self.assertEqual(self.quiz_status.status, 'Not Started')
        complete_quiz(request, self.quiz.id)
        self.quiz_status.refresh_from_db()
        self.assertEqual(self.quiz_status.status, 'Completed')
        print(f"Quiz {self.quiz.title} is {self.quiz_status.status}!")


if __name__ == '__main__':
    unittest.main()
