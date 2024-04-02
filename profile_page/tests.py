from django.test import TestCase
from unittest.mock import patch, Mock
from modules.models import Module, Lesson, Quiz
from modules.user_progress_models import LessonStatus, QuizStatus
from .views import calculate_progress

class CalculateProgressTestCase(TestCase):
    @patch('modules.models.Module.objects.filter')
    @patch('modules.models.Lesson.objects.filter')
    @patch('modules.models.Quiz.objects.filter')
    @patch('modules.user_progress_models.LessonStatus.objects.filter')
    @patch('modules.user_progress_models.QuizStatus.objects.filter')
    def test_calculate_progress(self, mock_quiz_status_filter, mock_lesson_status_filter, 
                                mock_quiz_filter, mock_lesson_filter, mock_module_filter):

        user_profile = Mock()
        chosen_language_id = 1
        mock_module_filter.return_value = [Mock(), Mock()]
        mock_lesson_filter.return_value.count.return_value = 3
        mock_quiz_filter.return_value.count.return_value = 2
        mock_lesson_status_filter.return_value.count.return_value = 2
        mock_quiz_status_filter.return_value.count.return_value = 1

        calculate_progress(user_profile, chosen_language_id)

        self.assertEqual(user_profile.progress, 60.0)

