from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import *


class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='python')
        test_user1 = User.objects.create_user(
            username='test01', password='12345678'
        )
        test_post = Post.objects.create(
            category_id=1, title='Title test', excerpt='Post excerpt',
            content='The content of post', slug='post-title',
            author_id=1, status='published'
        )

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        cate = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'test01')
        self.assertEqual(title, 'Title test')
        self.assertEqual(content, 'The content of post')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'Title test')
        self.assertEqual(str(cate), 'python')
