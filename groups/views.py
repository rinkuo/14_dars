from django.shortcuts import render, get_object_or_404, redirect
from .models import Group
from django.db import IntegrityError
from teachers.models import Teacher
from students.models import Student

def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'groups/groups-list.html', ctx)

def group_create(request):
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    error_message = None

    if request.method == 'POST':
        class_id = request.POST.get('class_leader')
        group_name = request.POST.get('group_name')
        student_ids = request.POST.getlist('students')

        if class_id and group_name:
            try:
                teacher = Teacher.objects.get(pk=class_id)
                group = Group.objects.create(
                    class_leader=teacher,
                    group_name=group_name
                )

                for student_id in student_ids:
                    student = Student.objects.get(pk=student_id)
                    group.students.add(student)

                return redirect('groups:group_list')
            except IntegrityError:
                error_message = "The selected teacher is already assigned as a class leader for another group."

    ctx = {
        'teachers': teachers,
        'students': students,
        'error_message': error_message
    }
    return render(request, 'groups/group-add.html', ctx)


def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    error_message = None

    if request.method == 'POST':
        class_leader_id = request.POST.get('class_leader')
        group_name = request.POST.get('group_name')
        student_ids = request.POST.getlist('students')

        if class_leader_id and group_name:
            try:
                class_leader = Teacher.objects.get(pk=class_leader_id)
                group.class_leader = class_leader
                group.group_name = group_name
                group.save()
                group.students.set(student_ids)
                return redirect(group.get_detail_url())
            except Teacher.DoesNotExist:
                error_message = "The selected teacher does not exist."

    ctx = {
        'group': group,
        'teachers': teachers,
        'students': students,
        'error_message': error_message,
    }
    return render(request, 'groups/group-add.html', ctx)

def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    student_count = group.students.count()
    context = {
        'group': group,
        'student_count': student_count,
    }
    return render(request, 'groups/group-detail.html', context)


def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()
    return redirect('groups:group_list')
