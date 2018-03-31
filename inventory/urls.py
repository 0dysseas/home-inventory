from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'products/$', views.InventoryList.as_view(), name='product-list'),
    url(r'^products/(?P<product_id>[0-9]+)/$', views.InventoryDetail.as_view()),
    url(r'^products/(?P<product_id>[0-9]+)/comments/$', views.CommentsList.as_view()),
    url(r'^products/(?P<product_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)/$', views.CommentsDetail.as_view()),
]