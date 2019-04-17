from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Pdf
from .forms import CreatePdfForm
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.contrib import messages


class ListPdfView(generic.ListView):
    model = Pdf
    template_name = 'pdf/index.html'

    def get_context_data(self, **kwargs):
        """This function creates a dictionary to be passed to html.
           Returns: context
        """
        context = super().get_context_data(**kwargs)
        context['pdfs'] = Pdf.objects.all()
        return context


class CreatePdfView(generic.CreateView):
    model = Pdf
    template_name = 'pdf/create_pdf.html'
    form_class = CreatePdfForm
    success_url = reverse_lazy('pdf:index')
