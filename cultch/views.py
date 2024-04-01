from django.views.generic import View
from django.shortcuts import render

from course.models import Course


class HomePageView(View):
    """ Home view """
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        context = {
            'courses': courses
        }
        return render(request, self.template_name, context)

class GameView(View):
        """ game view """
        template_name = 'game.html'

        def get(self, request, *args, **kwargs):
            return render(request, self.template_name)