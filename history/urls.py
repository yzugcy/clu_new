from django.urls import path

from course import views
from history import views

app_name = "history"


urlpatterns = [

    path('dynasty_song/', views.HistoryPagesongsView.as_view(), name="dynasty_song"),
    # path(
    #     '<int:pk>/details/', views.CourseDetailsView.as_view(),
    #     name='details'
    # )
]
