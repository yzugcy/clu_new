from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from course.models import Course, CourseContent, CourseContentReadStatus



class DiagoView(View):
    """ game view """
    template_name = 'diago/diago.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):
        context = {}
        input_1 = request.POST.get('input_num')
        input_2 = request.POST.get('input_value')
        context = {"input_1": input_1, "input_2": input_2}
        print(input_1)
        print(input_2)
        return HttpResponse(input_2)#input_1输入框位置  input_2输入框内容
