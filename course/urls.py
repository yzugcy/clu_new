from django.urls import path

from course import views

app_name = "course"


urlpatterns = [
    path("", views.CourseListView.as_view(), name="list"),
    path(
        '<int:pk>/overview/', views.CourseOverviewView.as_view(),
        name='overview'
    ),
    path(
        '<int:pk>/content/', views.CourseContentView.as_view(),
        name='content'
    ),
]
