from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

User = get_user_model()


class LeeriApprenticesTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_creation(self):
        """
        Test that a user is created correctly.
        """
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('testpassword'))

    def test_user_groups(self):
        """
        Test that a user can belong to groups.
        """
        group = Group.objects.create(name='Test Group')

        self.user.groups.add(group)

        self.assertTrue(self.user.groups.filter(name='Test Group').exists())

    def test_user_permissions(self):
        """
        Test that a user can have permissions.
        """
        content_type = ContentType.objects.get_for_model(User)

        # Create a permission
        permission = Permission.objects.create(
            name='Test Permission',
            codename='test_permission',
            content_type=content_type
        )

        self.user.user_permissions.add(permission)

        self.assertTrue(self.user.has_perm('auth.test_permission'))
