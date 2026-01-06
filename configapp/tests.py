from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):

    def setUp(self):
        # Test user yaratamiz
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        # Test post yaratamiz
        self.post = Post.objects.create(
            title='Yangi post',
            body='Bu post matni test uchun yozilgan',
            author=self.user
        )

    # Post modeli string ko‘rinishini tekshirish
    def test_string_representation(self):
        post = Post(title='Post mavzusi')
        self.assertEqual(str(post), post.title)

    # Post mazmunini tekshirish
    def test_post_content(self):
        self.assertEqual(self.post.title, 'Yangi post')
        self.assertEqual(self.post.body, 'Bu post matni test uchun yozilgan')
        self.assertEqual(self.post.author.username, 'testuser')

    # Post list view ishlashini tekshirish
    def test_post_list_view(self):
        url = reverse('post_list')  # urls.py da post_list nomi bo‘lishi kerak
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertTemplateUsed(response, 'configapp/post_list.html')

    # Post detail view ishlashini tekshirish
    def test_post_detail_view(self):
        url = reverse('Post_detail', args=[self.post.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)
        self.assertTemplateUsed(response, 'configapp/post_detail.html')


from django.test import TestCase

# Create your tests here.
