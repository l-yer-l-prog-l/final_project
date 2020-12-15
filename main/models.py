from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
	user = models.OneToOneField(User, related_name='profile', null=True, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	group = models.ForeignKey('Group', on_delete=models.SET_NULL, blank=True, null=True)
	discipline = models.ForeignKey('Discipline', on_delete=models.SET_NULL, blank=True, null=True)
	rating = models.ForeignKey('RatingTeacher', on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()


class RatingTeacher(models.Model):
	user = models.ForeignKey(User, related_name='rating', null=True, blank=True, on_delete=models.CASCADE)

	class Rating(models.IntegerChoices):
		One = 1
		Two = 2
		Three = 3
		Four = 4
		Five = 5

	rating = models.IntegerField(choices=Rating.choices, default=1)

	def __str__(self):
		return str(self.rating)


class Discipline(models.Model):
	title = models.CharField('Урок', max_length=100)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Дисциплина'
		verbose_name_plural = 'Дисциплины'


class Task(models.Model):
	title = models.CharField('Задание', max_length=100)
	description = models.TextField('Описание')
	date_of_start = models.DateField('Дата начала')
	date_of_finish = models.DateField('Дата завершения', null=True)
	discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Задание'
		verbose_name_plural = 'Задания'


class Answer(models.Model):
	title = models.CharField('Заголовок', max_length=50)
	description = models.TextField('Описание')
	date_of_finish = models.DateField('Дата завершения', auto_now=True)
	task = models.ForeignKey('Task', on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Ответ'
		verbose_name_plural = 'Ответы'


class Mark(models.Model):
	mark = models.IntegerField('Оценка')
	answer = models.OneToOneField(Answer, on_delete=models.CASCADE)

	def __int__(self):
		return self.mark

	class Meta:
		verbose_name = 'Оценка'
		verbose_name_plural = 'Оценки'


class Group(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Группа(учебная)'
		verbose_name_plural = 'Группы(учебная)'


class Timetable(models.Model):
	group = models.ForeignKey("Group", on_delete=models.CASCADE, null=True, blank=True)
	time = models.CharField(max_length=50)
	monday = models.ForeignKey('Discipline', related_name='Timetable.monday+', on_delete=models.CASCADE)
	tuesday = models.ForeignKey('Discipline', related_name='Timetable.tuesday+', on_delete=models.CASCADE)
	wednesday = models.ForeignKey('Discipline', related_name='Timetable.wednesday+', on_delete=models.CASCADE)
	thursday = models.ForeignKey('Discipline', related_name='Timetable.thursday+', on_delete=models.CASCADE)
	friday = models.ForeignKey('Discipline', related_name='Timetable.friday+', on_delete=models.CASCADE)
	saturday = models.ForeignKey('Discipline', related_name='Timetable.saturday+', on_delete=models.CASCADE)
	sunday = models.ForeignKey('Discipline', related_name='Timetable.sunday+', on_delete=models.CASCADE)

	def __str__(self):
		return str(self.group)

	class Meta:
		verbose_name = 'Расписание'
		verbose_name_plural = 'Расписание'



#     ----- Day Time Discipline -----

