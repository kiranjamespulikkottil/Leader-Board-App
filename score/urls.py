from django.urls import path

from . import views

urlpatterns = [
    path('', views.ScoreListView.as_view(), name='home'),
    path('score/<int:pk>/', views.ScoreDetailView.as_view(), name='score_detail'),
    path('score/add/', views.ScoreAddView.as_view(), name='score_add'),
    path('score/<int:pk>/edit', views.ScoreUpdateView.as_view(), name='score_edit'),
    path('score/<int:pk>/delete', views.ScoreDeleteView.as_view(), name='score_delete'),
]
