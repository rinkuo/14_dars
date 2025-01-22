from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from .models import Subject
from teachers.models import Teacher


def subject_list(request):
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects}
    return render(request, 'subjects/subjects-list.html', ctx)


def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    ctx = {'subject': subject}
    return render(request, 'subjects/subject-detail.html', ctx)

def subject_create(request):
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        selected_teacher_ids = request.POST.getlist('teachers')

        if name:
            subject = Subject.objects.create(name=name)
            if selected_teacher_ids:  # Check if teachers are selected
                selected_teachers = Teacher.objects.filter(id__in=selected_teacher_ids)
                subject.teachers.set(selected_teachers)
            subject.save()
            return redirect('subjects:subject_list')
    return render(request, 'subjects/subject-add.html', {'teachers': teachers})


def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        selected_teacher_ids = request.POST.getlist('teachers')

        if name:
            subject.name = name
            if selected_teacher_ids:  # Update teachers if provided
                selected_teachers = Teacher.objects.filter(id__in=selected_teacher_ids)
                subject.teachers.set(selected_teachers)
            else:
                subject.teachers.clear()  # Clear teachers if none selected
            subject.save()
            return redirect(subject.get_detail_url())
    return render(request, 'subjects/subject-add.html', {'subject': subject, 'teachers': teachers})


def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    return redirect('subjects:subject_list')

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subjects/subject_detail.html'