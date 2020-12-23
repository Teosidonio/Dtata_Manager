from django.urls import path
from django.contrib import admin

from . import views



urlpatterns = [
  path('', views.index_view, name='home'),
  path('admin/', admin.site.urls),
  path('feature-config', views.featureconfig_view, name='configs'),
  path('main-session/', views.main_session_view, name='main-session'),

  path('dev_cycle_iteration/list/', views.FeatureListView.as_view(), name='feature'),
  path('feature/create/', views.FeatureCreateView.as_view(), name='feature-create'),
  path('feature/<int:pk>/update/',
       views.FeatureUpdateView.as_view(), name='feature-update'),
  path('feature/<int:pk>/delete/',
       views.FeatureDeleteView.as_view(), name='feature-delete'),

  path('dev_list/list/', views.DevListView.as_view(), name='devfeature'),
  path('devfeature/create/', views.DevCreateView.as_view(), name='devfeature-create'),
  path('devfeature/<int:pk>/update/',
       views.DevUpdateView.as_view(), name='devfeature-update'),
  path('devfeature/<int:pk>/delete/',
       views.DevDeleteView.as_view(), name='devfeature-delete'),

  path('feature_list/list/', views.TeamListView.as_view(), name='features'),
  path('features/create/', views.TeamCreateView.as_view(), name='features-create'),
  path('features/<int:pk>/update/',
       views.TeamUpdateView.as_view(), name='features-update'),
  path('features/<int:pk>/delete/',
       views.TeamDeleteView.as_view(), name='features-delete'),

  path('team_list/list/', views.MainFListView.as_view(), name='team'),
  path('team/create/', views.MainFCreateView.as_view(),
       name='team-create'),
  path('team/<int:pk>/update/',
       views.MainFUpdateView.as_view(), name='team-update'),
  path('team/<int:pk>/delete/',
       views.MainFDeleteView.as_view(), name='team-delete'),

]