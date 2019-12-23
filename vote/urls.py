from django.urls import path
from . import views

app_name = 'Vote'
urlpatterns = [
    path('', views.indexView, name='home'),
    path('<int:question_id>/', views.detailView,  name='detail_url'),
    path('<int:question_id>/results/', views.resultView,  name='results_url'),
    path('<int:question_id>/votes/', views.voteView, name='vote_url'),
    path('resultdata/<str:obj>/', views.resultsData, name='resultdata')
]
