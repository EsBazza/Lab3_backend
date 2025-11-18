from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from .models import UserRegistration


class LoginViewTests(TestCase):
    """Test cases for the login view functionality"""
    
    def setUp(self):
        """Set up test user for login tests"""
        self.client = Client()
        self.login_url = reverse('registration:login_html')
        self.users_url = reverse('registration:users_html')
        
        # Create a test user
        self.test_user = UserRegistration.objects.create(
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            password=make_password('testpass123'),
            gender='Male'
        )
    
    def test_login_page_loads(self):
        """Test that the login page loads successfully"""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertContains(response, 'email')
        self.assertContains(response, 'password')
    
    def test_login_with_valid_credentials(self):
        """Test login with valid credentials redirects to users page"""
        response = self.client.post(self.login_url, {
            'email': 'testuser@example.com',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.users_url)
        # Check session was created
        self.assertIn('user_id', self.client.session)
        self.assertEqual(self.client.session['user_name'], 'Test User')
    
    def test_login_with_invalid_email(self):
        """Test login with invalid email shows error"""
        response = self.client.post(self.login_url, {
            'email': 'nonexistent@example.com',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid credentials')
    
    def test_login_with_invalid_password(self):
        """Test login with invalid password shows error"""
        response = self.client.post(self.login_url, {
            'email': 'testuser@example.com',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid credentials')
    
    def test_login_with_empty_fields(self):
        """Test login with empty fields shows error"""
        response = self.client.post(self.login_url, {
            'email': '',
            'password': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Enter both email and password')


class UsersListViewTests(TestCase):
    """Test cases for the users list view"""
    
    def setUp(self):
        """Set up test data for users list tests"""
        self.client = Client()
        self.users_url = reverse('registration:users_html')
        self.login_url = reverse('registration:login_html')
        
        # Create test users
        self.user1 = UserRegistration.objects.create(
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            password=make_password('pass123'),
            gender='Male'
        )
        self.user2 = UserRegistration.objects.create(
            first_name='Jane',
            last_name='Smith',
            email='jane@example.com',
            password=make_password('pass123'),
            gender='Female'
        )
    
    def test_users_list_requires_login(self):
        """Test that users list page requires login"""
        response = self.client.get(self.users_url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(self.login_url))
    
    def test_users_list_displays_after_login(self):
        """Test that users list displays correctly after login"""
        # Login first
        self.client.post(self.login_url, {
            'email': 'john@example.com',
            'password': 'pass123'
        })
        
        # Access users list
        response = self.client.get(self.users_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/users_list.html')
        self.assertContains(response, 'John')
        self.assertContains(response, 'Jane')
        self.assertContains(response, 'john@example.com')
        self.assertContains(response, 'jane@example.com')


class TemplateConfigurationTests(TestCase):
    """Test cases to verify template configuration"""
    
    def test_login_template_exists(self):
        """Test that login template can be found"""
        from django.template.loader import get_template
        try:
            template = get_template('registration/login.html')
            self.assertIsNotNone(template)
        except Exception as e:
            self.fail(f"Login template not found: {e}")
    
    def test_users_list_template_exists(self):
        """Test that users list template can be found"""
        from django.template.loader import get_template
        try:
            template = get_template('registration/users_list.html')
            self.assertIsNotNone(template)
        except Exception as e:
            self.fail(f"Users list template not found: {e}")


class UserRegistrationModelTests(TestCase):
    """Test cases for UserRegistration model"""
    
    def test_user_creation(self):
        """Test creating a user"""
        user = UserRegistration.objects.create(
            first_name='Test',
            last_name='User',
            email='test@example.com',
            password=make_password('password'),
            gender='Male'
        )
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
        self.assertEqual(user.email, 'test@example.com')
        self.assertIsNotNone(user.date_registration)
    
    def test_user_string_representation(self):
        """Test the string representation of a user"""
        user = UserRegistration.objects.create(
            first_name='Test',
            last_name='User',
            email='test@example.com',
            password='password',
            gender='Male'
        )
        self.assertEqual(str(user), 'TestUser')

