import random

from django import template
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from profile_page.models import Profile
from .models import Language, Lesson, Question, Answer, Quiz, LessonStatus, QuizStatus


def all_possible_classes(request):
    languages = Language.objects.all()
    context = {
        'languages': languages
    }
    return render(request, 'modules_main.html', context)


def modules_list(request, language_id):
    user = request.user
    language = get_object_or_404(Language, pk=language_id)
    modules = language.module_set.all()
    profile = Profile.objects.get(user=user)

    user_learner_type = user.profile.learner_type
    if user_learner_type in ["Beginner", "A rookie!"]:
        difficulty_level = "Easy"
    elif user_learner_type in ["Skilled", "A smart cookie!"]:
        difficulty_level = "Medium"
    elif user_learner_type in ["Advanced", "A very smart cookie!"]:
        difficulty_level = "Hard"
    else:
        difficulty_level = "Easy"

    lessons = Lesson.objects.filter(module__language=language, difficulty_level=difficulty_level)
    lesson_statuses = {}  # Dictionary to store lesson statuses

    for lesson in lessons:
        lesson_status = LessonStatus.objects.get_or_create(lesson=lesson, profile=profile)[0]
        lesson_statuses[lesson.id] = lesson_status

    quizzes = Quiz.objects.filter(module__language=language, difficulty_level=difficulty_level)
    quiz_statuses = {}

    for quiz in quizzes:
        quiz_status = QuizStatus.objects.get_or_create(quiz=quiz, profile=profile)[0]
        quiz_statuses[quiz.id] = quiz_status

    context = {
        'language': language,
        'modules': modules,
        'lessons': lessons,
        'quizzes': quizzes,
        'lesson_statuses': lesson_statuses,
        'quiz_statuses': quiz_statuses,
    }
    return render(request, 'modules_list.html', context)


def lesson_info(request, lesson_id, language_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    language = get_object_or_404(Language, pk=language_id)
    sections = lesson.section_set.all()
    section_count = sections.count()
    context = {'lesson': lesson, 'language': language, 'sections': sections, 'section_count': section_count}
    complete_lesson(request, lesson_id)
    return render(request, 'lesson_info.html', context)


@csrf_protect
def lesson_quiz(request, quiz_id, language_id):
    quiz = get_object_or_404(Lesson, pk=quiz_id)
    language = get_object_or_404(Language, pk=language_id)
    questions = list(Question.objects.filter(quiz_id=quiz_id))
    random.shuffle(questions)
    answers_dict = {}
    for question in questions:
        answers = list(Answer.objects.filter(question=question))  # Get answers for the question
        answers_dict[question] = answers
    return render(request, 'lesson_quiz.html',
                  {'quiz': quiz, 'language': language, 'questions': questions, 'answers_dict': answers_dict})


def complete_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    profile = Profile.objects.get(user=request.user)
    lesson_status = LessonStatus.objects.get(lesson_id=lesson.id, profile=profile)
    lesson_status.status = "Completed"
    lesson_status.save()


def complete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    profile = Profile.objects.get(user=request.user)
    quiz_status = QuizStatus.objects.get(quiz_id=quiz.id, profile=profile)
    quiz_status.status = "Completed"
    quiz_status.save()


def quiz_result(request, language_id, quiz_id):
    questions = Question.objects.all()
    language = Language.objects.get(pk=language_id)

    quiz_data = {}

    for question in questions:
        correct_answer = question.answer_set.filter(is_correct='Correct').first()
        quiz_data[question] = correct_answer

    context = {'quiz_data': quiz_data, 'language': language}
    complete_quiz(request, quiz_id)

    return render(request, 'quiz_result.html', context)
