from django.shortcuts import render, redirect, get_object_or_404
from subjects.models import Subject
from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'teachers/teachers-list.html', ctx)


def teacher_create(request):
    subjects = Subject.objects.all()
    errors = []

    if request.method == 'POST':
        # Collect data from POST
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject_id = request.POST.get('subject')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        work_experience = request.POST.get('work_experience')
        images = request.FILES.get('images')

        # Debugging log (optional)
        print(f"POST data: {request.POST}")

        # Validate required fields
        if not (first_name and last_name and subject_id and phone_number and email and work_experience and images):
            errors.append("All fields are required.")
        try:
            subject = Subject.objects.get(pk=subject_id)
        except Subject.DoesNotExist:
            errors.append("Invalid subject selected.")

        # Save teacher if no errors
        if not errors:
            Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                subject=subject,
                phone_number=phone_number,
                email=email,
                work_experience=work_experience,
                images=images
            )
            return redirect('teachers:teacher_list')

    ctx = {'subjects': subjects, 'errors': errors}
    return render(request, 'teachers/teacher-add.html', ctx)


def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    ctx = {'teacher': teacher}
    return render(request, 'teachers/teacher-detail.html', ctx)


def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    subjects = Subject.objects.all()
    errors = []

    if request.method == 'POST':
        # Collect data from POST
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject_id = request.POST.get('subject')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        work_experience = request.POST.get('work_experience')
        images = request.FILES.get('images')

        # Validate required fields
        if not (first_name and last_name and subject_id and phone_number and email and work_experience):
            errors.append("All fields are required.")
        try:
            subject = Subject.objects.get(pk=subject_id)
        except Subject.DoesNotExist:
            errors.append("Invalid subject selected.")

        # Update teacher if no errors
        if not errors:
            teacher.first_name = first_name
            teacher.last_name = last_name
            teacher.subject = subject
            teacher.phone_number = phone_number
            teacher.email = email
            teacher.work_experience = work_experience
            if images:
                teacher.images = images
            teacher.save()
            return redirect('teachers:teacher_detail', pk=teacher.pk)

    ctx = {'teacher': teacher, 'subjects': subjects, 'errors': errors}
    return render(request, 'teachers/teacher-add.html', ctx)


def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('teachers:teacher_list')
