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

        if not all([first_name, last_name, group_id, birth_date, images, phone_number, address]):
            ctx = {'groups': groups, 'error': "All fields are required."}
            return render(request, 'students/student-add.html', ctx)

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
        full_name = request.POST.get('fullName')
        group_id = request.POST.get('group')
        birth_date = request.POST.get('birth_date')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        photo = request.FILES.get('photo')

        if not full_name or not group_id or not birth_date or not phone or not address:
            ctx = {'student': student, 'groups': groups, 'error': "All fields are required."}
            return render(request, 'students/student-add.html', ctx)

        try:
            student.first_name, student.last_name = full_name.split(' ', 1)
        except ValueError:
            ctx = {'student': student, 'groups': groups, 'error': "Invalid full name format."}
            return render(request, 'students/student-add.html', ctx)

        student.group = Group.objects.get(id=group_id)
        student.birth_date = birth_date
        student.phone_number = phone
        student.address = address
        if photo:
            student.images = photo
        student.save()

        return redirect('students:student_list')

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
