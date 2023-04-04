from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Books
from .serializers import BookSerializer
from rest_framework import generics


# Create your views here.
class BookListApi(APIView):

    def get(self, request):
        books = Books.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status": f"Returned {len(books)} books",
            'books': serializer_data
        }

        return Response(data)


# Bu hammasini get qilish uchun
# class BookListApi(generics.ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer


# bu id orqali get qilish uchun
class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BookCreateApiView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BookListCreate(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookViewset(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
