from django.urls import path
from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView
urlpatterns = [
    path('', BookListView.as_view(), name = 'main'),
    path('create', BookCreateView.as_view(), name='create'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='update'),
    path('books/', BookListView.as_view(), name='book-list'),
    
]
