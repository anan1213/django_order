from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import BookInfo
from .forms import CreateImageForm
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.contrib import messages

from .func import get_asin_isbn
from .func import get_image_url

class ListImageView(generic.ListView):
    model = BookInfo
    template_name = 'book/index.html'

    def get_context_data(self, **kwargs):
        """This function creates a dictionary to be passed to html.
           Returns: context
        """
        new_context= []
        context = super().get_context_data(**kwargs)
        Books = BookInfo.objects.all()
        print(type(Books))
        for object in Books:
            print(object.amazon_url)
            amazon_url = object.amazon_url
            asin = get_asin_isbn(amazon_url)
            print(asin)
            try:
                image_url = get_image_url(asin)
            except:
                pass
            if image_url:
                object.img_url = image_url
            else:
                pass
        context['names'] = Books


        return context


class CreateImageView(generic.CreateView):
    model = BookInfo
    template_name = 'book/create_book.html'
    form_class = CreateImageForm
    success_url = reverse_lazy('book:index')

"""
@require_POST
def deleteImage(request):
    delete_id = request.POST['delete_id']
    if delete_id:
        Url.objects.filter(id=delete_id).delete()
    return redirect('book:index')
"""

@require_POST
def delete_book(request):
    delete_id = request.POST['delete_id']
    if delete_id:
        BookInfo.objects.filter(id=delete_id).delete()
    return redirect('book:index')
