import random
from datetime import datetime

from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_protect
from opentelemetry import trace
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


from profile_page.models import Profile
from resource_library.models import Resource
from .models import Language, Lesson, Question, Answer, Quiz
from .user_progress_models import LessonStatus, QuizStatus, QuizUserAnswers

tracer = trace.get_tracer(__name__)


@login_required
def all_possible_classes(request):
    languages = Language.objects.all()
    context = {
        'languages': languages
    }
    return render(request, 'module/modules_main.html', context)

@login_required
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def modules_list(request, language_id):
    with tracer.start_as_current_span("modules_list"):
        user = request.user
        language = get_object_or_404(Language, pk=language_id)
        modules = language.module_set.all()
        profile = Profile.objects.get(user=user)

        learner_type_to_difficulty = {
            1: "Easy",
            2: "Medium",
            3: "Hard"
        }

        user_learner_type_id = user.profile.learner_type.id
        difficulty_level = learner_type_to_difficulty.get(user_learner_type_id, "Easy")

        lessons = Lesson.objects.filter(module__language=language, difficulty_level=difficulty_level).order_by('module')
        quizzes = Quiz.objects.filter(module__language=language, difficulty_level=difficulty_level).order_by('module')

        lesson_statuses = LessonStatus.objects.filter(profile=profile, lesson__in=lessons)
        quiz_statuses = QuizStatus.objects.filter(profile=profile, quiz__in=quizzes)

        # Map lesson and quiz statuses to their respective IDs
        lesson_status_dict = {status.lesson.id: status.status for status in lesson_statuses}
        quiz_status_dict = {status.quiz.id: status.status for status in quiz_statuses}

        # Prepare the data structure with lessons and quizzes grouped by modules
        modules_data = []
        for module in modules:
            module_lessons = lessons.filter(module=module)
            module_quizzes = quizzes.filter(module=module)

            module_data = {
                'id': module.id,
                'title': module.title,
                'lessons': [{
                    'id': lesson.id,
                    'title': lesson.title,
                    'status': lesson_status_dict.get(lesson.id, 'Not Started')
                } for lesson in module_lessons],
                'quizzes': [{
                    'id': quiz.id,
                    'title': quiz.title,
                    'status': quiz_status_dict.get(quiz.id, 'Not Started')
                } for quiz in module_quizzes]
            }
            modules_data.append(module_data)

        # Final response data
        data = {
            'language': {
                'id': language.id,
                'name': language.name
            },
            'modules': modules_data
        }

        # Check if the request expects a JSON response
        if 'application/json' in request.META.get('HTTP_ACCEPT', ''):
            return Response(data, status=status.HTTP_200_OK)
        else:
            context = {
                'language': language,
                'modules': modules,
                'lessons': lessons,
                'quizzes': quizzes,
                'lesson_statuses': lesson_statuses,
                'quiz_statuses': quiz_statuses,
            }
            return render(request, 'module/modules_list.html', context)




@login_required
def lesson_info(request, lesson_id, language_id):
    with tracer.start_as_current_span("lesson_info") as span:
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        language = get_object_or_404(Language, pk=language_id)
        sections = lesson.section_set.all()
        section_count = sections.count()
        context = {'lesson': lesson, 'language': language, 'sections': sections, 'section_count': section_count}
        complete_lesson(request, lesson_id)
        return render(request, 'module/lesson_info.html', context)


@csrf_protect
@login_required
def lesson_quiz(request, quiz_id, language_id):
    with tracer.start_as_current_span("lesson_quiz") as span:
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
        return render(request, 'module/lesson_quiz.html',
                      {'quiz': quiz, 'quiz_status': quiz_status, 'language': language, 'questions': questions,
                       'answers_dict': answers_dict})


def complete_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    profile = Profile.objects.get(user=request.user)
    lesson_status, created = LessonStatus.objects.get_or_create(lesson_id=lesson.id, profile=profile)
    lesson_status.status = "Completed"
    lesson_status.finished_at = datetime.now()
    lesson_status.save()


def complete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    profile = Profile.objects.get(user=request.user)
    quiz_status, created = QuizStatus.objects.get_or_create(quiz_id=quiz.id, profile=profile)
    quiz_status.status = "Completed"
    quiz_status.finished_at = datetime.now()
    quiz_status.save()


@login_required
def quiz_result(request, language_id, quiz_id):
    with tracer.start_as_current_span("quiz_result") as span:
        if request.method == 'POST':
            return handle_quiz_post(request, language_id, quiz_id)
        else:
            return show_quiz_result(request, language_id, quiz_id)


def handle_quiz_post(request, language_id, quiz_id):
    with tracer.start_as_current_span("handle_quiz_post") as span:
        submitted_data = request.POST
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        profile = get_object_or_404(Profile, user=request.user)

        process_submitted_answers(submitted_data, quiz, profile)

        complete_quiz(request, quiz_id)

        percentage_correct = calculate_percentage_correct(quiz, profile)

        if request.user.profile.quiz_results_notifications == "Send":
            send_quiz_results_email(request.user, quiz, profile, percentage_correct, language_id)

        return redirect('quiz_result', language_id=language_id, quiz_id=quiz_id)


