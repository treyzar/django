from django.shortcuts import render
from .models import Book
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    template_name = "book_form.html"
    success_url = reverse_lazy('main')

class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
    template_name = "book_form.html"
    success_url = reverse_lazy('main')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete_confirm.html'
    success_url = reverse_lazy('main')