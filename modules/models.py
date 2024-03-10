from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    difficulty_level = models.CharField(
        max_length=20,
        choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')],
        default='medium'
    )

    def __str__(self):
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    lessons = models.ManyToManyField(Lesson)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
