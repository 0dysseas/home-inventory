from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'products/$', views.InventoryList.as_view()),
url(r'^products/(?P<pk>[0-9]+)/$', views.InventoryDetail.as_view()),
]