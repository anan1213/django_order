from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import SubClass, Url
from .forms import CreateFormUrl, CreateFormSubclass
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.contrib import messages

class IndexViewSubclass(generic.ListView):
    model = SubClass
    template_name = 'url/subclass_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subclasses'] = SubClass.objects.all()
        return context

class IndexViewUrl(generic.ListView):
    model = Url
    template_name = 'url/url_list.html'


    def get_queryset(self):
        queryset = super().get_queryset()
        detail = get_object_or_404(SubClass, subclass=self.kwargs['get_name'])
        queryset = queryset.filter(subclass=detail)

        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        context['title_name'] = get_object_or_404(SubClass, subclass=self.kwargs['get_name'])
        return context


class CreateViewUrl(generic.CreateView):
    model = Url
    template_name = 'url/url_create_form.html'
    success_url = reverse_lazy('url:index')
    form_class = CreateFormUrl



class CreateViewSubclass(generic.CreateView):
    model = SubClass
    template_name = 'url/subclass_create_form.html'
    success_url = reverse_lazy('url:index')
    form_class = CreateFormSubclass

'''
class DeleteViewSubclass(generic.DeleteView):
    model = SubClass
    templete_name = 'url/delete_category_'
'''

@require_POST
def deleteUrl(request):
    delete_id = request.POST['delete_id']
    if delete_id:
        Url.objects.filter(id=delete_id).delete()
    return redirect('url:index')



def deleteSubclass(request):
    delete_id = request.POST['delete_id']
    if delete_id:
        subclass = SubClass.objects.get(id=delete_id)
        url_exit = Url.objects.filter(subclass=subclass)
        if url_exit:
            def form_invalid(self, form):
                messages.error(self.request, 'ファイルが空じゃありません')
                return super().form_invalid(form)
        else:
            SubClass.objects.filter(id=delete_id).delete()
    return redirect('url:index')
