from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product, Comments
from .serializers import ProductSerializer, CommentSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class InventoryList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )
    lookup_url_kwarg = 'product_id'


class InventoryDetail(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )
    lookup_url_kwarg = 'product_id'


class CommentsList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    lookup_url_kwarg = 'product_id'

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, product_id=self.kwargs['product_id'])

    def get_queryset(self):
        product = self.kwargs['product_id']
        return Comments.objects.filter(product__id=product)


class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    lookup_url_kwarg = 'comment_id'

    def get_queryset(self):
        comment = self.kwargs['comment_id']
        return Comments.objects.filter(id=comment)