from django.views.generic import ListView
from django.shortcuts import render


class BlogListView(ListView):
    """ Blog view """
    template_name = 'blog/blog.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
