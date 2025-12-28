from django.test import TestCase
from django.urls import reverse 
from .models import Post
from django.contrib.auth.models import User
# Create your tests here.
class PostMOdelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        Post.objects.create(title='Mavzu', text='yangilik matni')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_title=f'{post.title}'
        expected_object_text=f'{post.text}'
        self.assertEqual(expected_object_title,'Mavzu')
        self.assertEqual(expected_object_text,'yangilik matni')

class HomePageViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='adminuser', password='password123')
        post=Post.objects.create(title='Mavzu2', text='yangilik matni')

    def test_views_url_exists_at_proper_location(self):
        resp=self.client.get('/')
        self.assertEqual(resp.status_code,200)
    
    def test_view_uses_correct_template(self):
        resp=self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp, 'home.html')
    def test_post_list_on_hompage(self):
        resp = self.client.get(reverse('home'))
        self.assertContains(resp, 'yangilik matni')
