from django.urls import path

from course import views
from readclassic import views

app_name = "readclassic"


urlpatterns = [
    path("<email>/", views.ClassicsharingPagegameView.as_view(), name="cs"),
    path('lfs/', views.LearnFamousPagesongsView.as_view(), name="lfs"),
    path(
        '<int:id>/sdetails/', views.SharingDetailsView.as_view(),
        name='sdetails'
        ),
    path(
        '<int:id>/<int:likes>/sdetailsa/', views.SharingDetails_saveView.as_view(),
        name='sdetailsup'
    ),
    path(
        '<int:id>/<int:classicid>/sdetails/', views.SharingDetails_delete_commentView.as_view(),
        name='sdetailsde'
    ),
    path(
        '<int:id>/<email>/sdetailsb/', views.SharingDetails_delete_classicView.as_view(),
        name='sdetaildeclassic'
    ),

]
