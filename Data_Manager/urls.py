from django.urls import path

from .views import Environment_list, EnvironmentDeleteView, EnvironmentDetailView, EnvironmentUpdateView, EnvironmentCreateView, EnvironmentBulkUploadView, downloadcsv

urlpatterns = [
  path('list', Environment_list, name='environment-list'),
  path('<int:pk>/', EnvironmentDetailView.as_view(), name='environment-detail'),
  path('create/', EnvironmentCreateView.as_view(), name='environment-create'),
  path('<int:pk>/update/', EnvironmentUpdateView.as_view(), name='environment-update'),
  path('delete/<int:pk>/', EnvironmentDeleteView.as_view(), name='environment-delete'),

  path('upload/', EnvironmentBulkUploadView.as_view(), name='environment-upload'),
  path('downloadcsv/', downloadcsv, name='download-csv'),

]
