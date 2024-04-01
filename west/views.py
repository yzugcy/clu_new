from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from course.models import Course, CourseContent, CourseContentReadStatus


class WestView(View):
    """ game view """
    template_name = 'west/west.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)
