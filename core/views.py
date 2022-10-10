from django.shortcuts import render

# Create your views here.

# import viewsets
from rest_framework import viewsets
  
# import local data
from .serializers import DeletePostSerializer, EbookSerializer
from .models import Ebook
  
# create a viewset
class Ebookviewset(viewsets.ModelViewSet):
    # define queryset
    queryset = Ebook.objects.all()
    # specify serializer to be used
    serializer_class = EbookSerializer

class DeletePostViewSet(viewsets.ModelViewSet):
    queryset = Ebook.objects.all()
    serializer_class = DeletePostSerializer
    # permission_classes = (IsAuthenticated,)
    http_method_names = ['delete', ]

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        # you custom logic #
        return super(DeletePostViewSet, self).destroy(request, pk, *args, **kwargs)