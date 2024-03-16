from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Language, Lesson


def all_possible_classes(request):
    languages = Language.objects.all()
    context = {
        'languages': languages
    }
    return render(request, 'modules_main.html', context)


def modules_list(request, language_id):
    language = get_object_or_404(Language, pk=language_id)
    modules = language.module_set.all()
    lessons = Lesson.objects.filter(module__language=language)

    context = {
        'language': language,
        'modules': modules,
        'lessons': lessons,
    }
    return render(request, 'modules_list.html', context)


def lessons_list(request, lesson_id, language_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    language = get_object_or_404(Language, pk=language_id)
    sections = lesson.section_set.all()
    section_count = sections.count()
    complete_lesson(request, lesson_id)
    return render(request, 'lesson_info.html',
                  {'lesson': lesson, 'language': language, 'sections': sections, 'section_count': section_count})


def complete_lesson(request, lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)
    lesson.status = 'Completed'
    lesson.save()
