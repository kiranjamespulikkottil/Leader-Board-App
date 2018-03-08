from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . models import Score

class ScoreListView(ListView):
    model = Score
    template_name = 'home.html'

class ScoreDetailView(DetailView):
    model = Score
    template_name = 'score_detail.html'

class ScoreAddView(CreateView):
    model = Score
    template_name = 'score_add.html'
    fields = '__all__'

class ScoreUpdateView(UpdateView):
    model = Score
    fields = ['name', 'score']
    template_name = 'score_edit.html'

class ScoreDeleteView(DeleteView):
    model = Score
    template_name = 'score_delete.html'
    success_url = reverse_lazy('home')
