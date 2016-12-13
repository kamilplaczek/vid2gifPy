from django.conf.urls import url
from . import views
from .views import ConvertVidRequestCreateView, ConvertVidRequestDetailsView, ConvertVidRequestListView

urlpatterns = [
    url(r'^$', ConvertVidRequestCreateView.as_view(success_url="/")),
    url(r'^(?P<pk>\d+)$', ConvertVidRequestDetailsView.as_view(), name='convertvidrequest_details'),
    url(r'^gifs/', ConvertVidRequestListView.as_view(), name='convertvidrequest_list'),
]