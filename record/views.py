from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Record
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
  template_name = 'pages/home.html'

class RecordListView(ListView):
  template_name = 'pages/record_list.html'
  model = Record
  context_object_name = 'list_of_records'

class RecordDetailView(DetailView):
  template_name = 'pages/record_detail.html'
  model = Record

class RecordCreateView(CreateView):
  template_name = 'pages/create_record.html'
  model = Record
  fields = ['title', 'artist' ,'genre', 'added_by']
  #success_url = reverse_lazy('record_list')

class RecordUpdateView(UpdateView):
  template_name = 'pages/update_record.html'
  model = Record
  fields = ['title', 'artist' ,'genre', 'added_by']
  #success_url = reverse_lazy('record_list')

class RecordDeleteView(DeleteView):
  template_name = 'pages/delete_record.html'
  model = Record
  success_url = reverse_lazy('record_list')