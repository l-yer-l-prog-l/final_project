from django.contrib import admin
from .models import *
from django.contrib import admin


# Register your models here.


class TaskAdmin(admin.ModelAdmin):
	list_display = ["title", "discipline"]

	class Meta:
		model = Task


class AnswerAdmin(admin.ModelAdmin):
	list_display = ["title", "date_of_finish"]

	class Meta:
		model = Answer


class DisciplineAdmin(admin.ModelAdmin):
	list_display = ["title"]

	class Meta:
		model = Discipline


class MarkAdmin(admin.ModelAdmin):
	list_display = ["mark", "answer"]

	class Meta:
		model = Mark


class TimetableAdmin(admin.ModelAdmin):
	list_display = ('group', 'time', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')


class RatingAdmin(admin.ModelAdmin):
	list_display = ('user', 'rating')

admin.site.register(Group)
admin.site.register(Task, TaskAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Mark, MarkAdmin)
admin.site.register(Timetable, TimetableAdmin)
admin.site.register(Profile)
admin.site.register(RatingTeacher, RatingAdmin)

