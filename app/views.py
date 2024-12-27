from django.shortcuts import render
from django.db.models import Q
from .models import Book
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView



class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            # Ищем по названию и автору (регистр не учитывается)
            return Book.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query)
            )
        return Book.objects.all()
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