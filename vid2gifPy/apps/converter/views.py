from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import CreateView, DetailView
from .models import ConvertVidRequestModel
from django.core.urlresolvers import reverse
from .services import VidConvertService


class ConvertVidRequestCreateView(CreateView):
    model = ConvertVidRequestModel
    fields = ('is_loop', 'vid_file')

    def form_valid(self, form):
        response = super(ConvertVidRequestCreateView, self).form_valid(form)
        service = VidConvertService()
        service.convert_to_gif(self.object.vid_file.name, self.object.id)
        return response

    def get_success_url(self):
        return reverse('convertvidrequest_details', args=(self.object.id,))


class ConvertVidRequestDetailsView(DetailView):
    model = ConvertVidRequestModel
