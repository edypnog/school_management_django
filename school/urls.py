from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("students/", views.student_list, name="student_list"),
    path("students/<int:pk>/", views.student_detail, name="student_detail"),
    path("students/create", views.student_create, name="student_create"),
    path("students/update/<int:pk>/", views.student_update, name="student_update"),
    path("students/delete/<int:pk>/", views.student_delete, name="student_delete"),
    # ! courses path
    path("courses/", views.course_list, name="course_list"),
    path("courses/<int:pk>/", views.course_detail, name="course_detail"),
    path("courses/create", views.course_create, name="course_create"),
    path("courses/update/<int:pk>/", views.course_update, name="course_update"),
    path("courses/delete/<int:pk>/", views.course_delete, name="course_delete"),
    # ! cta
    path("cta/", views.cta_view, name="cta_view"),
]
