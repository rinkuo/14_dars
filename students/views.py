from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from groups.models import Group
from subjects.models import Subject
from teachers.models import Teacher


def home(request):
    student_count = Student.objects.count()
    teacher_count = Teacher.objects.count()
    group_count = Group.objects.count()
    subject_count = Subject.objects.count()

    return render(request, 'index.html', {
        'student_count': student_count,
        'teacher_count': teacher_count,
        'group_count': group_count,
        'subject_count': subject_count,
    })


def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/students-list.html', ctx)


def student_create(request):
    groups = Group.objects.all()
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        group_id = request.POST.get('group')
        birth_date = request.POST.get('birth_date')
        images = request.FILES.get('images')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        if first_name and last_name and group_id and birth_date and images and phone_number and address:
            try:
                group = Group.objects.get(pk=group_id)
            except Group.DoesNotExist:
                ctx = {'groups': groups, 'error': "Invalid group selected."}
                return render(request, 'students/student-add.html', ctx)

            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                group=group,
                birth_date=birth_date,
                images=images,
                phone_number=phone_number,
                address=address,
            )
            return redirect('students:student_list')
    ctx = {'groups': groups}
    return render(request, 'students/student-add.html', ctx)


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    groups = Group.objects.all()
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        group_id = request.POST.get('group')
        birth_date = request.POST.get('birth_date')
        images = request.FILES.get('images')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        if first_name and last_name and group_id and birth_date and images and phone_number and address:
            try:
                group = Group.objects.get(pk=group_id)
            except Group.DoesNotExist:
                ctx = {'student': student, 'groups': groups, 'error': "Invalid group selected."}
                return render(request, 'students/student-add.html', ctx)

            student.first_name = first_name
            student.last_name = last_name
            student.group = group
            student.birth_date = birth_date
            student.images = images
            student.phone_number = phone_number
            student.address = address
            student.save()
            return redirect(student.get_detail_url())
    ctx = {'student': student, 'groups': groups}
    return render(request, 'students/student-add.html', ctx)


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    ctx = {'student': student}
    return render(request, 'students/student-detail.html', ctx)


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('students:student_list')
