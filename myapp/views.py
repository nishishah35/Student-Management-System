from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

import pandas as pd
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student
from .forms import StudentForm
from .serializer import StudentSerializer

def send_test_email(request):

    send_mail(
        'Test Subject',
        'Hello from Django',
        'admin@gmail.com',
        ['test@gmail.com'],
        fail_silently=False,
    )

    return HttpResponse("Email Sent")

def export_excel(request):

    students = Student.objects.all().values()

    df = pd.DataFrame(students)

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    response['Content-Disposition'] = 'attachment; filename=students.xlsx'

    df.to_excel(response, index=False)

    return response

# ---------------- API ---------------- #

@api_view(['GET'])
def student_api(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


# ---------------- HOME PAGE ---------------- #

@login_required
def home(request):

    search = request.GET.get('search')

    if search:
        students = Student.objects.filter(name__icontains=search)
    else:
        students = Student.objects.all()

    # Pagination
    paginator = Paginator(students, 5)

    page_number = request.GET.get('page')

    students = paginator.get_page(page_number)

    return render(request, 'index.html', {'students': students})


# ---------------- ADD STUDENT ---------------- #

@login_required
def add_student(request):

    form = StudentForm(request.POST or None,
                       request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'add.html', {'form': form})


# ---------------- UPDATE STUDENT ---------------- #

@login_required
def update_student(request, id):

    student = get_object_or_404(Student, id=id)

    form = StudentForm(request.POST or None,
                       request.FILES or None,
                       instance=student)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'add.html', {'form': form})


# ---------------- DELETE STUDENT ---------------- #

@login_required
def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()

    return redirect('/')