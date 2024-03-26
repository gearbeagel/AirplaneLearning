from django.contrib import admin
from .models import Language, Lesson, Quiz, Module, Section, Question, Answer, LessonStatus, QuizStatus, QuizUserAnswers

# Register your models here

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display only the name field

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'difficulty_level')  # Customize displayed fields

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'difficulty_level')  # Customize displayed fields

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'order')  # Customize displayed fields

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson')  # Customize displayed fields

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz')  # Customize displayed fields

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')  # Customize displayed fields

@admin.register(LessonStatus)
class LessonStatusAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'profile', 'status', 'finished_at')  # Customize displayed fields

@admin.register(QuizStatus)
class QuizStatusAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'profile', 'status', 'finished_at')  # Customize displayed fields

@admin.register(QuizUserAnswers)
class QuizUserAnswersAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'profile', 'user_answer', 'is_correct', 'question')  # Customize displayed fields
