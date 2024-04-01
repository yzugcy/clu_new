from django.urls import path

from course import views
from west import views

app_name = "west"


urlpatterns = [
    path("", views.WestView.as_view(), name="west"),

    # path(
    #     '<int:pk>/details/', views.CourseDetailsView.as_view(),
    #     name='details'
    # )
]
