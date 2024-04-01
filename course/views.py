from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from course.models import Course, CourseContent, CourseContentReadStatus


class CourseListView(ListView):
    """ Course view """
    template_name = 'course/course.html'
    model = Course

    def get_queryset(self, **kwargs):
        self.course_list = self.model.objects.all().order_by('-pk')
        return self.course_list

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        context['total_count'] = self.course_list.count()
        return context


class CourseDetailsView(View):
    template_name = 'course/course-details.html'

    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=self.kwargs['pk'])
        context = {
            'course': course
        }
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
