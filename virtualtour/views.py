from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from virtualtour.models import Tour


class VirtualTourListView(ListView):
    """ Course view """
    template_name = 'virtualtour/list.html'
    model = Tour

    def get_queryset(self, **kwargs):
        self.tour_list = self.model.objects.all().order_by('-pk')
        return self.tour_list

    def get_context_data(self, **kwargs):
        context = super(VirtualTourListView, self).get_context_data(**kwargs)
        context['total_count'] = self.tour_list.count()
        return context


class VirtualTourDetailsView(View):
    template_name = 'virtualtour/details.html'
    model = Tour

    def get(self, request, *args, **kwargs):
        tour = get_object_or_404(self.model, slug=self.kwargs['slug'])
        context = {
            'tour': tour
        }
        return render(request, self.template_name, context)
