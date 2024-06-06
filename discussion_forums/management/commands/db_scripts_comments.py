import random
from django.core.management.base import BaseCommand
from faker import Faker
from discussion_forums.models import Topic, Comment
from modules.models import Lesson
from profile_page.models import LearnerType, Language, Profile
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Generate fake comments for topics'

    def handle(self, *args, **kwargs):
        faker = Faker()

        # Create some LearnerTypes and Languages if they don't exist
        learner_types = LearnerType.objects.all()
        if not learner_types:
            for _ in range(5):
                LearnerType.objects.create(name=faker.word())

        languages = Language.objects.all()
        if not languages:
            for _ in range(5):
                Language.objects.create(name=faker.language_name())

        for _ in range(20):
            user = User.objects.create_user(
                username=faker.user_name(),
                email=faker.email(),
                password='password123'
            )
            Profile.objects.create(
                user=user,
                username=user.username,
                email=user.email,
                progress=random.uniform(0, 100),
                learner_type=random.choice(LearnerType.objects.all()),
                chosen_language=random.choice(Language.objects.all()),
                receive_notifications=random.choice(['Send', 'Do not send']),
                new_modules_notifications=random.choice(['Send', 'Do not send']),
                quiz_results_notifications=random.choice(['Send', 'Do not send']),
                discussion_notifications=random.choice(['Send', 'Do not send']),
                new_resources_notifications=random.choice(['Send', 'Do not send']),
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

        self.stdout.write(self.style.SUCCESS('Successfully generated fake comments for topics'))
