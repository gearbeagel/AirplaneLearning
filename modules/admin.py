from django.contrib import admin
from .models import Language, Lesson, Quiz, Module, Section, Question, Answer
from .user_progress_models import LessonStatus, QuizStatus, QuizUserAnswers
# Register your models here

admin.register(Language)
admin.register(Lesson)
admin.register(Quiz)
admin.register(Module)
admin.register(Section)
admin.register(Question)
admin.register(Answer)
admin.register(LessonStatus)
admin.register(QuizStatus)
admin.register(QuizUserAnswers)
