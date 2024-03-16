import unittest
from unittest.mock import patch
from django.test import Client, TestCase

from modules.views import complete_lesson
from .models import Language, Module, Lesson


class LessonCompletionTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.language = Language.objects.create(name='Test Language')
        cls.module = Module.objects.create(title='Test Module', language=cls.language)
        cls.lesson = Lesson.objects.create(title='Test Lesson', module=cls.module)

    @patch('modules.views.complete_lesson')
    def test_complete_lesson(self, mock_complete_lesson):
        mock_complete_lesson.return_value = None
        self.assertEqual(self.lesson.status.lower(), 'not_started')
        complete_lesson(None, self.lesson.id)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.status.lower(), 'completed')
        print(f"Lesson {self.lesson.title} is completed!")


if __name__ == '__main__':
    unittest.main()
