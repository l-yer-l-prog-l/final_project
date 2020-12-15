from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('task', views.task, name='task'),
	path('main', views.main, name='main'),
	path('answer', views.answer, name='answer'),
	path('discipline', views.discipline, name='discipline'),
	path('profile', views.profile, name='profile'),
	path('timetable', views.timetable, name='timetable'),
	path('teachers_list', views.teachers_list, name='teachers_list'),
	path('teacher/<int:pk>', views.teacher_rating, name='teacher_rating'),
]