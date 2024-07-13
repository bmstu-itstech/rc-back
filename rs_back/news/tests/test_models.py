from django.core.exceptions import ValidationError
from django.test import TestCase

from rs_back.news.models import News


class NewsTestCase(TestCase):
    def setUp(self):
        News.objects.create(
            title='news1',
            description='description1',
            new_url='https://url.com',
            photo='1.png',
        ).save()

    def tearDown(self):
        News.objects.all().delete()
        super().tearDown()

    def test_create_good(self):
        item = News.objects.create(
            title='news2',
            description='description2',
            new_url='https://url.com',
            photo='2.png',
        )
        item.full_clean()
        item.save()
        self.assertEqual(News.objects.count(), 2)

    def test_create_bad(self):
        item = News.objects.create(
            title='news3',
            description='description3',
            new_url='https://url',
            photo='3.png',
        )
        try:
            item.full_clean()
            item.save()
        except ValidationError:
            item.delete()
        item = News.objects.create(
            description='description4',
            new_url='https://url.com',
            photo='4.png',
        )
        try:
            item.full_clean()
            item.save()
        except ValidationError:
            item.delete()
        self.assertEqual(News.objects.count(), 1)
