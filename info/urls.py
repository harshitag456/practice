from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$',views.details,name='details'),
        url(r'^(?P<list_id>[0-9]+)/$',views.index,name='index')

]
