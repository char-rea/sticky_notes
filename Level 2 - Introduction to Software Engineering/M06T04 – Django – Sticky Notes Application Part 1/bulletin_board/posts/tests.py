from django.test import TestCase
from django.urls import reverse
from .models import Post, Author

# Test cases for the Post model and views in the bulletin board application
class PostModelTest(TestCase):
    def setUp(self):
        # Create an Author object
        author = Author.objects.create(name='Test Author')

        # Create a Post object for testing
        Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=author
        )

    def test_post_has_title(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Test Post')

    def test_post_has_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.content, 'This is a test post.')


class PostViewTest(TestCase):
    def setUp(self):
        # Create an Author object
        author = Author.objects.create(name='Test Author')

        # Create a Post object for testing views
        Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=author
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        post = Post.objects.get(id=1)
        response = self.client.get(
            reverse('post_detail', args=[post.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is a test post.')