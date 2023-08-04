from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course
from .forms import StudentForm, CourseForm


def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "student_detail.html", {"student": student})


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "student_form.html", {"form": form})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)
    return render(request, "student_form.html", {"form": form})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    return render(redirect, "student_confirm_delete.html", {student: "student"})


# ! implement views and forms for Courses CRUD operations


def course_list(request):
    courses = Course.objects.all()
    return render(request, "course_list.html", {"courses": courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, "course_detail.html", {"course": course})


def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm()
    return render(request, "course_form.html", {"form": form})


def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm(instance=course)
    return render(request, "course_form.html", {"form": form})


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.delete()
        return redirect("course_list")
    return render(redirect, "course_confirm_delete.html", {course: "student"})


def cta_view(request):
    return render(request, "cta.html")
