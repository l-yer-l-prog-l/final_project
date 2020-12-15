from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Task, Discipline, Timetable
from .forms import AnswerForm, TeacherRatingForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


def index(request):
	return render(request, 'main/index.html')


@login_required
def task(request):
	tasks_list = Task.objects.all()
	paginator = Paginator(tasks_list, 3)
	page = request.GET.get('page')
	try:
		tasks = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer deliver the first page
		tasks = paginator.page(1)
	except EmptyPage:
		# If page is out of range deliver last page of results
		tasks = paginator.page(paginator.num_pages)
	return render(request, 'main/task.html', {'page': page, 'tasks': tasks})


@login_required
def answer(request):
	if request.method == 'POST':
		answer_form = AnswerForm(request.POST)
		if answer_form.is_valid():
			answer_form.save()
			return redirect('main')
	else:
		answer_form = AnswerForm()
	return render(request,
				  'main/answer.html',
				  {'task': task,
				   'answer_form': answer_form})


@login_required
def main(request):
	return render(request, 'main/main.html')


@login_required
def discipline(request):
	discipline_list = Discipline.objects.all()
	return render(request, 'main/discipline.html', {'discipline_list': discipline_list})


@login_required
def timetable(request):
	timetable = Timetable.objects.all()
	return render(request, 'main/timetable.html', {'timetable': timetable})


@login_required
def profile(request):
	return render(request, 'main/profile.html')


@login_required
def teachers_list(request):
	user = User.objects.all()
	return render(request, 'main/teachers_list.html', {'user': user})


@login_required
def teacher_rating(request, pk):
	user = User.objects.get(pk=pk)
	if request.method == "POST":
		form = TeacherRatingForm(request.POST)
		if form.is_valid():
			rating = form.save(commit=False)
			rating.save()
			return redirect('main')
	else:
		form = TeacherRatingForm()
	return render(request, 'main/teacher_rating.html', context={'user': user, 'form': form})



