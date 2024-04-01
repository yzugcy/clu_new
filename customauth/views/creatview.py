from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from customauth.models import  Image

from customauth.forms import ImageForm

class ImageCreate(CreateView):
    model = Image
    form_class = ImageForm
    success_url = reverse_lazy('image-list')