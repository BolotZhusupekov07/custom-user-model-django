from typing import SupportsAbs
from django.test import TestCase
from django.contrib.auth import get_user_model

class UserAccountsTest(TestCase):

    def test_super_user(self):
        db = get_user_model()
        superuser = db.objects.create_superuser(email='test@gmail.com', user_name='username',
                                                first_name='firstname', password='password')
        self.assertEqual(superuser.email , 'test@gmail.com')
        self.assertEqual(superuser.user_name , 'username')
        self.assertEqual(superuser.first_name , 'firstname')
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_active)
        self.assertEqual(str(superuser), 'username')

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='email@gmail.com', user_name='test_username1', first_name='test_firstname', 
                password='password', is_superuser=False
            )
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='email@gmail.com', user_name='test_username1', first_name='test_firstname', 
                password='password', is_staff=False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='email@gmail.com', user_name='test_username1', first_name='test_firstname', 
                password='password', is_active=False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='', user_name='test_username1', first_name='test_firstname', 
                password='password', is_superuser=True
            )

    def test_user(self):
        db = get_user_model()
        user = db.objects.create_user(email='normal_user@gmail.com', user_name='username',
                                first_name='firstname', password='password')
        self.assertEqual(user.email, 'normal_user@gmail.com')
        self.assertEqual(user.first_name, 'firstname')
        self.assertEqual(user.user_name, 'username')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

        with self.assertRaises(ValueError):
            db.objects.create_user(email='', user_name='username', first_name='first_name', password='ps')
        