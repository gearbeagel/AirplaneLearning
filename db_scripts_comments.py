import os
import django
import random
from faker import Faker
from discussion_forums.models import Topic, Comment
from modules.models import Lesson
from profile_page.models import LearnerType, Language, Profile
from django.contrib.auth.models import User

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ALPP.settings")

django.setup()


def create_fake_data():
    faker = Faker()

    learner_types = LearnerType.objects.all()
    if not learner_types:
        for _ in range(5):
            LearnerType.objects.create(name=faker.word())

    languages = Language.objects.all()
    if not languages:
        for _ in range(5):
            Language.objects.create(name=faker.language_name())

    if not Profile.objects.exists():
        for _ in range(10):
            user = User.objects.create_user(
                username=faker.user_name(),
                email=faker.email(),
                password='password123'
            )
            Profile.objects.create(
                user=user,
                progress=random.uniform(0, 100),
                profile_pic_url=faker.image_url(),
                learner_type=random.choice(LearnerType.objects.all()),
                chosen_language=random.choice(Language.objects.all()),
                receive_notifications=random.choice(['Send', 'Do not send']),
                new_modules_notifications=random.choice(['Send', 'Do not send']),
                quiz_results_notifications=random.choice(['Send', 'Do not send']),
                discussion_notifications=random.choice(['Send', 'Do not send']),
                new_resources_notifications=random.choice(['Send', 'Do not send']),
            )

    if not Topic.objects.exists():
        for _ in range(10):
            Topic.objects.create(
                title=faker.sentence(nb_words=5),
                subject=random.choice(Lesson.objects.all()),
                description=faker.paragraph(nb_sentences=3)
            )

    # Create some Comments
    profiles = Profile.objects.all()
    topics = Topic.objects.all()

    for _ in range(50):
        Comment.objects.create(
            message=faker.paragraph(nb_sentences=2),
            topic=random.choice(topics),
            created_by=random.choice(profiles)
        )

    print('Successfully generated fake comments for topics')


if __name__ == '__main__':
    create_fake_data()
