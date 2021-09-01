from django.urls import path
from django.urls.resolvers import URLPattern
from .views import HomeView, RecordListView, RecordDetailView, RecordCreateView, RecordUpdateView, RecordDeleteView


urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('record_list/', RecordListView.as_view(), name='record_list'),
  path('<int:pk>/', RecordDetailView.as_view(), name='record_detail'),
  path('create/', RecordCreateView.as_view(), name='create_record'),
  path('<int:pk>/update/', RecordUpdateView.as_view(), name='update_record'),
  path('<int:pk>/delete/', RecordDeleteView.as_view(), name='delete_record'),
]