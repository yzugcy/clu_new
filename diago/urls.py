from django.urls import path

from course import views
from diago import views

app_name = "diago"


urlpatterns = [
    path("", views.DiagoView.as_view(), name="diago"),

    # path(
    #     '<int:pk>/details/', views.CourseDetailsView.as_view(),
    #     name='details'
    # )
]
