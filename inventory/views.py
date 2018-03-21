from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product, Comments
from .serializers import ProductSerializer, CommentSerializer
from .permissions import IsAdminOrReadOnly


class InventoryList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )


class InventoryDetail(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )


class CommentsList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, product_id=self.kwargs['pk'])
