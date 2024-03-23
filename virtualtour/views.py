from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from course.models import Course, CourseContent, CourseContentReadStatus


class VirtualTourListView(ListView):
    """ Course view """
    template_name = 'virtualtour/list.html'
    model = Course

    def get_queryset(self, **kwargs):
        self.course_list = self.model.objects.all().order_by('-pk')
        return self.course_list

    def get_context_data(self, **kwargs):
        context = super(VirtualTourListView, self).get_context_data(**kwargs)
        context['total_count'] = self.course_list.count()
        return context


class VirtualTourDetailsView(View):
    template_name = 'virtualtour/details.html'

    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=self.kwargs['pk'])
        context = {
            'course': course
        }
        return render(request, self.template_name, context)
