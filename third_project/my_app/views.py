from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from my_app import models
from django.urls import reverse_lazy
# Create your views here.
class IndexView(TemplateView):
    template_name = 'my_app/index.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['context_1'] = "message 1"
            context['context_2'] = "message 2"
            return context
class Home(ListView):
      context_object_name = 'musician_list'
      model = models.Musician
      template_name = 'my_app/index.html'

class MusicianDetails(DetailView):
      context_object_name = 'musician'
      model = models.Musician
      template_name = 'my_app/musician_details.html'
class AddMusician(CreateView):
      fields = ('name', 'age')
      template_name = 'my_app/musician_form.html'
      model = models.Musician

class UpdateMusician(UpdateView):
      fields = ('name', 'age')
      model = models.Musician
      template_name = 'my_app/musician_form.html'

class DeleteMusician(DeleteView):
    context_object_name = 'musician'
    model = models.Musician
    success_url = reverse_lazy("my_app:index")
    template_name = 'my_app/delete_musician.html'
