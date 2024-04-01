from django.urls import path

from virtualtour import views

app_name = "vt"


urlpatterns = [
    path("", views.VirtualTourListView.as_view(), name="list"),
    path(
        '<str:slug>/explore/', views.VirtualTourDetailsView.as_view(),
        name='details'
    ),

    path(
        'sharevideo/', views.VirtualTourShareVideoView.as_view(),
        name='sharevideo'
    ),
]
