from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from course.models import Course, CourseContent, CourseContentReadStatus


class CourseListView(ListView):
    """ Course view """
    template_name = 'course/course.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class CourseOverviewView(LoginRequiredMixin, View):
    template_name = 'courses/overview.html'

    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=self.kwargs['pk'])
        context = {
            'course': course
        }
        return render(request, self.template_name, context)


class CourseContentView(LoginRequiredMixin, View):
    template_name = 'courses/learning.html'

    def get(self, request, *args, **kwargs):
        content = get_object_or_404(CourseContent, pk=self.kwargs['pk'])
        CourseContentReadStatus.objects.get_or_create(
            user=request.user,
            content=content,
            is_read=True
        )
        context = {
            'content': content,
            'course': content.course_module.course
        }
        return render(request, self.template_name, context)
