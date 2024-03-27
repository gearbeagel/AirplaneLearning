from django.contrib.auth.models import User
from django.test import TestCase

from modules.models import Lesson, Quiz, Module, Language
from modules.user_progress_models import LessonStatus, QuizStatus
from .models import Profile

from .views import calculate_progress


class CalculateProgressTestCase(TestCase):
    def setUp(self):
        # Create a user for the Profile
        self.user = User.objects.create_user(username='test_user')

        # Create a Profile object for the user
        self.user_profile = Profile.objects.create(user=self.user, progress=0)

        # Create a language
        self.language = Language.objects.create(name='English')  # Replace 'English' with the actual language name

        # Create some modules associated with the language
        self.module1 = Module.objects.create(title='Module 1', language=self.language)
        self.module2 = Module.objects.create(title='Module 2', language=self.language)

        # Create some lessons and quizzes associated with modules
        self.lesson1 = Lesson.objects.create(title='Lesson 1', module=self.module1)
        self.lesson2 = Lesson.objects.create(title='Lesson 2', module=self.module2)
        self.quiz1 = Quiz.objects.create(title='Quiz 1', module=self.module1)
        self.quiz2 = Quiz.objects.create(title='Quiz 2', module=self.module2)

        # Mark some lessons and quizzes as completed for the user profile
        LessonStatus.objects.create(lesson=self.lesson1, profile=self.user_profile, status='Completed')
        LessonStatus.objects.create(lesson=self.lesson2, profile=self.user_profile, status='Completed')
        QuizStatus.objects.create(quiz=self.quiz1, profile=self.user_profile, status='Completed')


    def test_calculate_progress(self):
        calculate_progress(self.user_profile)

        updated_profile = Profile.objects.get(pk=self.user_profile.pk)

        total_lessons = Lesson.objects.count()
        total_quizzes = Quiz.objects.count()
        completed_lessons = LessonStatus.objects.filter(profile=self.user_profile, status="Completed").count()
        completed_quizzes = QuizStatus.objects.filter(profile=self.user_profile, status="Completed").count()
        total_items = total_lessons + total_quizzes
        completed_items = completed_lessons + completed_quizzes
        expected_progress = (completed_items / total_items) * 100

        print(f"Expected Progress: {expected_progress}%")
        print(f"Actual Progress: {updated_profile.progress}%")

        self.assertEqual(updated_profile.progress, expected_progress)
