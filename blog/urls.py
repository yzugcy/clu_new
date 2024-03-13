from django.urls import path

from blog import views

app_name = "blog"


urlpatterns = [
    path("", views.BlogListView.as_view(), name="list"),
]
