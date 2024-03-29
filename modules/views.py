import random
from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect

from profile_page.models import Profile
from .models import Language, Lesson, Question, Answer, Quiz
from .user_progress_models import LessonStatus, QuizStatus, QuizUserAnswers


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
    if user_learner_type in ["A rookie! (Beginner)", "Beginner"]:
        difficulty_level = "Easy"
    elif user_learner_type in ["A pookie! (Skilled)", "A smart cookie!"]:
        difficulty_level = "Medium"
    elif user_learner_type in ["A smart cookie! (Advanced)", "Advanced"]:
        difficulty_level = "Hard"
    else:
        difficulty_level = "Easy"

    lessons = Lesson.objects.filter(module__language=language, difficulty_level=difficulty_level)
    lesson_statuses = {}

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
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    profile = get_object_or_404(Profile, user=request.user)
    quiz_status, created = QuizStatus.objects.get_or_create(quiz_id=quiz.id, profile=profile)
    language = get_object_or_404(Language, pk=language_id)
    questions = list(Question.objects.filter(quiz_id=quiz.id))
    random.shuffle(questions)
    answers_dict = {}
    for question in questions:
        answers = list(Answer.objects.filter(question=question))
        answers_dict[question] = answers
    return render(request, 'lesson_quiz.html',
                  {'quiz': quiz, 'quiz_status': quiz_status, 'language': language, 'questions': questions,
                   'answers_dict': answers_dict})


def complete_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    profile = Profile.objects.get(user=request.user)
    lesson_status = LessonStatus.objects.get(lesson_id=lesson.id, profile=profile)
    lesson_status.status = "Completed"
    lesson_status.finished_at = datetime.now()
    lesson_status.save()


def complete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    profile = Profile.objects.get(user=request.user)
    quiz_status = QuizStatus.objects.get(quiz_id=quiz.id, profile=profile)
    quiz_status.status = "Completed"
    quiz_status.finished_at = datetime.now()
    quiz_status.save()


def quiz_result(request, language_id, quiz_id):
    if request.method == 'POST':
        submitted_data = request.POST
        for question_id, answer_id in submitted_data.items():
            if question_id.startswith('question_'):
                question_id = question_id.split('_')[1]

                quiz = get_object_or_404(Quiz, pk=quiz_id)
                question = get_object_or_404(Question, pk=question_id)
                user_answer = get_object_or_404(Answer, pk=answer_id)
                profile = get_object_or_404(Profile, user=request.user)
                correct_answer = question.answer_set.filter(is_correct="Correct").first()

                is_correct = "Correct" if user_answer == correct_answer else "Incorrect"

                QuizUserAnswers.objects.create(
                    quiz=quiz,
                    question=question,
                    profile=profile,
                    user_answer=user_answer.text,
                    is_correct=is_correct
                )

        quiz_status, created = QuizStatus.objects.get_or_create(quiz_id=quiz_id, profile=profile)
        quiz_status.status = "Completed"
        quiz_status.save()

        return redirect('quiz_result', language_id=language_id, quiz_id=quiz_id)

    quiz = get_object_or_404(Quiz, pk=quiz_id)
    profile = get_object_or_404(Profile, user=request.user)
    language = get_object_or_404(Language, pk=language_id)
    questions = Question.objects.filter(quiz=quiz)
    user_answers = QuizUserAnswers.objects.filter(quiz=quiz, profile=profile)

    quiz_data = {}
    for question in questions:
        user_answer = user_answers.filter(question=question).first()
        correct_answer = question.answer_set.filter(is_correct="Correct").first()
        quiz_data[question] = {
            'correct_answer': correct_answer.text if correct_answer else None,
            'user_answer': user_answer.user_answer if user_answer else None,
            'is_correct': user_answer.is_correct if user_answer else None
        }

    context = {'quiz': quiz, 'language': language, 'questions': questions, 'quiz_data': quiz_data}
    return render(request, 'quiz_result.html', context)