def process_submitted_answers(submitted_data, quiz, profile):
    for question_id, answer_id in submitted_data.items():
        if question_id.startswith('question_'):
            question_id = question_id.split('_')[1]
            question = get_object_or_404(Question, pk=question_id)

            if question.question_type == "Single Choice":
                process_single_choice_answer(quiz, question, profile, answer_id)

            elif question.question_type == "Multiple Choice":
                process_multiple_choice_answer(submitted_data, quiz, question, profile)

            elif question.question_type == "Open Text":
                process_open_text_answer(quiz, question, profile, answer_id)


def process_single_choice_answer(quiz, question, profile, answer_id):
    user_answer = get_object_or_404(Answer, pk=answer_id)
    is_correct = "Correct" if user_answer.is_correct == "Correct" else "Incorrect"
    new_answer = QuizUserAnswers.objects.create(
        quiz=quiz,
        question=question,
        profile=profile,
        user_answer=user_answer.text,
        is_correct=is_correct
    )
    new_answer.save()


def process_multiple_choice_answer(submitted_data, quiz, question, profile):
    answer_ids = submitted_data.getlist(f"question_{question.id}")
    correct_answer = question.answer_set.filter(is_correct="Correct").values_list('text', flat=True)
    correct_answers = list(correct_answer) if correct_answer else None
    answer_objects = Answer.objects.filter(pk__in=answer_ids)
    user_answers = [answer.text for answer in answer_objects]
    is_correct = "Correct" if user_answers == correct_answers else "Incorrect"
    new_answer = QuizUserAnswers.objects.create(
        quiz=quiz,
        question=question,
        profile=profile,
        user_answer=user_answers,
        is_correct=is_correct
    )
    new_answer.save()


def process_open_text_answer(quiz, question, profile, answer_id):
    user_answer_text = answer_id.strip().lower()
    correct_answer = question.answer_set.filter(is_correct="Correct").first()
    correct_answer_text = correct_answer.text.strip().lower() if correct_answer else ''
    is_correct = "Correct" if user_answer_text == correct_answer_text else "Incorrect"
    if user_answer_text:
        new_answer = QuizUserAnswers.objects.create(
            quiz=quiz,
            question=question,
            profile=profile,
            user_answer=user_answer_text,
            is_correct=is_correct
        )
        new_answer.save()


def calculate_percentage_correct(quiz, profile):
    total_questions = quiz.question_set.count()
    total_correct_answers = QuizUserAnswers.objects.filter(quiz=quiz, profile=profile, is_correct="Correct").count()
    return (total_correct_answers / total_questions) * 100


def send_quiz_results_email(user, quiz, profile, percentage_correct, language_id):
    subject = f"Quiz Result for {quiz.title}"
    html_message = render_to_string('emails/email_quiz_result.html', {
        'quiz': quiz,
        'profile': profile,
        'percentage_correct': percentage_correct,
        'language_id': language_id
    })
    plain_message = strip_tags(html_message)
    recipient_list = [user.email]

    send_mail(subject, plain_message, None, recipient_list, html_message=html_message)


def show_quiz_result(request, language_id, quiz_id):
    with tracer.start_as_current_span("show_quiz_result") as span:
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        profile = get_object_or_404(Profile, user=request.user)
        language = get_object_or_404(Language, pk=language_id)

        questions = quiz.question_set.all()
        user_answers = QuizUserAnswers.objects.filter(quiz=quiz, profile=profile)

        percentage_correct = calculate_percentage_correct(quiz, profile)
        quiz_data = get_quiz_data(questions, user_answers)

        resources = Resource.objects.filter(name=quiz.title)

        context = {
            'quiz': quiz,
            'language': language,
            'questions': questions,
            'quiz_data': quiz_data,
            'resource_data': resources,
            'percentage_correct': percentage_correct
        }
        return render(request, 'module/quiz_result.html', context)


def get_quiz_data(questions, user_answers):
    quiz_data = {}
    for question in questions:
        user_answer = user_answers.filter(question=question).first()
        correct_answer = list(question.answer_set.filter(is_correct="Correct").values_list('text', flat=True))

        user_answer_text = user_answer.user_answer if user_answer else None
        user_answer_text = parse_user_answer(user_answer_text)

        quiz_data[question] = {
            'correct_answer': correct_answer,
            'user_answer': user_answer_text,
            'is_correct': user_answer.is_correct if user_answer else None
        }
    return quiz_data


def parse_user_answer(user_answer_text):
    if isinstance(user_answer_text, str) and user_answer_text.startswith('[') and user_answer_text.endswith(']'):
        user_answer_list = user_answer_text[1:-1].split(',')
        return [answer.strip().strip("'") for answer in user_answer_list if answer.strip()]
    return user_answer_text
