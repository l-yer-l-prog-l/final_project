from django.test import TestCase
from main.models import Discipline, Task
from django.contrib.auth.models import User


class DisciplineModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Discipline.objects.create(title='Math')

    def test_title_label(self):
        discipline = Discipline.objects.get(id=1)
        field_label = discipline._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'Урок')


class TaskModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        discipline = Discipline.objects.create(title="Math")
        Task.objects.create(title="New task", description="New description", date_of_start="2020-12-15", date_of_finish="2020-12-16", discipline=discipline)

    def test_title_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Задание')

    def test_description_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Описание')

    def test_date_of_start_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('date_of_start').verbose_name
        self.assertEquals(field_label, 'Дата начала')

    def test_date_of_finish_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('date_of_finish').verbose_name
        self.assertEquals(field_label, 'Дата завершения')

    def test_discipline_null    (self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('discipline').null
        self.assertEquals(field_label, False)