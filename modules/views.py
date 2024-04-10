import random
from datetime import datetime

from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
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
    if user_learner_type.id == 1:
        difficulty_level = "Easy"
    elif user_learner_type.id == 2:
        difficulty_level = "Medium"
    elif user_learner_type.id == 3:
        difficulty_level = "Hard"
    else:
        difficulty_level = "Easy"

    lessons = Lesson.objects.filter(module__language=language, difficulty_level=difficulty_level)
    for lesson in lessons:
        lesson_statuses = LessonStatus.objects.filter(profile=profile, lesson=lesson)

    quizzes = Quiz.objects.filter(module__language=language, difficulty_level=difficulty_level)
    for quiz in quizzes:
        quiz_statuses = QuizStatus.objects.filter(profile=profile, quiz=quiz)

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
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        profile = get_object_or_404(Profile, user=request.user)

        for question_id, answer_id in submitted_data.items():
            if question_id.startswith('question_'):
                question_id = question_id.split('_')[1]
                question = get_object_or_404(Question, pk=question_id)

                if question.question_type == "Single Choice":
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

                elif question.question_type == "Multiple Choice":
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

                elif question.question_type == "Open Text":
                    user_answer_text = answer_id.strip().lower()
                    correct_answer = question.answer_set.filter(is_correct="Correct").first()
                    correct_answer_text = correct_answer.text.strip().lower() if correct_answer else ''
                    is_correct = "Correct" if user_answer_text == correct_answer_text else "Incorrect"
                    if user_answer_text:
                        new_answer = QuizUserAnswers.objects.create(
                            quiz=quiz,
                            question=question,
                            profile=request.user.profile,
                            user_answer=user_answer_text,
                            is_correct=is_correct
                        )
                        new_answer.save()

        quiz_status, created = QuizStatus.objects.get_or_create(quiz_id=quiz_id, profile=profile)
        quiz_status.status = "Completed"
        quiz_status.save()

        subject = f"Quiz Result for {quiz.title}"
        total_questions = quiz.question_set.count()
        total_correct_answers = QuizUserAnswers.objects.filter(quiz=quiz, profile=profile, is_correct="Correct").count()
        percentage_correct = (total_correct_answers / total_questions) * 100
        html_message = render_to_string('email_quiz_result.html', {'quiz': quiz, 'profile': profile,
                                                              'percentage_correct': percentage_correct,
                                                              'language_id': language_id})
        plain_message = strip_tags(html_message)
        recipient_list = [request.user.email]

        send_mail(subject, plain_message, None, recipient_list, html_message=html_message)

        return redirect('quiz_result', language_id=language_id, quiz_id=quiz_id)

    quiz = get_object_or_404(Quiz, pk=quiz_id)
    profile = get_object_or_404(Profile, user=request.user)
    language = get_object_or_404(Language, pk=language_id)
    questions = Question.objects.filter(quiz=quiz)
    user_answers = QuizUserAnswers.objects.filter(quiz=quiz, profile=profile)

    quiz_data = {}
    for question in questions:
        user_answer = user_answers.filter(question=question).first()
        correct_answer = question.answer_set.filter(is_correct="Correct").values_list('text', flat=True)
        correct_answer = list(correct_answer) if correct_answer else None

        user_answer_text = user_answer.user_answer if user_answer else None

        if isinstance(user_answer_text, str) and user_answer_text.startswith('[') and user_answer_text.endswith(']'):
            user_answer_list = user_answer_text[1:-1].split(',')
            user_answer_text = [answer.strip().strip("'") for answer in user_answer_list if answer.strip()]

        quiz_data[question] = {
            'correct_answer': correct_answer,
            'user_answer': user_answer_text,
            'is_correct': user_answer.is_correct if user_answer else None
        }

    context = {'quiz': quiz, 'language': language, 'questions': questions, 'quiz_data': quiz_data}
    return render(request, 'quiz_result.html', context)
