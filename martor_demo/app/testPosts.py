from django.test import TestCase
from app.models import Post


class PostTestCase(TestCase):

    def testPost(self):
        post = Post(title="title", description="blurba", wiki="body")
        self.assertEqual(post.title, "title")
        self.assertEqual(post.description, "blurba")
        self.assertEqual(post.wiki, "body")
