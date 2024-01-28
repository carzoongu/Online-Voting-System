from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.questions, name='questions'),
    path('<int:question_id>/', views.choices, name = 'choices'),
    path('<int:question_id>/results/', views.results, name = 'results'),
    path('<int:question_id>/vote/', views.vote, name = 'vote'),
    
]
