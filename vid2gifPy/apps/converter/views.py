from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import CreateView, DetailView, ListView
from .models import ConvertVidRequestModel
from django.core.urlresolvers import reverse
from .services import VidConvertService
from datetime import datetime

class ConvertVidRequestCreateView(CreateView):
    model = ConvertVidRequestModel
    fields = ('loop_mode', 'size', 'quality', 'speed', 'caption', 'caption_position', 'vid_file')

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.creation_date = datetime.now()
        self.object.save()
        service = VidConvertService()
        self.object.result_file_name = service.convert_to_gif(self.object.vid_file.name, self.object.id, self.object.size, self.object.speed, self.object.quality, self.object.loop_mode, self.object.caption_position, self.object.caption)
        self.object.save()
        return super(ConvertVidRequestCreateView, self).form_valid(form);

    def get_success_url(self):
        return reverse('convertvidrequest_details', args=(self.object.id,))


class ConvertVidRequestDetailsView(DetailView):
    model = ConvertVidRequestModel

class ConvertVidRequestListView(ListView):
    model = ConvertVidRequestModel