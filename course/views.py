from django.views.generic import ListView
from django.shortcuts import render


class CourseListView(ListView):
    """ Course view """
    template_name = 'course/course.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
