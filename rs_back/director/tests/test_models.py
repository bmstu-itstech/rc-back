from django.core.exceptions import ValidationError
from django.test import TestCase

from rs_back.director.models import Director


class DirectorTestCase(TestCase):
    def setUp(self):
        Director.objects.create(
            fio='director1',
            email='abc@mail.ru',
            role='post1',
            photo='1.png',
        ).save()

    def tearDown(self):
        Director.objects.all().delete()
        super().tearDown()

    def test_create_good(self):
        item = Director.objects.create(
            fio='director2',
            email='abc2@mail.ru',
            role='post2',
            photo='2.png',
        )
        item.full_clean()
        item.save()
        self.assertEqual(Director.objects.count(), 2)

    def test_create_bad(self):
        item = Director.objects.create(
            fio='director3',
            email='mail.ru',
            role='post3',
            photo='3.png',
        )
        try:
            item.full_clean()
            item.save()
        except ValidationError:
            item.delete()
        item = Director.objects.create(
            fio='director4',
            email='abc4',
            role='post4',
            photo='4.png',
        )
        try:
            item.full_clean()
            item.save()
        except ValidationError:
            item.delete()
        item = Director.objects.create(
            fio='director5',
            email='abc5@mail.ru',
            photo='5.png',
        )
        try:
            item.full_clean()
            item.save()
        except ValidationError:
            item.delete()
        self.assertEqual(Director.objects.count(), 1)
